import os
import ast
from radon.complexity import cc_visit
from radon.metrics import mi_visit, h_visit
from radon.raw import analyze

class ComplexityAnalyzer:
    def __init__(self, project_path):
        self.project_path = project_path
        self.report = []

    def analyze(self):
        for root, _, files in os.walk(self.project_path):
            for file in files:
                if file.endswith('.py'):
                    self._analyze_file(os.path.join(root, file))
        return self.report

    def _analyze_file(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            tree = ast.parse(content, filename=file_path)

            # Radon Metrics
            raw_metrics = analyze(content)
            complexity_metrics = cc_visit(tree)
            maintainability_metrics = mi_visit(tree)
            halstead_metrics = h_visit(tree)

            self.report.append({
                'file': file_path,
                'lines': len(lines),
                'complexity': complexity_metrics,
                'maintainability': maintainability_metrics,
                'halstead': halstead_metrics,
                'raw': raw_metrics
            })

    def generate_report(self):
        for file_report in self.report:
            print(f"File: {file_report['file']}")
            print(f"Lines: {file_report['lines']}")
            print("Complexity Metrics:")
            for item in file_report['complexity']:
                print(f"  {item}")
            print("Maintainability Index:")
            for item in file_report['maintainability']:
                print(f"  {item}")
            print("Halstead Metrics:")
            for item in file_report['halstead']:
                print(f"  {item}")
            print("Raw Metrics:")
            print(f"  {file_report['raw']}")
            print("-" * 80)

if __name__ == "__main__":
    project_path = 'path/to/your/project'
    analyzer = ComplexityAnalyzer(project_path)
    analyzer.analyze()
    analyzer.generate_report()
