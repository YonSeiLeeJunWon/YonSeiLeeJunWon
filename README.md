<img src="score.png">

# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
    - name: Run Update Python Script 
      run: |
        python utils/count_files.py
    - name: Run Update README.md File
      run: |
        git add .
        git diff
        git config --local user.email "chaerin.dev@gmail.com"
        git config --local user.name "chaerin-dev"
        git commit -m "Automatically Update README.md file"
        git push
