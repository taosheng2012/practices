from misc import *

# ******************************************************************************
path_code = os.path.dirname(os.path.abspath(__file__))
path_root = os.path.abspath(os.path.join(path_code, os.pardir))
path_data = os.path.join(path_root, "data")

os.chdir(path_code)

# ******************************************************************************
title = "APP Path Info"

info_dict = {
    "APP Path (root)": path_root,
    "APP Path (code)": path_code,
    "APP Path (data)": path_data,
    "Current Working Dir(cwd)": path_code,
}


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
