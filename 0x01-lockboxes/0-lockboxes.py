#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    if len(boxes) == 0:
        return False
    keys = [0]
    keys.extend(list(set(boxes[0])))
    
    index = 1
    while index < len(keys):
        key = keys[index]
        for box in boxes[key]:
            if box not in keys and box < len(boxes) and box > 0:
                keys.append(box)
        index += 1
    
    if len(keys) == len(boxes):
        return True
    return False
