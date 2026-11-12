
#!/usr/bin/env python
"""
Django Management Utility

This script provides command-line access to Django's administrative
management commands, including running the development server,
database migrations, creating superusers, and collecting static files.

Project: Django Web Application
Configuration: configuration.settings
"""

import os
import sys
import logging
import platform
from pathlib import Path
from datetime import datetime


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
PROJECT_NAME = "Django Management System"
DJANGO_SETTINGS_MODULE = "configuration.settings"
MINIMUM_PYTHON_VERSION = (3, 9)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    DJANGO_SETTINGS_MODULE
)


# ============================================================
# LOGGING CONFIGURATION
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)


# ============================================================
# ENVIRONMENT VALIDATION
# ============================================================

def validate_environment():
    """Validate Python version and project environment."""

    current_version = sys.version_info[:2]

    if current_version < MINIMUM_PYTHON_VERSION:
        raise RuntimeError(
            f"Python {MINIMUM_PYTHON_VERSION[0]}."
            f"{MINIMUM_PYTHON_VERSION[1]} or higher is required. "
            f"Current version: {platform.python_version()}"
        )

    if not BASE_DIR.exists():
        raise FileNotFoundError(
            f"Project directory not found: {BASE_DIR}"
        )

    logger.info("Environment validation completed successfully.")


# ============================================================
# DJANGO INITIALIZATION
# ============================================================

def initialize_django():
    """Initialize Django's command-line management system."""

    try:
        from django.core.management import (
            execute_from_command_line
        )

        logger.info("Django framework imported successfully.")

        return execute_from_command_line

    except ImportError as exc:
        logger.critical(
            "Django could not be imported. "
            "Check your installation and virtual environment."
        )

        raise ImportError(
            "Django is not installed or unavailable in the "
            "current Python environment. "
            "Try installing it using: pip install django"
        ) from exc


# ============================================================
# SYSTEM INFORMATION
# ============================================================

def display_system_information():
    """Display basic project and runtime information."""

    logger.info("=" * 55)
    logger.info("PROJECT: %s", PROJECT_NAME)
    logger.info("PYTHON VERSION: %s", platform.python_version())
    logger.info("OPERATING SYSTEM: %s", platform.system())
    logger.info("PROJECT DIRECTORY: %s", BASE_DIR)
    logger.info("SETTINGS MODULE: %s", DJANGO_SETTINGS_MODULE)
    logger.info("STARTUP TIME: %s", datetime.now())
    logger.info("=" * 55)


# ============================================================
# COMMAND EXECUTION
# ============================================================

def execute_management_command():
    """Execute the requested Django management command."""

    execute_from_command_line = initialize_django()

    try:
        logger.info("Executing Django management command...")

        execute_from_command_line(sys.argv)

        logger.info("Management command completed successfully.")

    except KeyboardInterrupt:
        logger.warning(
            "Process interrupted by user. Shutting down..."
        )
        sys.exit(130)

    except Exception as exc:
        logger.exception(
            "An unexpected error occurred: %s", exc
        )
        raise


# ============================================================
# APPLICATION ENTRY POINT
# ============================================================

def main():
    """Main entry point for Django administrative operations."""

    try:
        display_system_information()

        validate_environment()

        execute_management_command()

    except Exception as exc:
        logger.error("Application startup failed: %s", exc)
        sys.exit(1)


# ============================================================
# SCRIPT EXECUTION
# ============================================================

if __name__ == "__main__":

    logger.info("Starting Django Management Utility...")

    main()
