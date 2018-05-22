from misc import *

# ****************************************************************************
title = "Python Interpreter Info (sys) :"

info_dict = {
    "Current Platform": sys.platform,
    "Implementation": sys.implementation.name,
    "Implementation Ver": sys.implementation.version,
    "Python Lang Ver": sys.version_info,
    "Python Lang Ver (Hex)": f"{sys.hexversion:#x}",
    "Ver (Startup)": sys.version,
    "Native Byte Order": sys.byteorder,
    "Python C API Ver": sys.api_version,
    "Python Executable": sys.executable,
    "Python Exec_prefix": sys.exec_prefix,
    "Thread Switch Interval": sys.getswitchinterval(),
    "Default String Encoding": sys.getdefaultencoding(),
    "Filesystem Encoding": sys.getfilesystemencoding(),
    "Max Unicode Code Point": f"{sys.maxunicode:#x}",
    "Max Stack Depth": sys.getrecursionlimit(),
    "Sys Modlue Obj Size": str(sys.getsizeof(sys)) + " Bytes",
    "Is Shutting Down?": sys.is_finalizing(),
}

info_list = {
    "Meta Path": sys.meta_path,
    "Search Path": sys.path,
    "Built-in Modules": sys.builtin_module_names,
    "Loaded Modules": sys.modules,
    "Command Line Flags": struct_sequence_to_list("sys.flags"),
    "Float Type Info": struct_sequence_to_list("sys.float_info"),
    "Numeric Hash Info": struct_sequence_to_list("sys.hash_info"),
    "Integer Type Info": struct_sequence_to_list("sys.int_info"),
    "Thread Info": struct_sequence_to_list("sys.thread_info"),
}


def main():
    print_separator()
    print(title + "\n")

    print_dict(info_dict, 25)

    print()
    for k, v in info_list.items():
        print_list(v, k, 25)

    print()
    print_separator()
    print("Interpreter Copyright:" + "\n")
    print(sys.copyright)


# ****************************************************************************
if __name__ == "__main__":
    main()
