"""Tests for fluid dynamics calculations."""

import pytest
import numpy as np
from src.physics.fluid_dynamics import FluidDynamics


@pytest.fixture
def fluid_dynamics():
    """Create fluid dynamics instance."""
    return FluidDynamics()


class TestFluidDynamics:
    """Test fluid dynamics functionality."""
    
    def test_initialization(self, fluid_dynamics):
        """Test fluid dynamics initializes correctly."""
        assert fluid_dynamics.smoothing_radius > 0
        assert fluid_dynamics.rest_density > 0
        assert fluid_dynamics.gas_constant > 0
    
    def test_flow_velocity_level(self, fluid_dynamics):
        """Test flow velocity on level canvas."""
        vx, vy = fluid_dynamics.calculate_flow_velocity(0.0, 0.0, 300.0)
        
        # On level surface, velocity should be near zero
        assert abs(vx) < 0.1
        assert abs(vy) < 0.1
    
    def test_flow_velocity_tilted(self, fluid_dynamics):
        """Test flow velocity on tilted canvas."""
        vx, vy = fluid_dynamics.calculate_flow_velocity(30.0, 0.0, 300.0)
        
        # With tilt, should have flow in x direction
        assert abs(vx) > 0.1
    
    def test_viscosity_effect(self, fluid_dynamics):
        """Test viscosity affects flow velocity."""
        # Low viscosity should flow faster
        vx_low, _ = fluid_dynamics.calculate_flow_velocity(30.0, 0.0, 100.0)
        
        # High viscosity should flow slower
        vx_high, _ = fluid_dynamics.calculate_flow_velocity(30.0, 0.0, 800.0)
        
        assert abs(vx_low) > abs(vx_high)
    
    def test_tilt_direction(self, fluid_dynamics):
        """Test flow direction matches tilt direction."""
        # Positive tilt should give positive velocity
        vx_pos, _ = fluid_dynamics.calculate_flow_velocity(30.0, 0.0, 300.0)
        assert vx_pos > 0
        
        # Negative tilt should give negative velocity
        vx_neg, _ = fluid_dynamics.calculate_flow_velocity(-30.0, 0.0, 300.0)
        assert vx_neg < 0
