#--------------------------------------------------------------------------------
# isoplot: default_load_data.py
#
# Description: A set of functions for default data loading behavior.
#--------------------------------------------------------------------------------

import os
import csv
from PyQt4 import QtCore, QtGui

def load_data_file(path=None):
    if path is None:
        path = str( QtGui.QFileDialog.getOpenFileName(None,
                                                      "Open Data File", "",
                                                      "CSV data files (*.csv)") )

    base_name = os.path.basename(path)
    (mod_name, ext) = base_name.split('.')

    if ext == "csv":
        data = load_data_from_csv(path)
    else:
        print("Error: File type %s not supported." % ext)

    return (base_name, data)

#--------------------------------------------------------------------------------

# Will create a dict with column header --> list of strings
def load_data_from_csv(path=None, floatify=True):
    if path is None:
        path = str( QtGui.QFileDialog.getOpenFileName(None,
                                                      "Open Data File", "",
                                                      "CSV data files (*.csv)") )
    base_name = os.path.basename(path)
        
    reader = csv.DictReader(open(path))

    result = {}
    for row in reader:
        for column, value in row.iteritems():
            column = column.strip()
            value = value.strip()
            
            result.setdefault(column, []).append(value)

            
    def floatify_dict(d):
        for key in d.keys():
            for i,val in enumerate(d[key]):
                try:
                    new_val = float(val)
                except:
                    new_val = val
                    
                d[key][i] = new_val
        return d
            
    if floatify is True:
        result = floatify_dict(result)
        
    return (base_name, result)


