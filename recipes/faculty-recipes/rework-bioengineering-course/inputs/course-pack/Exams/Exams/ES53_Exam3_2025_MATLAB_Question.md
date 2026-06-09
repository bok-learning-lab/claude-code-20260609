# ES53_Exam3_2025_MATLAB_Question.docx — text digest

_Extracted text from 46 paragraphs. Images, tables, and formatting omitted._

ES 53: Quantitative Physiology [2025]

Exam 3 – Non-timed MATLAB Question 

INSTRUCTIONS: 

We recommend setting aside approximately 30-60 minutes to finish the final MATLAB question; however you can spend as much time as you want on it before the deadline (12:30pm Eastern Thursday Dec. 4th).

You must complete this coding task on your own without the help of others. Any AI you use is your responsibility to check and verify for correctness. No copying from others or the internet is allowed. You may however use parts of your own past code that you wrote, and you may use the online MATLAB documentation. No collaboration or TF help on this exam question is allowed. It must represent your work only and you cannot borrow code from any other peers with whom you may have worked during the semester.

Submit two files to Gradescope. Submit the graph of the output of your code as a PDF. Also submit your m-file script (not a live script). Go back and check that both files show up clearly in Gradescope. 

Good luck!

Download the .mat data file (respiratorydata.mat) from Canvas. This is just like the data you collected in lab 6.

Specifically, 

Write a single script (as opposed to a function) that imports the data and can find the peaks and valleys of the respiratory and pulse data before and during a breath hold experiment. It must be no more than 60 lines of code. Specifically, make sure it does the following and is clearly commented so that others can follow your code: 

Plot the data from the first block of each of the first two channels of data. These should be plotted in one single figure with two subplots (one for each channel). See example figure above.

Plot only the first 200 seconds of each of these channels. 

Plot the raw data in black and use appropriate axis labels and units (as shown above).

Find and plot the inhalation peaks during tidal breathing as red circles on the respiratory plot.

Find and plot the exhalation valleys during tidal breathing as green asterisks on the respiratory plot.

Find and plot the pulse peaks during the breath hold as red circles on the pulse plot.

Find the number of inhalation peaks during tidal breathing and have your code output that number to the command window. [Name this variable peakNum1]

Find the number of exhalation valleys during tidal breathing and have your code output that number to the command window. [Name this variable valleyNum1]

Find the number of pulse peaks during the breath hold and have your code output that number to the command window. [Name this variable peakNum2]

Find the respiratory rate during tidal breathing, and have your code output that number to the command window [Name this variable RR]

Find the heart rate during tidal breathing, and have your code output that number to the command window [Name this variable HR]

Do not hard code. Use variables from the mat file.

Your code must work when we download it and test it. 

It cannot contain more than 60 lines of code.

In gradescope, upload your figure as a PDF and upload your code as an m-file. 
