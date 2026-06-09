#!/usr/bin/python
import re
import sys
from table_plot import *

# Two regular expressions that are used when scanning the text files
p=re.compile("[\-_\[\]`]")
p2=re.compile("[^a-zA-z ]")

# A small function to map a character to a number, by pulling out the first
# five binary digits. This routine will convert a space to 0, and then a=1,
# b=2, ..., z=26.
def num(char):
    return ord(char)&31

# This function will create a table of digram probabilities based on an input
# text file. It returns the probabilities in a single list c, so that the
# probability of observing digram (i,j) is given by c[i+27*j].
def create_table(filename):

    # Create empty counters for each digram
    c=[0 for i in range(729)]

    # Open the text file
    f=open(filename,"r")

    # Loop over each line in the file
    for x in f:

        # Convert some punctuation marks to spaces
        x=p.sub(" ",x)

        # Remove everything other than letters and spaces
        x=p2.sub("",x).lower()

        # Loop over each word
        for w in x.split():
            lw=len(w)

            # Add one to the "_X" digram counter where X is the first character
            c[27*num(w[0])]+=1

            # Scan the word and add one two each digram counter
            for i in range(lw-1):
                c[num(w[i])+27*num(w[i+1])]+=1

            # Add one to the "X_" digram counter where X is the last character
            c[num(w[lw-1])]+=1

    # Close the file
    f.close()

    # Count up the total number of entries and add a small fictitious count of
    # 0.1 to all digrams that were not observed, to avoid numerical problems
    # later when taking logarithms
    n=0
    for i in range(729):
        if(c[i]==0):
            c[i]=0.1        
        n+=c[i]

    # Print a status message about the number of digrams that were processed
    print "%s : %d digrams processed" % (filename,int(n))

    # Divide all of the entries by the total to get normalized probabilities,
    # and return the entries as one list
    ni=1.0/n
    for i in range(729):
        c[i]*=ni
    return c

# Create tables for the five languages by processing the five Project Gutenberg
# books. After these lines are run, the probability of digram (i,j) in language
# k is given by t[k][i+27*j].
lang=["English","French","German","Italian","Spanish","sp2"]
t=[0 for i in range(5)]
t[0]=create_table("en_voyage_out.txt.prc")
t[1]=create_table("fr_atlantide.txt.prc")
t[2]=create_table("ge_siddartha.txt.prc")
t[3]=create_table("it_dal_cellulare.txt.prc")
t[4]=create_table("sp_la_voz.txt.prc")

# Make a 2D plot of the English digrams
table_plot(t[0])

# Uncomment the following line to make plot of the differences between Italian
# and Spanish digrams
table_plot_difference(t[0],t[1])
