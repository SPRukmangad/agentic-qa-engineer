"""
Logging package.

Expose the public logger factory for the application.
"""

from .logger import get_logger

__all__ = ["get_logger"]