from sensors.depth_camera import DepthCamera
from reconstruction.mesh_builder import build_mesh
from rendering.lightfield_renderer import render_to_projector
from ai.gesture_recognition import detect_gestures
from ai.control_ai import process_ai
import cv2
import numpy as np

# Initialize camera
cam = DepthCamera()

while True:
    depth, color = cam.get_frames()
    if depth is None or color is None:
        continue

    # Build mesh
    mesh = build_mesh(depth, color, intrinsics=(640, 640, 320, 240))

    # Detect gestures
    gesture = detect_gestures(depth)

    # Process AI (placeholder)
    mesh = process_ai(mesh, gesture)

    # Render to projector
    frame = render_to_projector(mesh)

    # Overlay hand/touch effects
    if gesture == "hand_detected":
        # Simple demo effect at center
        frame = cv2.circle(frame, (frame.shape[1]//2, frame.shape[0]//2), 20, (0, 255, 0), -1)

    # Show output (for bench testing)
    cv2.imshow("Projector Output", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
