"""Puts tests/ on the import path so tests in `tests/<state>/` can use `seedutil`."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
