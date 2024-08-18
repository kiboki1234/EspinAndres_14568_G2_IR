# run_tests.py
import os
from behave.__main__ import main as behave_main

def run_tests():
    # El archivo de salida será cucumber_report.json en la raíz del proyecto
    behave_main(["-f", "json.pretty", "-o", "results.json", "features"])

if __name__ == '__main__':
    run_tests()
