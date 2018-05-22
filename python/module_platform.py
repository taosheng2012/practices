from misc import *

# ****************************************************************************
title = "Platform Info (platform):"

info_dict = {
    "System Name": platform.system(),
    "System Release": platform.release(),
    "System Version": platform.version(),
    "General Info": platform.platform(),
    "Bit Architeture": platform.architecture()[0],
    "Linkage Format": platform.architecture()[1],
    "Machine Type": platform.machine(),
    "Computer Network Name": platform.node(),
    "Processor Name": platform.processor(),
    "Python Implementation": platform.python_implementation(),
    "Python Build No.": platform.python_build()[0],
    "Python Build Date": platform.python_build()[1],
    "Python Compiler": platform.python_compiler(),
    "Python SCM Branch": platform.python_branch(),
}

# info_list = {
# }


def main():
    print_separator()
    print(title + "\n")

    print_dict(info_dict, 25)

    # print()
    # for k, v in info_list.items():
    #     print_list(v, k, 25)

# ****************************************************************************
if __name__ == "__main__":
    main()
