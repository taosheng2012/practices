import sys
import os
import platform
import atexit


def print_separator():
    line = "*" * 80
    print(line)


def struct_sequence_to_list(struct_sequence):
    if type(struct_sequence) is not str:
        raise TypeError("Need a str obj")

    info_list = []
    obj = eval(struct_sequence)

    for i in dir(obj):
        if not i.startswith("_"):
            t = struct_sequence + "." + i
            info_list.append((i + " ").ljust(24, "-") + " " + str(eval(t)))
    return info_list


def print_dict(info, num_ljust):
    for k, v in info.items():
        print((k + " ").ljust(num_ljust, "-") + " " + str(v))


def print_list(info, title, num_ljust):
    line_part_0 = "".ljust(num_ljust)
    info = list(map(str, info))

    item_width = max(map(len, info))
    item_width += 2

    col = (100 - num_ljust) // item_width

    if col <= 1:
        print((title + " ").ljust(num_ljust, "-") + " " + info[0])
        for i in info[1:]:
            print(line_part_0 + " " + i)
        return
    else:
        t = len(info)
        row = t // col if t % col == 0 else t // col + 1

        lines = [[] for i in range(row)]

        lines[0].append((title + " ").ljust(num_ljust, "-") + " ")
        for i in range(1, row):
            lines[i].append(line_part_0 + " ")

        try:
            for m in range(col):
                for i in range(row):
                    t = info[i + m * row].ljust(item_width)
                    lines[i].append(t)
        except IndexError:
            pass
            # print(e)

        for line in lines:
            for line_part in line:
                print(line_part, end="")
            print()
