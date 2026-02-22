"""Launcher backends for spinning up SGLang diffusion workers.

Right now only local subprocesses are supported. The backend interface
is meant to be extended for other deployment strategies (Kubernetes,
Ray, etc.) down the road.
"""

from sglang_diffusion_routing.launcher.backend import (
    LaunchedWorker,
    LauncherBackend,
    WorkerLaunchResult,
)
from sglang_diffusion_routing.launcher.config import create_backend, load_launcher_config
from sglang_diffusion_routing.launcher.local import LocalLauncher, LocalLauncherConfig

__all__ = [
    "LaunchedWorker",
    "LauncherBackend",
    "LocalLauncher",
    "LocalLauncherConfig",
    "WorkerLaunchResult",
    "create_backend",
    "load_launcher_config",
]
