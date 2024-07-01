# CodeComplexityAnalyzer

CodeComplexityAnalyzer is a Python tool that analyzes and reports on the complexity of Python code files in a project. It calculates various metrics such as cyclomatic complexity, lines of code (LOC), maintainability index, and more.

## Features

- **Cyclomatic Complexity**: Calculates the cyclomatic complexity of the code.
- **Lines of Code**: Counts the number of lines in the code.
- **Maintainability Index**: Measures the maintainability of the code.
- **Halstead Metrics**: Calculates Halstead metrics for the code.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/wasserpuncher/CodeComplexityAnalyzer.git
    cd CodeComplexityAnalyzer
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the complexity analyzer:
    ```bash
    python complexity_analyzer.py
    ```

2. The script will print the complexity report to the console.

## License

This project is licensed under the MIT License.
