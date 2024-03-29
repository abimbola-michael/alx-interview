#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    if len(boxes) == 0:
        return False
    keys = [0]
    index = 0
    while index < len(keys):
        key = keys[index]
        for box in boxes[key]:
            if box < len(boxes) and box > 0 and box not in keys:
                keys.append(box)
        index += 1

    if len(keys) == len(boxes):
        return True
    return False
