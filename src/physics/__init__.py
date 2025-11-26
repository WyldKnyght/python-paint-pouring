"""Physics simulation module.

Contains particle system, fluid dynamics, and canvas mechanics.
"""

from src.physics.particle_system import ParticleSystem
from src.physics.fluid_dynamics import FluidDynamics
from src.physics.canvas import Canvas

__all__ = ["ParticleSystem", "FluidDynamics", "Canvas"]
