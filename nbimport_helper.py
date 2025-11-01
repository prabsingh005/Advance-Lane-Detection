import sys, os, nbimporter

def setup_notebook_imports(path):
    if path not in sys.path:
        sys.path.append(path)
    print(f"Notebook import path added: {path}")

def nbimport(name):
    return nbimporter.NotebookLoader().load_module(name)
