#!/usr/bin/python
import sys
import re
reload(sys) 
sys.setdefaultencoding("utf-8")
import unicodedata

# This Python program is not needed for the homework, but it can be used to process
# Project Gutenberg text files and remove special characters and accents. It also removes
# the extraneous header and footer of the files

# Check that a filename has been given
if len(sys.argv)!=2:
    print "Syntax: ./remove_acc.py <filename>"
    sys.exit()

# Function to remove accents from a string
def remove_accents(input_str):
    nkfd_form = unicodedata.normalize('NFKD',unicode(input_str))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

# Regular expressions to detect the end of the header and start of the footer
ps=re.compile("\*\*\* START OF THIS PROJECT GUTENBERG")
pe=re.compile("\*\*\* END OF THIS PROJECT GUTENBERG")

# Open the file
f=open(sys.argv[1],"r")

# Skip the header
for x in f:
    if(ps.match(x)):
        break

# Open the output file
g=open(sys.argv[1]+".prc","w")

# Print until the footer starts
for x in f:
    if(pe.match(x)):
        break
    g.write(remove_accents(x))
