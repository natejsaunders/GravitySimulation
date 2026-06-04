# Gravity Simulation

A 2D gravitational physics sandbox built with Pygame.

## Requirements

- Python 3.10+
- Pygame 2.0+

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python gravity.py
```

## Controls

| Input | Action |
|-------|--------|
| Click and drag | Aim a new object (direction and speed based on drag vector) |
| Release mouse | Launch the object |
| Space | Pause / resume simulation |

Objects that travel more than 10 screen widths from the origin are removed.

## Configuration

Edit the constants at the top of `gravity.py`:

- `SCREEN_SIZE` — Window dimensions
- `MAX_FRAMERATE` — Frame rate cap
- `G` — Gravitational constant

Preset objects can be added to the `gravity_objects` list in `main()`.
