#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import urllib.request
from pathlib import Path


def _ensure_model_present():
    """If the model file is missing, try downloading it from MODEL_REMOTE_URL.

    Set the environment variable `MODEL_REMOTE_URL` to a URL where the
    `xgb_model.joblib` can be downloaded (for example an S3 presigned URL).
    This function will only attempt to download when the model file does not
    already exist.
    """
    try:
        base = Path(__file__).resolve().parents[1]
        model_path = base / 'ML_project' / 'models' / 'xgb_model.joblib'
        if model_path.exists():
            return
        url = os.environ.get('MODEL_REMOTE_URL')
        if not url:
            return
        model_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Downloading model from {url} to {model_path}...")
        urllib.request.urlretrieve(url, model_path)
        print("Model downloaded.")
    except Exception as e:
        # Don't prevent the server from starting if the download fails;
        # just log the error so deployment can proceed and the model can
        # be provided by other means.
        print(f"Model download failed: {e}")


def main():
    """Run administrative tasks."""
    # attempt to fetch model if a remote URL is provided
    _ensure_model_present()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tip_prediction.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
