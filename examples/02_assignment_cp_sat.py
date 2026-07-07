from ortools.sat.python import cp_model


def solve() -> dict:
    # cost[worker][task]
    costs = [
        [90, 76, 75, 70],
        [35, 85, 55, 65],
        [125, 95, 90, 105],
        [45, 110, 95, 115],
    ]
    n_workers = len(costs)
    n_tasks = len(costs[0])

    model = cp_model.CpModel()
    assign = {}
    for w in range(n_workers):
        for t in range(n_tasks):
            assign[w, t] = model.NewBoolVar(f"worker_{w}_task_{t}")

    # Each worker does exactly one task.
    for w in range(n_workers):
        model.AddExactlyOne(assign[w, t] for t in range(n_tasks))

    # Each task is done by exactly one worker.
    for t in range(n_tasks):
        model.AddExactlyOne(assign[w, t] for w in range(n_workers))

    model.Minimize(sum(costs[w][t] * assign[w, t] for w in range(n_workers) for t in range(n_tasks)))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    result = []
    for w in range(n_workers):
        for t in range(n_tasks):
            if solver.BooleanValue(assign[w, t]):
                result.append({"worker": w, "task": t, "cost": costs[w][t]})

    return {"status": solver.StatusName(status), "total_cost": int(solver.ObjectiveValue()), "assignments": result}


if __name__ == "__main__":
    print(solve())
