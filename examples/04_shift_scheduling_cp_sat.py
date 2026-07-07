from ortools.sat.python import cp_model


def solve() -> dict:
    nurses = ["A", "B", "C"]
    days = ["Mon", "Tue", "Wed", "Thu"]
    shifts = ["day", "night"]

    model = cp_model.CpModel()
    work = {}
    for n in nurses:
        for d in days:
            for s in shifts:
                work[n, d, s] = model.NewBoolVar(f"{n}_{d}_{s}")

    # Every shift must have exactly one nurse.
    for d in days:
        for s in shifts:
            model.AddExactlyOne(work[n, d, s] for n in nurses)

    # A nurse cannot work both day and night on the same day.
    for n in nurses:
        for d in days:
            model.AddAtMostOne(work[n, d, s] for s in shifts)

    # Fairness: each nurse works at least 2 shifts and at most 3 shifts.
    for n in nurses:
        total = sum(work[n, d, s] for d in days for s in shifts)
        model.Add(total >= 2)
        model.Add(total <= 3)

    # Small preference: A should avoid night shifts if possible.
    model.Minimize(sum(work["A", d, "night"] for d in days))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    schedule = []
    for d in days:
        for s in shifts:
            assigned = [n for n in nurses if solver.BooleanValue(work[n, d, s])][0]
            schedule.append({"day": d, "shift": s, "nurse": assigned})

    return {"status": solver.StatusName(status), "schedule": schedule}


if __name__ == "__main__":
    print(solve())
