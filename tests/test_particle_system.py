"""Tests for particle system."""

import pytest
import taichi as ti
import numpy as np
from src.config import Config
from src.physics.particle_system import ParticleSystem


@pytest.fixture
def config():
    """Create test configuration."""
    return Config()


@pytest.fixture
def particle_system(config):
    """Create particle system instance."""
    return ParticleSystem(config)


class TestParticleSystem:
    """Test particle system functionality."""
    
    def test_initialization(self, particle_system):
        """Test particle system initializes correctly."""
        assert particle_system.get_particle_count() == 0
        assert particle_system.get_backend() in ["GPU", "CPU"]
    
    def test_add_particles(self, particle_system):
        """Test adding particles."""
        color = ti.Vector([1.0, 0.0, 0.0, 1.0])
        particle_system.add_particles(100.0, 100.0, 50, color, 1.0, 300.0)
        
        assert particle_system.get_particle_count() == 50
    
    def test_particle_data(self, particle_system):
        """Test getting particle data."""
        color = ti.Vector([0.0, 1.0, 0.0, 1.0])
        particle_system.add_particles(200.0, 200.0, 100, color, 1.0, 500.0)
        
        positions, colors = particle_system.get_particle_data()
        
        assert len(positions) == 100
        assert len(colors) == 100
        assert positions.shape == (100, 2)
        assert colors.shape == (100, 4)
    
    def test_update(self, particle_system):
        """Test physics update."""
        color = ti.Vector([0.0, 0.0, 1.0, 1.0])
        particle_system.add_particles(400.0, 300.0, 10, color, 1.0, 300.0)
        
        positions_before, _ = particle_system.get_particle_data()
        
        # Update physics
        particle_system.update(0.016)
        
        positions_after, _ = particle_system.get_particle_data()
        
        # Positions should remain similar (no tilt, so minimal movement)
        assert positions_before.shape == positions_after.shape
    
    def test_tilt(self, particle_system):
        """Test canvas tilting."""
        particle_system.set_tilt(10.0, -5.0)
        
        # Tilt should be within bounds
        assert -45.0 <= particle_system.tilt_x[None] <= 45.0
        assert -45.0 <= particle_system.tilt_y[None] <= 45.0
    
    def test_reset(self, particle_system):
        """Test reset functionality."""
        color = ti.Vector([1.0, 1.0, 0.0, 1.0])
        particle_system.add_particles(300.0, 300.0, 200, color, 1.0, 300.0)
        
        assert particle_system.get_particle_count() == 200
        
        particle_system.reset()
        
        assert particle_system.get_particle_count() == 0
    
    def test_max_particles(self, particle_system):
        """Test maximum particle limit."""
        color = ti.Vector([1.0, 0.0, 1.0, 1.0])
        max_p = particle_system.max_particles
        
        # Try to add more than max
        particle_system.add_particles(400.0, 400.0, max_p + 100, color, 1.0, 300.0)
        
        # Should be capped at max
        assert particle_system.get_particle_count() == max_p
