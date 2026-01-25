"""
ap-copy-lights: Copy and organize astrophotography files based on FITS header metadata.
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ap-copy-lights")
except PackageNotFoundError:
    __version__ = "0.1.0"
