# AERIS Phone

AERIS is an embedded spatial-computing software stack for RGB/depth capture, point-cloud reconstruction, gesture interaction, projector output, and an AI control layer designed for future LMLM integration.

The repository is hardware-aware but simulation-first: `python main.py --simulate` runs without a RealSense camera, projector, microphone, or LMLM backend. Hardware adapters become active when their optional dependencies and devices are available.

## Architecture

```
camera -> RGB/depth frames -> point cloud -> mesh -> spatial renderer
                         \-> gesture detector -> interaction effects
AI/LMLM control <--------------------------------------/
```

## Run

```bash
python -m pip install -r requirements.txt
python main.py --simulate
```

For a RealSense deployment:

```bash
python main.py --camera realsense --headless
```

The current renderer is a projector-frame/mesh preview, not a physical hologram generator. A true light-field or diffractive display still requires the optical hardware and its calibration model.

## Layout

- `sensors/` — RGB, depth and microphone adapters
- `reconstruction/` — point cloud and mesh construction
- `rendering/` — projector/light-field preview and interaction overlays
- `ai/` — gesture and LMLM control boundary
- `networking/` — call/streaming primitives
- `system/` — battery, thermal and power abstractions
- `config/` — YAML configuration
- `tests/` — hardware-independent tests

## Safety

Do not connect an unknown battery pack directly to embedded hardware. Match voltage/current requirements to the actual board and peripherals, and validate projector optics before prolonged operation.
