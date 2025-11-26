"""Canvas mechanics including tilting and boundary conditions."""

import numpy as np
from typing import Tuple
from dataclasses import dataclass


@dataclass
class TiltState:
    """Current tilt state of canvas."""
    x_angle: float = 0.0
    y_angle: float = 0.0


class Canvas:
    """Manages canvas properties and transformations."""
    
    def __init__(self, width: int, height: int):
        """Initialize canvas.
        
        Args:
            width: Canvas width in pixels
            height: Canvas height in pixels
        """
        self.width = width
        self.height = height
        self.tilt = TiltState()
        
        self.min_tilt = -45.0
        self.max_tilt = 45.0
        self.tilt_step = 5.0
    
    def set_tilt(self, x_angle: float, y_angle: float):
        """Set canvas tilt angles."""
        self.tilt.x_angle = np.clip(x_angle, self.min_tilt, self.max_tilt)
        self.tilt.y_angle = np.clip(y_angle, self.min_tilt, self.max_tilt)
    
    def adjust_tilt(self, dx: float, dy: float):
        """Adjust tilt by delta amounts."""
        new_x = self.tilt.x_angle + dx
        new_y = self.tilt.y_angle + dy
        self.set_tilt(new_x, new_y)
    
    def tilt_left(self):
        """Tilt canvas to the left."""
        self.adjust_tilt(-self.tilt_step, 0)
    
    def tilt_right(self):
        """Tilt canvas to the right."""
        self.adjust_tilt(self.tilt_step, 0)
    
    def tilt_up(self):
        """Tilt canvas upward."""
        self.adjust_tilt(0, -self.tilt_step)
    
    def tilt_down(self):
        """Tilt canvas downward."""
        self.adjust_tilt(0, self.tilt_step)
    
    def reset_tilt(self):
        """Reset canvas to level."""
        self.set_tilt(0.0, 0.0)
    
    def get_gravity_vector(self, base_gravity: float = 9.8) -> Tuple[float, float]:
        """Calculate effective gravity vector."""
        tilt_x_rad = np.radians(self.tilt.x_angle)
        tilt_y_rad = np.radians(self.tilt.y_angle)
        
        gx = base_gravity * np.sin(tilt_x_rad)
        gy = base_gravity * np.sin(tilt_y_rad)
        
        return gx, gy
    
    def get_center(self) -> Tuple[float, float]:
        """Get canvas center coordinates."""
        return self.width / 2, self.height / 2
    
    def get_tilt_display(self) -> str:
        """Get formatted tilt display string."""
        return f"Tilt: X={self.tilt.x_angle:+.1f}° Y={self.tilt.y_angle:+.1f}°"
