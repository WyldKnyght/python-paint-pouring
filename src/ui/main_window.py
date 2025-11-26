"""Main application window with Pygame."""

import pygame
import taichi as ti
from src.config import Config
from src.physics.particle_system import ParticleSystem
from src.physics.canvas import Canvas
from src.rendering.renderer import ParticleRenderer


class PaintPouringWindow:
    """Main application window.
    
    Handles event processing, rendering, and simulation updates.
    """
    
    def __init__(self, config: Config):
        """Initialize main window.
        
        Args:
            config: Configuration object
        """
        self.config = config
        
        # Create Pygame window
        self.screen = pygame.display.set_mode(
            (config.canvas.width, config.canvas.height)
        )
        pygame.display.set_caption(config.ui.window_title)
        
        # Initialize components
        self.particle_system = ParticleSystem(config)
        self.canvas = Canvas(config.canvas.width, config.canvas.height)
        self.renderer = ParticleRenderer(config, self.screen)
        
        # Simulation state
        self.running = True
        self.paused = False
        self.clock = pygame.time.Clock()
        
        # Current paint settings
        self.current_color = config.COLOR_PRESETS["blue"]
        self.current_viscosity = config.physics.viscosity_medium
        self.current_density = 1.0
        
        # Color preset keys
        self.color_keys = {
            pygame.K_1: "white",
            pygame.K_2: "black",
            pygame.K_3: "red",
            pygame.K_4: "blue",
            pygame.K_5: "yellow",
            pygame.K_6: "green",
            pygame.K_7: "purple",
            pygame.K_8: "orange",
            pygame.K_9: "turquoise",
        }
    
    def handle_events(self):
        """Process user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.add_paint_at_mouse()
            
            elif event.type == pygame.KEYDOWN:
                self.handle_keypress(event.key)
    
    def handle_keypress(self, key: int):
        """Handle keyboard input.
        
        Args:
            key: Pygame key constant
        """
        # Color selection (1-9 keys)
        if key in self.color_keys:
            color_name = self.color_keys[key]
            self.current_color = self.config.COLOR_PRESETS[color_name]
            print(f"Selected color: {color_name}")
        
        # Canvas tilting (arrow keys)
        elif key == pygame.K_LEFT:
            self.canvas.tilt_left()
            self.update_particle_system_tilt()
        elif key == pygame.K_RIGHT:
            self.canvas.tilt_right()
            self.update_particle_system_tilt()
        elif key == pygame.K_UP:
            self.canvas.tilt_up()
            self.update_particle_system_tilt()
        elif key == pygame.K_DOWN:
            self.canvas.tilt_down()
            self.update_particle_system_tilt()
        
        # Viscosity adjustment
        elif key == pygame.K_EQUALS or key == pygame.K_PLUS:
            self.current_viscosity = min(self.current_viscosity + 50, 1000)
            print(f"Viscosity: {self.current_viscosity}")
        elif key == pygame.K_MINUS:
            self.current_viscosity = max(self.current_viscosity - 50, 50)
            print(f"Viscosity: {self.current_viscosity}")
        
        # Simulation controls
        elif key == pygame.K_SPACE:
            self.paused = not self.paused
            print(f"{'Paused' if self.paused else 'Resumed'}")
        elif key == pygame.K_r:
            self.reset_simulation()
        
        # Export (placeholder for Phase 5)
        elif key == pygame.K_e:
            print("Export feature coming in Phase 5!")
        elif key == pygame.K_s:
            print("Save recipe feature coming in Phase 5!")
    
    def add_paint_at_mouse(self):
        """Add paint particles at current mouse position."""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        # Convert color tuple to Taichi vector
        color_vec = ti.Vector(self.current_color)
        
        # Add 300 particles
        self.particle_system.add_particles(
            float(mouse_x),
            float(mouse_y),
            300,
            color_vec,
            self.current_density,
            self.current_viscosity
        )
    
    def update_particle_system_tilt(self):
        """Update particle system with current canvas tilt."""
        self.particle_system.set_tilt(
            self.canvas.tilt.x_angle,
            self.canvas.tilt.y_angle
        )
    
    def reset_simulation(self):
        """Reset the simulation."""
        self.particle_system.reset()
        self.canvas.reset_tilt()
        self.update_particle_system_tilt()
        print("Canvas reset")
    
    def update(self):
        """Update simulation physics."""
        if not self.paused:
            dt = self.config.physics.time_step
            self.particle_system.update(dt)
    
    def render(self):
        """Render the current frame."""
        # Clear screen
        self.renderer.clear()
        
        # Get particle data and render
        positions, colors = self.particle_system.get_particle_data()
        self.renderer.render_particles(positions, colors)
        
        # Render UI info
        if self.config.ui.show_particle_count:
            count_text = f"Particles: {self.particle_system.get_particle_count()}"
            self.renderer.render_ui_text(count_text, (10, 10))
        
        if self.config.ui.show_fps:
            fps_text = f"FPS: {int(self.clock.get_fps())}"
            self.renderer.render_ui_text(fps_text, (10, 30))
        
        # Show tilt
        tilt_text = self.canvas.get_tilt_display()
        self.renderer.render_ui_text(tilt_text, (10, 50))
        
        # Show backend
        backend_text = f"Backend: {self.particle_system.get_backend()}"
        self.renderer.render_ui_text(backend_text, (10, 70))
        
        # Show current viscosity
        visc_text = f"Viscosity: {int(self.current_viscosity)} cP"
        self.renderer.render_ui_text(visc_text, (10, 90))
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main application loop."""
        print("\n" + "="*50)
        print("Python Digital Paint Pouring Simulator")
        print("="*50)
        print(f"Backend: {self.particle_system.get_backend()}")
        print(f"Max particles: {self.config.physics.max_particles}")
        print("\nControls:")
        print("  Left Click: Add paint")
        print("  1-9: Select color")
        print("  Arrow Keys: Tilt canvas")
        print("  +/-: Adjust viscosity")
        print("  Space: Pause/Resume")
        print("  R: Reset canvas")
        print("  ESC/Close: Exit")
        print("="*50 + "\n")
        
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.config.render.fps)
        
        print("\nSimulator closed. Thank you!")
