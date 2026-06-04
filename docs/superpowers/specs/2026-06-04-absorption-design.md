# Small Object Absorption

## Summary
Smaller GravityObjects that fully enter larger GravityObjects get absorbed — the larger gains the smaller's mass (with radius recalculated from density) and their velocities combine via momentum conservation.

## Detection
After all positions are updated each frame, the main loop checks each pair of objects. If `distance(center_a, center_b) + smaller.radius <= larger.radius`, the smaller is fully contained and gets absorbed.

## Behavior
- **Mass:** `larger.mass += smaller.mass`
- **Radius:** Recalculated as `sqrt(mass / (pi * density))` — density stays constant per object
- **Velocity:** Momentum-conserving `v = (m1*v1 + m2*v2) / (m1 + m2)`
- **Removal:** The smaller object is removed from `gravity_objects`

## Changes
### `gravity_object.py`
- Add `absorb(self, other)` method updating mass, radius, and velocity

### `gravity.py`
- Add absorption check loop after the update loop in `main()`
