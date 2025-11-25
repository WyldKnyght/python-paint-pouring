# Python Digital Paint Pouring Simulator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A GPU-accelerated digital paint pouring simulator built with Python, Taichi Lang, and Pygame. This project simulates realistic fluid dynamics for creating digital paint pouring art.

## 🎨 Features

**Phase 1 (Current):**
- ✅ GPU-accelerated particle physics with Taichi
- ✅ Real-time fluid simulation
- ✅ Canvas tilting mechanics
- ✅ Multiple paint colors with different viscosities
- ✅ Interactive controls

**Upcoming Phases:**
- 🔜 ModernGL rendering for advanced graphics
- 🔜 PyQt6 professional UI
- 🔜 Cell formation algorithms
- 🔜 Export to image/video
- 🔜 Recipe saving system

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Windows 11 (primary), macOS or Linux
- GPU recommended (NVIDIA/AMD/Intel with OpenGL support)

### Installation

```bash
# Clone the repository
git clone https://github.com/WyldKnyght/python-paint-pouring.git
cd python-paint-pouring

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Simulator

```bash
python -m src.main
```

## 📁 Project Structure

```
paint_pouring_simulator/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Application entry point
│   ├── config.py               # Configuration settings
│   ├── physics/
│   │   ├── __init__.py
│   │   ├── particle_system.py  # Taichi particle physics
│   │   ├── fluid_dynamics.py   # Flow calculations
│   │   └── canvas.py           # Canvas tilting logic
│   ├── rendering/
│   │   ├── __init__.py
│   │   └── renderer.py         # Pygame renderer (Phase 1)
│   └── ui/
│       ├── __init__.py
│       └── main_window.py      # Main UI window
├── tests/
│   ├── __init__.py
│   ├── test_particle_system.py
│   ├── test_fluid_dynamics.py
│   └── test_canvas.py
├── data/
│   ├── exports/                # Exported images/videos
│   └── recipes/                # Saved paint recipes
├── docs/
│   ├── ARCHITECTURE.md
│   ├── PHYSICS.md
│   └── CONTRIBUTING.md
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── .gitignore
└── README.md
```

## 🎮 Controls

- **Left Click**: Add paint at cursor position
- **1-9 Keys**: Select paint color presets
- **Arrow Keys**: Tilt canvas
- **Space**: Pause/Resume simulation
- **R**: Reset canvas
- **+/-**: Adjust viscosity
- **S**: Save current state
- **E**: Export as image

## 🧪 Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_particle_system.py -v
```

## 🔧 Configuration

Edit `src/config.py` to customize:

- Canvas size and resolution
- Maximum particle count
- Physics parameters (gravity, friction)
- Default paint viscosities
- Color presets

## 📊 Performance

**Expected Performance (Phase 1 - Pygame):**
- 1,000-3,000 particles @ 30-60 FPS (CPU)
- 5,000-10,000 particles @ 30-60 FPS (GPU with Taichi)

**Planned Performance (Phase 3+ - ModernGL):**
- 20,000-50,000 particles @ 60 FPS (GPU)

## 🛠️ Technology Stack

- **Physics Engine**: Taichi Lang (GPU-accelerated)
- **Rendering**: Pygame (Phase 1), ModernGL (Phase 3+)
- **UI Framework**: Pygame (Phase 1), PyQt6 (Phase 3+)
- **Testing**: pytest, pytest-cov
- **Code Quality**: black, flake8, mypy

## 🧑‍💻 Development Principles

This project follows:

- **SOLID Principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **Clean Code**: DRY, small functions, descriptive names, minimal arguments
- **PEP 8**: Python standard naming conventions
- **Type Hints**: Full type annotation for better IDE support
- **Testing**: Unit tests with >80% coverage target

## 📖 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [Physics Implementation](docs/PHYSICS.md)
- [Contributing Guidelines](docs/CONTRIBUTING.md)

## 🗺️ Roadmap

### Phase 1-2: Foundation (Weeks 1-6) ✅
- [x] Project setup and structure
- [x] Taichi particle system
- [x] Basic Pygame rendering
- [x] Canvas tilting mechanics
- [x] UI controls

### Phase 3-5: Core Features (Weeks 7-16)
- [ ] ModernGL renderer integration
- [ ] PyQt6 professional UI
- [ ] Cell formation algorithms
- [ ] Advanced fluid dynamics (SPH)
- [ ] Image export functionality

### Phase 6-7: Polish (Weeks 17-22)
- [ ] Video export (MP4)
- [ ] Recipe saving/loading
- [ ] Preset paint collections
- [ ] Undo/Redo system
- [ ] Performance optimization

### Phase 8-10: Advanced (Weeks 23+)
- [ ] AI-assisted composition
- [ ] Realistic physics refinements
- [ ] Multi-layer support
- [ ] Texture overlays
- [ ] Community sharing features

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Taichi Lang](https://www.taichi-lang.org/) for GPU acceleration framework
- [ModernGL](https://moderngl.readthedocs.io/) for modern OpenGL rendering
- [Pygame](https://www.pygame.org/) for rapid prototyping
- Fluid art community for inspiration

## 📧 Contact

- **Author**: Craig Myers (WyldKnyght)
- **GitHub**: [@WyldKnyght](https://github.com/WyldKnyght)
- **Email**: WyldKnyght2002@gmail.com

---

**Note**: This is a Phase 1 implementation. Features and performance will improve significantly in upcoming phases.