"""
Centralized logging configuration for the Agentic QA Engineer project.

Purpose
-------
This module provides a single place to configure logging for the
entire application.

Why do we need this?
--------------------
Instead of using print() statements throughout the codebase, every
module should use a logger. Logging provides:

- Log levels (INFO, DEBUG, WARNING, ERROR, CRITICAL)
- Timestamps
- Consistent formatting
- File logging
- Console logging
- Easier debugging
- Production readiness

Design Decision
---------------
We expose a `get_logger()` function instead of a global logger object.

Reason:
Each module should have its own logger name.

Example:

    logger = get_logger(__name__)

This makes log messages much easier to trace.

Trade-offs
----------
Pros
- Standard Python logging
- Zero external dependencies
- Easy migration to Structlog later
- Familiar to most Python developers

Cons
- More verbose than Loguru
- Manual configuration required

Future Improvements
-------------------
- JSON logging
- Structlog
- Correlation IDs
- Request IDs
- Cloud logging integration
"""

from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler


# --------------------------------------------------------------------------
# Project Paths
# --------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

LOG_DIRECTORY = PROJECT_ROOT / "logs"
LOG_DIRECTORY.mkdir(exist_ok=True)

LOG_FILE = LOG_DIRECTORY / "application.log"


# --------------------------------------------------------------------------
# Logger Factory
# --------------------------------------------------------------------------

def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Parameters
    ----------
    name : str
        Usually __name__ from the calling module.

    Returns
    -------
    logging.Logger
        Configured logger instance.

    Notes
    -----
    The logger is configured only once.
    Subsequent calls return the already configured logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ------------------------------------------------------------------
    # Console Handler
    # ------------------------------------------------------------------

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # ------------------------------------------------------------------
    # Rotating File Handler
    # ------------------------------------------------------------------

    file_handler = RotatingFileHandler(
        filename=LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    # ------------------------------------------------------------------
    # Register Handlers
    # ------------------------------------------------------------------

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger