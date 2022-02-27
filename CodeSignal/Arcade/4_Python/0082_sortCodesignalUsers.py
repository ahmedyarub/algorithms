def solution(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))


def CodeSignalUser(*user):
    return User(*user)


from functools import total_ordering


@total_ordering
class User(object):
    def __init__(self, name, user_id, xp):
        self.name = name
        self.user_id = int(user_id)
        self.xp = int(xp)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if self.xp == other.xp:
            return self.user_id > other.user_id
        else:
            return self.xp < other.xp

    def __eq__(self, other):
        return self.xp == other.xp and self.user_id == other.user_id
