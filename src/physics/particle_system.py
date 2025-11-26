"""Taichi-based particle system for paint simulation."""

import taichi as ti
import numpy as np
from typing import Tuple
from src.config import Config


@ti.data_oriented
class ParticleSystem:
    """GPU-accelerated particle system using Taichi.
    
    Handles particle creation, physics updates, and state management.
    Uses Smoothed Particle Hydrodynamics (SPH) principles.
    """
    
    def __init__(self, config: Config):
        """Initialize particle system.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.max_particles = config.physics.max_particles
        
        # Initialize Taichi
        try:
            ti.init(arch=ti.gpu)
            self.backend = "GPU"
        except Exception:
            ti.init(arch=ti.cpu)
            self.backend = "CPU"
        
        # Particle count
        self.num_particles = ti.field(dtype=ti.i32, shape=())
        self.num_particles[None] = 0
        
        # Particle properties
        self.position = ti.Vector.field(2, dtype=ti.f32, shape=self.max_particles)
        self.velocity = ti.Vector.field(2, dtype=ti.f32, shape=self.max_particles)
        self.color = ti.Vector.field(4, dtype=ti.f32, shape=self.max_particles)
        self.density = ti.field(dtype=ti.f32, shape=self.max_particles)
        self.viscosity = ti.field(dtype=ti.f32, shape=self.max_particles)
        self.is_active = ti.field(dtype=ti.i32, shape=self.max_particles)
        
        # Canvas properties
        self.canvas_width = float(config.canvas.width)
        self.canvas_height = float(config.canvas.height)
        
        # Physics parameters
        self.gravity = ti.field(dtype=ti.f32, shape=())
        self.gravity[None] = config.physics.gravity
        self.friction = config.physics.friction
        
        # Tilt angles
        self.tilt_x = ti.field(dtype=ti.f32, shape=())
        self.tilt_y = ti.field(dtype=ti.f32, shape=())
        self.tilt_x[None] = 0.0
        self.tilt_y[None] = 0.0
    
    @ti.kernel
    def add_particles(
        self,
        center_x: ti.f32,
        center_y: ti.f32,
        count: ti.i32,
        color: ti.types.vector(4, ti.f32),
        paint_density: ti.f32,
        paint_viscosity: ti.f32
    ):
        """Add particles at position."""
        start_idx = self.num_particles[None]
        
        for i in range(count):
            if start_idx + i < self.max_particles:
                idx = start_idx + i
                
                # Random circular distribution
                angle = ti.random() * 2.0 * 3.14159
                radius = ti.sqrt(ti.random()) * 10.0
                offset_x = radius * ti.cos(angle)
                offset_y = radius * ti.sin(angle)
                
                self.position[idx] = ti.Vector([center_x + offset_x, center_y + offset_y])
                self.velocity[idx] = ti.Vector([0.0, 0.0])
                self.color[idx] = color
                self.density[idx] = paint_density
                self.viscosity[idx] = paint_viscosity
                self.is_active[idx] = 1
        
        self.num_particles[None] = ti.min(start_idx + count, self.max_particles)
    
    @ti.kernel
    def update(self, dt: ti.f32):
        """Update particle physics."""
        # Calculate gravity from tilt
        tilt_x_rad = self.tilt_x[None] * 3.14159 / 180.0
        tilt_y_rad = self.tilt_y[None] * 3.14159 / 180.0
        
        gravity_x = self.gravity[None] * ti.sin(tilt_x_rad)
        gravity_y = self.gravity[None] * ti.sin(tilt_y_rad)
        
        for i in range(self.num_particles[None]):
            if self.is_active[i] == 1:
                # Apply gravity with viscosity dampening
                viscosity_factor = 1.0 / (1.0 + self.viscosity[i] * 0.001)
                
                accel_x = gravity_x * viscosity_factor
                accel_y = gravity_y * viscosity_factor
                
                self.velocity[i].x += accel_x * dt
                self.velocity[i].y += accel_y * dt
                
                # Apply friction
                self.velocity[i] *= self.friction
                
                # Update position
                self.position[i] += self.velocity[i] * dt
                
                # Boundary collision
                if self.position[i].x < 0:
                    self.position[i].x = 0
                    self.velocity[i].x *= -0.5
                elif self.position[i].x > self.canvas_width:
                    self.position[i].x = self.canvas_width
                    self.velocity[i].x *= -0.5
                
                if self.position[i].y < 0:
                    self.position[i].y = 0
                    self.velocity[i].y *= -0.5
                elif self.position[i].y > self.canvas_height:
                    self.position[i].y = self.canvas_height
                    self.velocity[i].y *= -0.5
    
    def set_tilt(self, tilt_x: float, tilt_y: float):
        """Set canvas tilt angles."""
        self.tilt_x[None] = np.clip(tilt_x, -45.0, 45.0)
        self.tilt_y[None] = np.clip(tilt_y, -45.0, 45.0)
    
    def get_particle_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """Get particle data for rendering."""
        n = self.num_particles[None]
        if n == 0:
            return np.array([]), np.array([])
        
        positions = self.position.to_numpy()[:n]
        colors = self.color.to_numpy()[:n]
        return positions, colors
    
    def get_particle_count(self) -> int:
        """Get current particle count."""
        return self.num_particles[None]
    
    def get_backend(self) -> str:
        """Get Taichi backend."""
        return self.backend
    
    @ti.kernel
    def reset(self):
        """Reset all particles."""
        self.num_particles[None] = 0
        for i in range(self.max_particles):
            self.is_active[i] = 0
