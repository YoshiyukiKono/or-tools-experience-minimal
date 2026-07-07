from ortools.constraint_solver import pywrapcp, routing_enums_pb2


def solve() -> dict:
    # Symmetric distance matrix for 5 locations.
    distance_matrix = [
        [0, 7, 9, 8, 6],
        [7, 0, 10, 4, 3],
        [9, 10, 0, 5, 8],
        [8, 4, 5, 0, 6],
        [6, 3, 8, 6, 0],
    ]

    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index: int, to_index: int) -> int:
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_parameters)
    if solution is None:
        return {"status": "NO_SOLUTION"}

    index = routing.Start(0)
    route = []
    total_distance = 0
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    route.append(manager.IndexToNode(index))

    return {"status": "OK", "route": route, "total_distance": total_distance}


if __name__ == "__main__":
    print(solve())
