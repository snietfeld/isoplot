
#--------------------------------------------------------------------------------
# isoplot: default_plots.py
#
# Description: A set of default plot functions for basic analysis. Also serves
#              as an example for users to create their own plotting modules.
#--------------------------------------------------------------------------------

import matplotlib.pyplot as plt

class Derp:
    def __init__(self):
        print("Init!")

def scatter(fname, data):
    print("Scatter!")
    print(fname)
    print(data)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data['time_s'], data['pos_x'])
    ax.set_title(fname)
    ax.grid(True)
    fig.show()
    

def line(fname, datadict):
    print("Line!")
