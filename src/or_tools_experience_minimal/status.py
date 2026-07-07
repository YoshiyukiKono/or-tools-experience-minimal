from ortools.sat.python import cp_model


def cp_sat_status_name(status: int) -> str:
    """Return a readable CP-SAT status name."""
    return cp_model.CpSolver().StatusName(status)
