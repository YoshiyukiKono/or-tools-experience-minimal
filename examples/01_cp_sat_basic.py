from ortools.sat.python import cp_model


def solve() -> dict[str, int | str]:
    model = cp_model.CpModel()

    x = model.NewIntVar(0, 2, "x")
    y = model.NewIntVar(0, 2, "y")
    z = model.NewIntVar(0, 2, "z")

    model.Add(x != y)
    model.Maximize(x + 2 * y + 3 * z)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    return {
        "status": solver.StatusName(status),
        "x": solver.Value(x),
        "y": solver.Value(y),
        "z": solver.Value(z),
        "objective": int(solver.ObjectiveValue()),
    }


if __name__ == "__main__":
    print(solve())
