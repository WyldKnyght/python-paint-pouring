"""Fluid dynamics calculations for paint behavior."""

import numpy as np
from typing import Tuple


class FluidDynamics:
    """Calculate fluid flow and interaction properties.
    
    Implements simplified Smoothed Particle Hydrodynamics (SPH).
    """
    
    def __init__(self):
        """Initialize fluid dynamics calculator."""
        self.smoothing_radius = 15.0
        self.rest_density = 1000.0
        self.gas_constant = 2000.0
        self.viscosity_coefficient = 0.01
    
    def calculate_flow_velocity(
        self,
        tilt_x: float,
        tilt_y: float,
        viscosity: float,
        gravity: float = 9.8
    ) -> Tuple[float, float]:
        """Calculate expected flow velocity from tilt and viscosity.
        
        Args:
            tilt_x: Tilt angle around X axis (degrees)
            tilt_y: Tilt angle around Y axis (degrees)
            viscosity: Paint viscosity (cP)
            gravity: Gravitational acceleration (m/s²)
        
        Returns:
            Tuple of (vx, vy) velocity components
        """
        tilt_x_rad = np.radians(tilt_x)
        tilt_y_rad = np.radians(tilt_y)
        
        gravity_x = gravity * np.sin(tilt_x_rad)
        gravity_y = gravity * np.sin(tilt_y_rad)
        
        viscosity_factor = 1.0 / (1.0 + viscosity * 0.001)
        
        vx = gravity_x * viscosity_factor
        vy = gravity_y * viscosity_factor
        
        return vx, vy
