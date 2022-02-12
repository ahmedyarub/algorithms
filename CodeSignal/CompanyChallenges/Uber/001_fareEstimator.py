def solution(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    return list(
        map(
            lambda t: round(t[0] * ride_time + t[1] * ride_distance, 2),
            zip(cost_per_minute, cost_per_mile)
        )
    )
