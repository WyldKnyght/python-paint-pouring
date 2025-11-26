"""Pygame-based particle renderer."""

import pygame
import numpy as np
from typing import Tuple
from src.config import Config


class ParticleRenderer:
    """Render particles using Pygame (Phase 1).
    
    This is the initial renderer using Pygame for prototyping.
    Will be replaced with ModernGL in Phase 3+ for better performance.
    """
    
    def __init__(self, config: Config, screen: pygame.Surface):
        """Initialize renderer.
        
        Args:
            config: Configuration object
            screen: Pygame surface to render to
        """
        self.config = config
        self.screen = screen
        self.particle_size = config.render.particle_size
        
        # Convert background color from 0-1 to 0-255
        bg = config.canvas.background_color
        self.background_color = bg
    
    def clear(self):
        """Clear the screen with background color."""
        self.screen.fill(self.background_color)
    
    def render_particles(self, positions: np.ndarray, colors: np.ndarray):
        """Render all particles.
        
        Args:
            positions: Nx2 array of (x, y) positions
            colors: Nx4 array of (r, g, b, a) colors (0-1 range)
        """
        if len(positions) == 0:
            return
        
        # Convert colors from 0-1 to 0-255
        colors_255 = (colors[:, :3] * 255).astype(int)
        alphas = colors[:, 3]
        
        # Create temporary surface for alpha blending
        temp_surface = pygame.Surface(
            (self.particle_size * 2, self.particle_size * 2),
            pygame.SRCALPHA
        )
        
        # Draw each particle
        for i in range(len(positions)):
            pos = positions[i].astype(int)
            color = colors_255[i]
            alpha = int(alphas[i] * 255)
            
            # Draw particle with alpha
            temp_surface.fill((0, 0, 0, 0))  # Clear temp surface
            pygame.draw.circle(
                temp_surface,
                (*color, alpha),
                (self.particle_size, self.particle_size),
                self.particle_size
            )
            
            # Blit to screen
            self.screen.blit(
                temp_surface,
                (pos[0] - self.particle_size, pos[1] - self.particle_size)
            )
    
    def render_ui_text(
        self,
        text: str,
        position: Tuple[int, int],
        color: Tuple[int, int, int] = (50, 50, 50),
        size: int = 20
    ):
        """Render UI text.
        
        Args:
            text: Text to render
            position: (x, y) position
            color: RGB color tuple (0-255)
            size: Font size
        """
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, position)
