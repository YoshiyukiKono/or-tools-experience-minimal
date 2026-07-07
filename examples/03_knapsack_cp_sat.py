from ortools.sat.python import cp_model


def solve() -> dict:
    items = [
        {"name": "laptop", "weight": 3, "value": 40},
        {"name": "camera", "weight": 2, "value": 25},
        {"name": "jacket", "weight": 4, "value": 30},
        {"name": "book", "weight": 1, "value": 10},
        {"name": "headphones", "weight": 1, "value": 15},
    ]
    capacity = 6

    model = cp_model.CpModel()
    take = [model.NewBoolVar(item["name"]) for item in items]

    model.Add(sum(item["weight"] * take[i] for i, item in enumerate(items)) <= capacity)
    model.Maximize(sum(item["value"] * take[i] for i, item in enumerate(items)))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    selected = [items[i] for i in range(len(items)) if solver.BooleanValue(take[i])]
    return {
        "status": solver.StatusName(status),
        "capacity": capacity,
        "total_weight": sum(item["weight"] for item in selected),
        "total_value": int(solver.ObjectiveValue()),
        "selected": selected,
    }


if __name__ == "__main__":
    print(solve())
