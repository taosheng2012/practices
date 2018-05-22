from misc import *

# ************************************************************
def exit_handler():
    print()
    if hasattr(sys, "last_traceback"):
        print("=== ERROR ===")
    else:
        print("=== SUCCESS ===")

atexit.register(exit_handler)




