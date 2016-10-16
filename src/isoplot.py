
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

import sys
from PyQt4 import QtCore, QtGui
from isoplot_gui import Ui_MainWindow


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


class Isoplot_App(QtGui.QMainWindow):

    def __init__(self, parent=None):
	QtGui.QWidget.__init__(self, parent)
	self.ui = Ui_MainWindow()
        self.config_path = os.path.abspath("./config.pkl")
        self.config = None
        self.load_map = None
        self.plot_map = None
        
	self.ui.setupUi(self)
	# here we connect signals with our slots
	#QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"), self.file_dialog)
        self.load_config(self.config_path)
        self.import_loadmods()
        self.import_plotmods()

        self.update_file_menu()

    def load_config(self, path):
        print("\n\n#\n# CONFIG\n#" + "-"*70)
        # If config file doesn't exist yet, create default
        if not os.path.isfile(path):
            print("Creating default config file at %s" % path)
            config = create_new_config()
            config['plotmod_paths'].append( os.path.abspath("./default_plotmod.py") )
            config['loadmod_paths'].append( os.path.abspath("./default_loadmod.py") )
            save_config(config, path)

        # Load config file
        print("Loading config file at %s" % path)
        config = load_config(path)
        print config
        self.config = config

    def import_loadmods(self):
        print("\n\n#\n# LOAD\n#" + "-"*70)
        # Load data load modules
        mod_dict = {}
        for mod_path in self.config['loadmod_paths']:
            (mod_name, mod) = load_module(mod_path)
            mod_dict[mod_name] = mod

        # Make dict that maps (mod_name, f_name) --> function handle
        load_map = {}
        for mod_name in mod_dict.keys():
            f_dict = get_functions(mod)
    
            for f_name in f_dict.keys():
                load_map[(mod_name, f_name)] = f_dict[f_name]
            print load_map
        self.load_map = load_map

    def update_file_menu(self):
        print("\n\n#\n# UPDATE\n#" + "-"*70)
        self.ui.menuFile.clear()

        #mod_names = list( set([mod_name for (mod_name, mod) in self.load_map.keys()]))

        mod_names = []
        for (mod_name, fcn_name) in self.load_map.keys():
            if mod_name not in mod_names:
                print("Adding %s" % mod_name)
                mod_menu = self.ui.menuFile.addMenu(mod_name)
                mod_names.append(mod_name)

            self.ui.menuFile.addMenu( mod_menu)
            action = mod_menu.addAction(fcn_name)
            fcn_handle = self.load_map[(mod_name, fcn_name)]

            QtCore.QObject.connect(action,QtCore.SIGNAL("triggered()"), fcn_handle)

        self.ui.menuFile.addSeparator()
        quit_action = self.ui.menuFile.addAction('Quit')
        QtCore.QObject.connect(quit_action,QtCore.SIGNAL("triggered()"), self.quit)

    def import_plotmods(self):
        pass

    def run_loadfun(self):
        pass

    def run_plotfun(self, mod_name, fcn_name):
        pass

    def quit(self):
        print("Quit!")


def Test():
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


if __name__=="__main__":
    # Start GUI
    app = QtGui.QApplication(sys.argv)
    myapp = Isoplot_App()
    myapp.show()
    sys.exit(app.exec_())
