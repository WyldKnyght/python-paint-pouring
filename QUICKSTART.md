# ⚡ Quick Start - 5 Minutes to Paint Pouring!

## Step 1: Clone & Setup (2 minutes)

```bash
# Clone the repository
git clone -b develop https://github.com/WyldKnyght/python-paint-pouring.git
cd python-paint-pouring

# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Run (30 seconds)

```bash
python -m src.main
```

## Step 3: Create Art! (2+ minutes)

### Basic Controls

| Action | Control |
|--------|--------|
| 🎨 Add paint | **Left Click** |
| 🎨 Choose color | **1-9 keys** |
| ⬆️⬇️⬅️➡️ Tilt canvas | **Arrow keys** |
| 💧 Thinner paint | **- key** |
| 🍯 Thicker paint | **+ key** |
| ⏸️ Pause | **Space** |
| 🔄 Reset | **R key** |

### Try This First!

1. **Press 4** (blue color)
2. **Click** anywhere on canvas
3. **Press 3** (red color)  
4. **Click** next to the blue
5. **Press →** (tilt right) - watch it flow!
6. **Press 5** (yellow color)
7. **Click** in the middle
8. **Press ↓** (tilt down)

🎉 You're creating digital paint art!

## Color Palette

| Key | Color | Best For |
|-----|-------|----------|
| **1** | White | Highlights, cells |
| **2** | Black | Contrast, depth |
| **3** | Red | Bold accents |
| **4** | Blue | Base layer |
| **5** | Yellow | Brightness |
| **6** | Green | Nature themes |
| **7** | Purple | Mystery |
| **8** | Orange | Warmth |
| **9** | Turquoise | Cool tones |

## Viscosity Guide

**Default: 300 cP (Medium)**

- **100 cP** (press - many times): Thin, flows fast - Dutch pour style
- **300 cP**: Standard acrylic paint
- **500 cP** (press + a few times): Thick - ring pour style
- **800 cP** (press + many times): Very thick - heavy body

## Tips for Great Results

✅ **Start with one color**, let it spread
✅ **Add contrasting colors** at edges
✅ **Use arrow keys gradually** - small tilts work best
✅ **Experiment with viscosity** - each paint behaves differently
✅ **Reset often (R key)** - practice makes perfect!

## Performance Tips

If it's slow:

1. **Check backend** in console:
   - "Backend: GPU" = Fast! ✅
   - "Backend: CPU" = Slower, use fewer particles

2. **Reduce particles** per click:
   - Edit `src/ui/main_window.py` line ~118
   - Change `300` to `100` or `50`

3. **Lower FPS**:
   - Edit `src/config.py`
   - Change `fps: int = 60` to `fps: int = 30`

## Troubleshooting

### "No module named 'src'"
```bash
# Make sure you're in project root
cd python-paint-pouring
python -m src.main
```

### Virtual environment not activating
```bash
# Windows PowerShell execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
```

### Taichi installation fails
```bash
# Install Visual C++ Build Tools first
# Then: pip install taichi
```

## What's Next?

- 📚 Read full [README.md](README.md) for all features
- 🔧 See [SETUP.md](SETUP.md) for development setup
- 🧪 Run tests: `pytest tests/`
- 💬 Share your creations!

## Need Help?

- **GitHub Issues**: [Report bugs or request features](https://github.com/WyldKnyght/python-paint-pouring/issues)
- **Email**: WyldKnyght2002@gmail.com

---

**Now go create something beautiful! 🎨✨**
