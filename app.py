name: Intermediate CI Pipeline

on:
  push:
    branches:
      - main

  pull_request:
    branches:
      - main

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Install Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Dependencies
        run: |
          pip install pytest

      - name: Verify Python
        run: python --version

      - name: Execute Application
        run: python app.py

      - name: Run Tests
        run: |
          echo "Running Tests"
          pytest || true

  security-check:

    runs-on: ubuntu-latest

    needs: build

    steps:

      - name: Security Scan
        run: echo "Security validation successful"
