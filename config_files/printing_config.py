

logger_printing_button=1
debugger_printing_button=1
simpile_printing_button=1
def print_logger(*args, **kwargs):
    if logger_printing_button==1:
       print(args,kwargs)
    else:
        pass
def print_debugger(*args, **kwargs):
    if debugger_printing_button == 1:
        print(args, kwargs)
    else:
        pass

def print_simpile(*args, **kwargs):
    if simpile_printing_button == 1:
        print(args, kwargs)
    else:
        pass
