def distanceToOrigin(x2, y2):
    return pow(pow(x2, 2) + pow(y2, 2), 0.5)


def solution(address, objects, names):
    min_length = 255
    target = ''
    normalized_address = address.lower()

    for i in range(len(names)):
        normalized_name = names[i].lower()

        if len(normalized_address) - 1 > len(normalized_name):
            continue

        valid_name = True
        for j in range(len(normalized_address) - 1):
            if normalized_address[j] != normalized_name[j]:
                valid_name = len(normalized_address) < len(normalized_name) and (
                        normalized_name.find(normalized_address[(j + 1)::], j + 1) == j + 1 or
                        normalized_name.find(normalized_address[(j + 1)::], j) == j or
                        normalized_name.find(normalized_address[j::], j + 1) == j + 1)
                break

        if not valid_name:
            continue

        if len(objects[i]) == 2:
            dest_x, dest_y = objects[i][0], objects[i][1]
        elif objects[i][0] == objects[i][2]:
            if (objects[i][1] < 0 < objects[i][3]) or (objects[i][3] < 0 < objects[i][1]):
                dest_x, dest_y = objects[i][0], 0
            else:
                dest_x, dest_y = \
                    objects[i][0], objects[i][1] if abs(objects[i][1]) < abs(objects[i][3]) else objects[i][3]
        else:
            if (objects[i][0] < 0 < objects[i][2]) or (objects[i][0] < 0 < objects[i][2]):
                dest_x, dest_y = 0, objects[i][1]
            else:
                dest_x, dest_y = \
                    objects[i][0] if abs(objects[i][0]) < abs(objects[i][2]) else objects[i][2], objects[i][1]

        cur_length = distanceToOrigin(dest_x, dest_y)
        if cur_length < min_length:
            min_length = cur_length
            target = names[i]

    return target
