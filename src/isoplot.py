
#--------------------------------------------------------------------------------
# isoplot - A lightweight data plotting and analysis application
#
# Author: Scott Nietfeld
# Initial Commit: 2016-10-12
#
# Compiling the GUI:  pyuic4 isoplot_gui.ui -o isoplot_gui.py
#
# Config File: On running the first time, a default config file will be created
#     for storing persistent app information, including:
#         mod_paths - A dictionary of full paths to plotting modules
#         default_data_dir - A default path for opening data files
#
#--------------------------------------------------------------------------------

import os
import pickle

config_path = "./config.pkl"

def create_new_config():
    config = {'mod_paths': [],
              'default_data_dir': os.path.abspath('./')}
    return config

def save_config(config, path):
    with open(os.path.abspath(path), 'wb') as handle:
        pickle.dump(config, handle)

def load_config(path):
    with open(os.path.abspath(path), 'rb') as handle:
        config = pickle.load(handle)
    return config

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
    return (mod_name, mod)

def get_functions(mod):
    import inspect

    all_functions = inspect.getmembers(mod, inspect.isfunction)

    f_dict = {}
    for (fname, f) in all_functions:
        f_dict[fname] = f
    
    return f_dict

def unload_module(path):
    pass

def load_data_file(path):
    pass

def run_usr_function(f_name):
    pass


if __name__=="__main__":
    print("Hello.")

    # If config file doesn't exist yet, create default
    if not os.path.isfile(config_path):
        print("Creating default config file at %s" % config_path)
        config = create_new_config()
        config['mod_paths'].append( os.path.abspath("./default_plots.py") )
        save_config(config, config_path)

    # Load config file
    print("Loading config file at %s" % config_path)
    config = load_config(config_path)

    # Load plotting modules
    for mod_path in config['mod_paths']:
        (mod_name, mod) = load_module(mod_path)
        f_dict = get_functions(mod)
        print f_dict.keys()

    print f_dict
    f_dict['scatter'](None, None)
    f_dict['line'](None, None)
    
