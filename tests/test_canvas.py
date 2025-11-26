"""Tests for canvas mechanics."""

import pytest
import numpy as np
from src.physics.canvas import Canvas, TiltState


@pytest.fixture
def canvas():
    """Create canvas instance."""
    return Canvas(800, 600)


class TestCanvas:
    """Test canvas functionality."""
    
    def test_initialization(self, canvas):
        """Test canvas initializes correctly."""
        assert canvas.width == 800
        assert canvas.height == 600
        assert canvas.tilt.x_angle == 0.0
        assert canvas.tilt.y_angle == 0.0
    
    def test_set_tilt(self, canvas):
        """Test setting tilt angles."""
        canvas.set_tilt(15.0, -20.0)
        
        assert canvas.tilt.x_angle == 15.0
        assert canvas.tilt.y_angle == -20.0
    
    def test_tilt_bounds(self, canvas):
        """Test tilt angle bounds."""
        # Try to set beyond limits
        canvas.set_tilt(60.0, -60.0)
        
        # Should be clamped
        assert canvas.tilt.x_angle == 45.0
        assert canvas.tilt.y_angle == -45.0
    
    def test_adjust_tilt(self, canvas):
        """Test adjusting tilt incrementally."""
        canvas.set_tilt(10.0, 10.0)
        canvas.adjust_tilt(5.0, -3.0)
        
        assert canvas.tilt.x_angle == 15.0
        assert canvas.tilt.y_angle == 7.0
    
    def test_tilt_directions(self, canvas):
        """Test directional tilt methods."""
        canvas.tilt_right()
        assert canvas.tilt.x_angle == 5.0
        
        canvas.tilt_left()
        assert canvas.tilt.x_angle == 0.0
        
        canvas.tilt_down()
        assert canvas.tilt.y_angle == 5.0
        
        canvas.tilt_up()
        assert canvas.tilt.y_angle == 0.0
    
    def test_reset_tilt(self, canvas):
        """Test resetting tilt to level."""
        canvas.set_tilt(30.0, -25.0)
        canvas.reset_tilt()
        
        assert canvas.tilt.x_angle == 0.0
        assert canvas.tilt.y_angle == 0.0
    
    def test_gravity_vector(self, canvas):
        """Test gravity vector calculation."""
        canvas.set_tilt(0.0, 0.0)
        gx, gy = canvas.get_gravity_vector()
        
        # At level, gravity should be near zero horizontally
        assert abs(gx) < 0.1
        assert abs(gy) < 0.1
        
        # With tilt, should have horizontal component
        canvas.set_tilt(30.0, 0.0)
        gx, gy = canvas.get_gravity_vector()
        assert abs(gx) > 0.1
    
    def test_get_center(self, canvas):
        """Test getting canvas center."""
        cx, cy = canvas.get_center()
        
        assert cx == 400.0
        assert cy == 300.0
    
    def test_tilt_display(self, canvas):
        """Test tilt display string."""
        canvas.set_tilt(15.5, -10.2)
        display = canvas.get_tilt_display()
        
        assert "15.5" in display or "15.5" in display
        assert "10.2" in display or "10.2" in display
