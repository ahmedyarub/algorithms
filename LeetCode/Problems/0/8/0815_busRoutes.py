import collections


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        to_routes = collections.defaultdict(set)
        for route_index, route in enumerate(routes):
            for stop in route:
                to_routes[stop].add(route_index)

        bfs = [(source, 0)]

        seen = {source}
        while len(bfs) > 0:
            stop, bus = bfs.pop(0)

            if stop == target:
                return bus

            for route_index in to_routes[stop]:
                for stop in routes[route_index]:
                    if stop not in seen:
                        bfs.append((stop, bus + 1))
                        seen.add(stop)

                routes[route_index] = []

        return -1
