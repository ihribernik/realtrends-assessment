"""
"""
from pathlib import Path
from realTrendsAssessment.settings.base import *  # NOQA


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = False

ALLOWED_HOSTS = ["*"]
