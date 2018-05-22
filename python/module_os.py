from misc import *

# ****************************************************************************
title = "OS Info (os):"

info_dict = {
    "User Name": os.getlogin(),
    "Current Working Dir": os.getcwd(),
    "Current Process ID": os.getpid(),
    "Parent Process ID": os.getppid(),
    "STDIN isatty": os.isatty(0),
    "STDOUT isatty": os.isatty(1),
    "STDERR isatty": os.isatty(2),
}


environ = os.environ.copy()
del environ["PATH"]

err_msg = []
for i in range(30):
    err_msg.append((str(i) + " ").ljust(8, "-") + " " + os.strerror(i))

info_list = {
    "Environ Var PATH": os.environ["PATH"].split(os.pathsep),
    "Error Message List": err_msg,
}


def main():
    print_separator()
    print(title + "\n")

    print_dict(info_dict, 25)

    print("\nEnvironment Varibles:")
    print_dict(environ, 25)

    print()
    for k, v in info_list.items():
        print_list(v, k, 25)

# ****************************************************************************
if __name__ == "__main__":
    main()
