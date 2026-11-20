# Jenkins Pipeline for Delivery Metrics Exporter

Automated CI/CD pipeline lab experiment for a Python metrics exporter application.

## Project Structure
- `exporter.py`: Python metrics exporter exposing Prometheus metrics (`total`, `success`, `failed`, `active_drivers`).
- `test_exporter.py`: Automated unit tests (compatible with `pytest` and `unittest`).
- `requirements.txt`: Python package dependencies.
- `Jenkinsfile`: Declarative 4-stage Jenkins pipeline.
- `.gitignore`: Files and directories excluded from Git tracking.

## Local Test Execution
```bash
python -m unittest test_exporter.py
```
