
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
    config = {'plotmod_paths': [],
              'loadmod_paths': [],
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
    mod_name = base_name.split('.')[0]

    print("Full path: %s" % full_path)
    print("Module name: %s" % mod_name)
    
    mod = imp.load_source(base_name, full_path)
    return (mod_name, mod)

def get_functions(mod):
    import inspect

    all_functions = inspect.getmembers(mod, inspect.isfunction)

    f_dict = {}
    for (f_name, f) in all_functions:
        f_dict[f_name] = f
    
    return f_dict

def unload_module(path):
    pass


def run_usr_function(mod_name, fcn_name):
    pass


if __name__=="__main__":
    print("Hello.")

    #
    # CONFIG
    #----------------------------------------------------------------------
    print("\n\n#\n# CONFIG\n#" + "-"*70)
    # If config file doesn't exist yet, create default
    if not os.path.isfile(config_path):
        print("Creating default config file at %s" % config_path)
        config = create_new_config()
        config['plotmod_paths'].append( os.path.abspath("./default_plotmod.py") )
        config['loadmod_paths'].append( os.path.abspath("./default_loadmod.py") )
        save_config(config, config_path)

    # Load config file
    print("Loading config file at %s" % config_path)
    config = load_config(config_path)
    print config

    
    #
    # LOAD
    #----------------------------------------------------------------------
    print("\n\n#\n# LOAD\n#" + "-"*70)
    # Load data load modules
    mod_dict = {}
    for mod_path in config['loadmod_paths']:
        (mod_name, mod) = load_module(mod_path)
        mod_dict[mod_name] = mod

    # Make dict that maps (mod_name, f_name) --> function handle
    load_map = {}
    for mod_name in mod_dict.keys():
        f_dict = get_functions(mod)

        for f_name in f_dict.keys():
            load_map[(mod_name, f_name)] = f_dict[f_name]
        print load_map.keys()

        
    #
    # PLOT
    #----------------------------------------------------------------------
    print("\n\n#\n# PLOT\n#" + "-"*70)
    # Load plotting modules
    mod_dict = {}
    for mod_path in config['plotmod_paths']:
        (mod_name, mod) = load_module(mod_path)
        mod_dict[mod_name] = mod

    # Make dict that maps (mod_name, f_name) --> function handle
    plot_map = {}
    for mod_name in mod_dict.keys():
        f_dict = get_functions(mod)

        for f_name in f_dict.keys():
            plot_map[(mod_name, f_name)] = f_dict[f_name]
        print plot_map.keys()


    
    #
    # RUN
    #----------------------------------------------------------------------
    data = load_map[('default_loadmod', 'load_data_file')]('./test.csv')
    print data
    
    print("\n\n#\n# RUN\n#" + "-"*70)
    plot_map[('default_plotmod','scatter')](None, None)
    plot_map[('default_plotmod','line')](None, None)


    
    
