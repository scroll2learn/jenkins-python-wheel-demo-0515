# Jenkins Python Wheel Demo

This project demonstrates a complete Jenkins CI/CD pipeline for a Python application.

Flow:

GitHub Push -> Jenkins Checkout -> Install Dependencies -> Test -> Build Wheel -> Deploy Wheel -> Run Installed Application

## Local Commands

Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install build and test tools:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Run tests:

```bash
python -m pytest -v
```

Build wheel:

```bash
python -m build
```

Install wheel:

```bash
python -m pip install dist/jenkins_python_demo-1.0.0-py3-none-any.whl
```

Run application:

```bash
jenkins-python-demo
```

Expected output:

```text
Application started successfully!
Welcome to Jenkins CI/CD Demo using Python Wheel
10 + 20 = 30
```
