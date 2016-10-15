
#--------------------------------------------------------------------------------
# isoplot - A lightweight data plotting and analysis application
#
# Author: Scott Nietfeld
# Initial Commit: 2016-10-12
#
# Compiling the GUI:  pyuic4 isoplot_gui.ui -o isoplot_gui.py
#--------------------------------------------------------------------------------

import os



def load_module(path):
    import imp
    
    print("Loading module from %s" % path)
    full_path = os.path.abspath(path)
    base_name = os.path.basename(full_path)
    mod_name= base_name.split('.')[0]

    print("Full path: %s" % full_path)
    print("Base name: %s" % base_name)
    print("Module name: %s" % mod_name)
    
    mod = imp.load_source(base_name, full_path)
    return mod

def get_functions(mod):
    import inspect

    all_functions = inspect.getmembers(mod, inspect.isfunction)
    return all_functions

def unload_module(path):
    pass

def load_data_file(path):
    pass

def run_usr_function(path):
    pass


if __name__=="__main__":
    print("Hello.")

    mod = load_module("./default_plots.py")
    f_list = get_functions(mod)
    
    print f_list
    
