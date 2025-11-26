# Setup Guide - Python Digital Paint Pouring Simulator

Complete installation and setup instructions for Windows 11.

## Prerequisites

### Required Software

- **Python 3.10+** - [Download from python.org](https://www.python.org/downloads/)
- **Git** - [Download from git-scm.com](https://git-scm.com/downloads)
- **VS Code** (recommended) - [Download from code.visualstudio.com](https://code.visualstudio.com/)

### Hardware Requirements

**Minimum**:
- CPU: Dual-core processor
- RAM: 4GB
- GPU: Integrated graphics with OpenGL support

**Recommended**:
- CPU: Quad-core processor
- RAM: 8GB+
- GPU: Dedicated GPU (NVIDIA/AMD/Intel with OpenGL 4.3+)

## Installation Steps

### 1. Clone the Repository

```bash
# Clone the develop branch
git clone -b develop https://github.com/WyldKnyght/python-paint-pouring.git
cd python-paint-pouring
```

### 2. Create Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# You should see (venv) in your prompt
```

### 3. Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# For development (includes testing tools)
pip install -r requirements-dev.txt
```

### 4. Verify Installation

```bash
# Check installed packages
pip list

# You should see:
# - taichi
# - pygame
# - numpy
# - pillow
```

## Running the Simulator

### Basic Usage

```bash
# Make sure venv is activated
python -m src.main
```

### Troubleshooting

#### "No module named 'src'" Error

Make sure you're in the project root directory:

```bash
cd python-paint-pouring
python -m src.main
```

#### Taichi GPU Initialization Failed

The simulator automatically falls back to CPU mode. To check:

```python
# In the console output, look for:
# Backend: GPU  (GPU mode working)
# Backend: CPU  (Fallback mode)
```

#### Pygame Display Issues

Try updating your graphics drivers or run in windowed mode.

## Development Setup

### VS Code Configuration

1. **Install Python Extension** (Microsoft)
2. **Open project folder** in VS Code
3. **Select Python interpreter**:
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose the venv interpreter

### Recommended VS Code Extensions

- Python (Microsoft)
- Pylance
- Python Test Explorer
- GitLens
- Better Comments

### VS Code Settings

Create `.vscode/settings.json`:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "[python]": {
        "editor.rulers": [88],
        "editor.tabSize": 4
    }
}
```

## Running Tests

### All Tests

```bash
pytest tests/
```

### With Coverage Report

```bash
pytest tests/ --cov=src --cov-report=html --cov-report=term

# View HTML report
start htmlcov/index.html  # Windows
```

### Specific Test File

```bash
pytest tests/test_particle_system.py -v
```

### Watch Mode (Auto-run on changes)

```bash
pip install pytest-watch
ptw tests/
```

## Code Quality Tools

### Format Code

```bash
# Format all Python files
black src/ tests/

# Check what would be formatted
black src/ tests/ --check
```

### Linting

```bash
# Run flake8
flake8 src/ tests/

# With specific rules
flake8 src/ --max-line-length=88 --extend-ignore=E203
```

### Type Checking

```bash
# Run mypy
mypy src/
```

### Run All Quality Checks

```bash
# Create a script: check_quality.bat
@echo off
echo Running Black...
black src/ tests/ --check
echo.
echo Running Flake8...
flake8 src/ tests/
echo.
echo Running Mypy...
mypy src/
echo.
echo Running Tests...
pytest tests/ --cov=src
echo.
echo All checks complete!
```

## Performance Optimization

### GPU Mode (Best Performance)

Taichi will automatically use GPU if available. To verify:

```bash
# Look for "Backend: GPU" in console output
python -m src.main
```

### CPU Mode (Fallback)

If GPU initialization fails, CPU mode is used automatically.

### Adjusting Particle Count

Edit `src/config.py`:

```python
@dataclass
class PhysicsConfig:
    max_particles: int = 5000  # Reduce for better performance
```

### Frame Rate Adjustment

Edit `src/config.py`:

```python
@dataclass
class RenderConfig:
    fps: int = 30  # Lower for slower computers
```

## Common Issues

### Issue: Virtual Environment Not Activating

**Solution**:

```bash
# PowerShell execution policy issue
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then retry
venv\Scripts\activate
```

### Issue: pip install fails with "No matching distribution"

**Solution**:

```bash
# Update pip
python -m pip install --upgrade pip

# Retry installation
pip install -r requirements.txt
```

### Issue: Taichi installation fails

**Solution**:

```bash
# Install Visual C++ Build Tools
# Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

# Then retry
pip install taichi
```

### Issue: Module import errors

**Solution**:

```bash
# Ensure you're in project root
cd python-paint-pouring

# Run as module
python -m src.main

# NOT: python src/main.py
```

## Updating

### Pull Latest Changes

```bash
# Fetch and merge latest code
git pull origin develop

# Update dependencies
pip install -r requirements.txt --upgrade
```

### Reinstall Dependencies

```bash
# Remove venv
deactivate
rmdir /s venv

# Recreate
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Uninstallation

### Remove Virtual Environment

```bash
# Deactivate
deactivate

# Delete venv folder
rmdir /s venv
```

### Remove Project

```bash
# Navigate to parent directory
cd ..

# Remove project folder
rmdir /s python-paint-pouring
```

## Next Steps

After successful setup:

1. **Run the simulator**: `python -m src.main`
2. **Try the controls**: See README.md for control keys
3. **Run tests**: `pytest tests/`
4. **Explore the code**: Start with `src/main.py`
5. **Make changes**: Follow CONTRIBUTING.md guidelines

## Getting Help

If you encounter issues:

1. Check this guide's troubleshooting section
2. Review README.md for usage information
3. Check GitHub Issues: [github.com/WyldKnyght/python-paint-pouring/issues](https://github.com/WyldKnyght/python-paint-pouring/issues)
4. Contact: WyldKnyght2002@gmail.com

## Resources

- **Python**: https://docs.python.org/3/
- **Taichi**: https://docs.taichi-lang.org/
- **Pygame**: https://www.pygame.org/docs/
- **pytest**: https://docs.pytest.org/
- **VS Code Python**: https://code.visualstudio.com/docs/python/python-tutorial
