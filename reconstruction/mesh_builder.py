from __future__ import annotations
import numpy as np

try:
    import open3d as o3d
except ImportError:
    o3d = None


def build_mesh(depth_image, color_image, intrinsics, depth_scale=0.001):
    """Build a bounded surface mesh from one RGB-D frame."""
    if o3d is None:
        raise RuntimeError("open3d is not installed")
    from .pointcloud_builder import build_pointcloud
    pcd = build_pointcloud(depth_image, color_image, intrinsics, depth_scale)
    if len(pcd.points) == 0:
        return o3d.geometry.TriangleMesh()
    pcd = pcd.voxel_down_sample(0.01)
    pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
    mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        pcd, depth=7
    )
    mesh.compute_vertex_normals()
    return mesh
