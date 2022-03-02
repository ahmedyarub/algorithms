class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):

        # Turn this problem into the Eulerian Path Checker rather than the NP-Complete Hamiltonian Path problem
        #
        #   How? Use the letters of the alphabet as the nodes instead of the names. The names will become the edges.
        #     Now we just check if we can connect all the edges without using any twice!
        #     We just turned it into the Eulerian path problem. This will become very important.
        #
        #   Generally, a graph will have an Eulerian path IF it has a maximum of 2 nodes that have an odd degree (Number of edges/teammates coming in and out)
        #     Why? We can use a odd-degree node as a starting or ending point.
        #     That forces us to use those two vertices/letters as the corresponding point in the team announcement.
        #   The rest of the nodes MUST have an equal number of in-degree and out-degree (We must somehow connect them all)
        #
        #   The check will be something like this:
        #     - Have two directories:
        #       - One for the names coming in (FROM)
        #       - The other for names going out (TO)
        #     - Go through every letter of the alphabet
        #     - Find all names that can go to current letter/vertice, save it to FROM
        #       - Ex: K -> Mark
        #     - Find all names that the letter can go to, save it to TO
        #       - Ex: M -> Mark
        #
        #     - Go through every letters again, count the number of nodes with unequal in-out degrees.
        #       - If there is 1 less in-degree (One less teammate to come from)
        #         - THIS IS OUR GUARANTEED STARTING NAME!
        #         - If we have more than one starting name, then it is impossible, return False.
        #
        #       - If there is 1 more in-degree (One more teammate to come from)
        #         - THIS IS OUR GUARANTEED ENDING NAME!
        #         - If we have more than one ending name, then it is impossible, return False.
        #
        #   We are almost done!
        #
        #   Doing this check can already pass most of the tests, the last thing we need to check is if the entire graph is connected.
        #     We can do this with a simple BFS:
        #       - Start from any teammate
        #       - Find all unvisited teammate who can lead to current teammate or vice-versa
        #           Ex: Mark <- [ Kurt ] -> Terk
        #       - Repeat until we can't find any more teammates
        #       - Then check if the entire team is visited.

        self.names = [i.lower() for i in self.names]

        letters = "abcdefghijklmnopqrstuvwxyz"
        FROM = {i: [] for i in letters}
        TO = {i: [] for i in letters}

        for i in letters:
            for j in self.names:
                if i == j[-1]:
                    FROM[i].append(j)  # Find names that lead to current letter
                if i == j[0]:
                    TO[i].append(j)  # Find names that letter can lead to

        # Debugging and visualizing the graph
        for i in letters:
            print("____________________")
            print("Node: %s" % i)
            print("From: ", FROM[i])
            print("To: ", TO[i])

        start = False
        end = False
        for i in letters:
            if len(FROM[i]) + 1 == len(TO[i]):
                # Found the start!
                if start:
                    return False  # Whoops, too many starts!
                start = True
            elif len(FROM[i]) == len(TO[i]) + 1:
                # Found the end!
                if end:
                    return False  # Whoops, too many ends!
                end = True
            elif len(FROM[i]) != len(TO[i]):
                return False

        # Check if graph is connected
        visited = {0}
        queue = [0]

        while queue:

            name = queue.pop(0)
            for ind, teammate in enumerate(self.names):
                if ind in visited:
                    continue
                if self.names[name][0] == teammate[-1]:
                    visited.add(ind)
                    queue.append(ind)
                elif self.names[name][-1] == teammate[0]:
                    visited.add(ind)
                    queue.append(ind)

        return len(visited) == len(self.names)  # Is everyone found?


def solution(team):
    return bool(Team(team))
