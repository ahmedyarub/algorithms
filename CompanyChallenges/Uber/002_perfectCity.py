def calc_axis(axis_depr, axis_dest):
    if int(axis_depr) != int(axis_dest):
        return abs(axis_depr - axis_dest)
    else:
        departure_offset = axis_depr % 1
        destination_offset = axis_dest % 1
        if (departure_offset + destination_offset) < 1:
            return departure_offset + destination_offset
        else:
            return 2 - departure_offset - destination_offset


def solution(departure, destination):
    return calc_axis(departure[0], destination[0]) + calc_axis(departure[1], destination[1])
