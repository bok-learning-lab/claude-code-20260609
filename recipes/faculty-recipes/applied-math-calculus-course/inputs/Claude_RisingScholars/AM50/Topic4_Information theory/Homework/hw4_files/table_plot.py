from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# This Python program contains two routines for plotting the digram
# frequencies. For the purposes of the homework, you can treat is as a black
# box and you should not need to make any modifications.
#
# The first routine, table_plot, can make a 2D plot of digram frequencies. It
# makes use of a logarithmic scale to better highlight small probabilities. The
# second routine, table_plot_differene, can plot the difference between two
# sets of digram frequencies. It uses a nonlinear scaling to better highlight
# small differences.

# Converts an integer back into a character
def num_inv(i):
    i=int(i+0.5)
    if(i==0):
        return "_"
    else:
        return chr(i|96)

# Creates a two-dimensional plot of the frequencies
def table_plot(c):

    # Assemble a two-dimensional array of the data, and take the logarithm to
    # bring out more detail in the small probability values
    X = np.zeros((27,27))
    for j in range(27):
        for i in range(27):
            X[i,j]=log(c[i+27*j])

    # Format the message that shows when mouse hovers over the plot
    def format_coord(x,y):
        x=int(x+0.5)
        y=int(y+0.5)
        if x>=0 and x<27 and y>=0 and y<27:
            return 'Digram="%s%s" Freq=%1.4f%%'% \
                   (num_inv(y),num_inv(x),100*exp(X[y,x]))
        else:
            return ''

    # Format the axis ticks to display letters
    fig,ax=plt.subplots()
    tick_labels=[num_inv(i) for i in range(27)]
    ax.set_xticks(range(27))
    ax.set_yticks(range(27))
    ax.set_xlabel("Second character")
    ax.set_ylabel("First character")
    ax.set_xticklabels(tick_labels)
    ax.set_yticklabels(tick_labels)

    # Carry out the 2D plot and set the mouse hover message
    plt.imshow(X,cmap=cm.jet,vmin=log(1e-6),vmax=log(0.05),interpolation='nearest')
    ax.format_coord = format_coord
    
    # Add a color bar to the plot, taking into account the logarithmic scaling
    cbar=plt.colorbar()
    cbar_ticks=[3e-6,1e-5,3e-5,1e-4,3e-4,1e-3,3e-3,1e-2,3e-2]
    cbar.set_ticks([log(k) for k in cbar_ticks])
    cbar.set_ticklabels(["%g%%"% (100.0*k) for k in cbar_ticks])
    
    # Show the plot
    plt.show()

# Nonlinear scaling to apply to the difference plot, to stretch out
# the small probablility region
def dscale(r):
    if(r<0):
	return -pow(-r,1/3.0)
    else:
	return pow(r,1/3.0)

# Inverse of the nonlinear scaling function
def dscale_inv(r):
    return pow(r,3.0)

# Creates a two-dimensional plot of the frequencies
def table_plot_difference(c,d):

    # Assemble a two-dimensional array of the data, and take the logarithm to
    # bring out more detail in the small probability values
    X = np.zeros((27,27))
    for j in range(27):
        for i in range(27):
	    X[i,j]=dscale(c[i+27*j]-d[i+27*j])

    # Format the message that shows when mouse hovers over the plot
    def format_coord2(x,y):
        x=int(x+0.5)
        y=int(y+0.5)
        if x>=0 and x<27 and y>=0 and y<27:
            return 'Digram="%s%s" Diff=%1.4f%%'% \
                   (num_inv(y),num_inv(x),100*dscale_inv(X[y,x]))
        else:
            return ''

    # Format the axis ticks to display letters
    fig,ax=plt.subplots()
    tick_labels=[num_inv(i) for i in range(27)]
    ax.set_xticks(range(27))
    ax.set_yticks(range(27))
    ax.set_xlabel("Second character")
    ax.set_ylabel("First character")
    ax.set_xticklabels(tick_labels)
    ax.set_yticklabels(tick_labels)

    # Carry out the 2D plot and set the mouse hover message
    plt.imshow(X,cmap=cm.RdBu,vmin=dscale(-0.021),vmax=dscale(0.021),interpolation='nearest')
    ax.format_coord = format_coord2

    # Add a color bar to the plot, taking into account the logarithmic scaling
    cbar=plt.colorbar()
    cbar_ticks=[-0.02,-0.01,-0.003,-0.0003,0,0.0003,0.003,0.01,0.02]
    print [dscale(k) for k in cbar_ticks]
    cbar.set_ticks([dscale(k) for k in cbar_ticks])
    cbar.set_ticklabels(["%g%%"% (100.0*k) for k in cbar_ticks])
    
    # Show the plot
    plt.show()
