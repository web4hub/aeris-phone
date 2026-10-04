from __future__ import annotations
import numpy as np

try:
    import open3d as o3d
except ImportError:
    o3d = None


def build_pointcloud(depth_image, color_image, intrinsics, depth_scale=0.001):
    if o3d is None:
        raise RuntimeError("open3d is not installed")
    fx, fy, cx, cy = intrinsics
    depth = o3d.geometry.Image(np.asarray(depth_image).astype(np.uint16))
    color = o3d.geometry.Image(np.asarray(color_image).astype(np.uint8))
    rgbd = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color, depth, depth_scale=1.0 / depth_scale, depth_trunc=8.0, convert_rgb_to_intensity=False
    )
    camera = o3d.camera.PinholeCameraIntrinsic(
        int(color_image.shape[1]), int(color_image.shape[0]), fx, fy, cx, cy
    )
    return o3d.geometry.PointCloud.create_from_rgbd_image(rgbd, camera)
