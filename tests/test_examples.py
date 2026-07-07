import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"


def load_example(filename: str):
    path = EXAMPLES / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_cp_sat_basic():
    result = load_example("01_cp_sat_basic.py").solve()
    assert result["status"] in {"OPTIMAL", "FEASIBLE"}
    assert result["x"] != result["y"]


def test_assignment():
    result = load_example("02_assignment_cp_sat.py").solve()
    assert result["status"] == "OPTIMAL"
    assert len(result["assignments"]) == 4


def test_knapsack():
    result = load_example("03_knapsack_cp_sat.py").solve()
    assert result["status"] == "OPTIMAL"
    assert result["total_weight"] <= result["capacity"]


def test_shift_scheduling():
    result = load_example("04_shift_scheduling_cp_sat.py").solve()
    assert result["status"] in {"OPTIMAL", "FEASIBLE"}
    assert len(result["schedule"]) == 8


def test_tsp():
    result = load_example("05_tsp_routing.py").solve()
    assert result["status"] == "OK"
    assert result["route"][0] == 0
    assert result["route"][-1] == 0
