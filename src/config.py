"""Configuration settings for the paint pouring simulator."""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class CanvasConfig:
    """Canvas configuration."""
    width: int = 800
    height: int = 600
    background_color: Tuple[int, int, int] = (242, 242, 238)  # Cream


@dataclass
class PhysicsConfig:
    """Physics simulation configuration."""
    max_particles: int = 10000
    gravity: float = 9.8
    friction: float = 0.98
    time_step: float = 0.016  # 16ms ~= 60 FPS
    
    # Viscosity presets (cP - centipoise)
    viscosity_very_thin: float = 100.0  # Dutch pour
    viscosity_medium: float = 300.0     # Standard
    viscosity_thick: float = 500.0      # Ring pour
    viscosity_very_thick: float = 800.0 # Heavy body


@dataclass
class RenderConfig:
    """Rendering configuration."""
    fps: int = 60
    particle_size: int = 5
    vsync: bool = True


@dataclass
class UIConfig:
    """User interface configuration."""
    window_title: str = "Digital Paint Pouring Simulator"
    show_fps: bool = True
    show_particle_count: bool = True


class Config:
    """Main configuration container."""
    
    def __init__(self):
        self.canvas = CanvasConfig()
        self.physics = PhysicsConfig()
        self.render = RenderConfig()
        self.ui = UIConfig()
    
    # Color presets (R, G, B, A) - normalized 0-1
    COLOR_PRESETS = {
        "white": (1.0, 1.0, 1.0, 1.0),
        "black": (0.0, 0.0, 0.0, 1.0),
        "red": (0.9, 0.2, 0.2, 1.0),
        "blue": (0.2, 0.5, 0.9, 1.0),
        "yellow": (0.95, 0.9, 0.2, 1.0),
        "green": (0.2, 0.8, 0.3, 1.0),
        "purple": (0.6, 0.2, 0.8, 1.0),
        "orange": (0.95, 0.6, 0.2, 1.0),
        "turquoise": (0.2, 0.9, 0.8, 1.0),
        "magenta": (0.9, 0.2, 0.7, 1.0),
    }


# Global configuration instance
config = Config()
