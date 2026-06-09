# 2025gradingrubric.docx — text digest

_Extracted text from 82 paragraphs. Images, tables, and formatting omitted._

Write a single script (as opposed to a function) that imports the data and can find the peaks and valleys of the respiratory and pulse data before and during a breath hold experiment. It must be no more than 60 lines of code. Specifically, make sure it does the following and is clearly commented so that others can follow your code: 

• Plot the data from the first block of each of the first two channels of data. These should be 

plotted in one single figure with two subplots (one for each channel). See example figure 

above.

• Plot only the first 200 seconds of each of these channels. 

• Plot the raw data in black and use appropriate axis labels and units (as shown above).

• Find and plot the inhalation peaks during tidal breathing as red circles on the respiratory plot.

• Find and plot the exhalation valleys during tidal breathing as green asterisks on the respiratory 

plot.

• Find and plot the pulse peaks during the breath hold as red circles on the pulse plot.

• Find the number of inhalation peaks during tidal breathing and have your code output that 

number to the command window. [Name this variable peakNum1]

• Find the number of exhalation valleys during tidal breathing and have your code output that 

number to the command window. [Name this variable valleyNum1]

• Find the number of pulse peaks during the breath hold and have your code output that number 

to the command window. [Name this variable peakNum2]

• Find the respiratory rate during tidal breathing, and have your code output that number to the 

command window [Name this variable RR]

• Find the heart rate during tidal breathing, and have your code output that number to the 

command window [Name this variable HR]

• Do not hard code. Use variables from the mat file.

• Your code must work when we download it and test it. 

• It cannot contain more than 60 lines of code.

In Gradescope, upload your figure as a PDF and upload your code as an m-file.

Grading rubric:

Total 9 points

Correct -0

Does the PDF match the output of the code? If no -3

Does the code run without needing revisions? If no -2 to -8 depending on severity

Is it more than 60 lines of code? Give a little leniency up to 70 lines. If longer -1

Is the correct time range properly displayed with correct labels? If no –1

Resp: mV (but don’t take off if labeled Volts, since sample labels as Volts)

Pulse: V

Are any peaks or valleys denoted outside of the tidal breathing in respiratory graph or outside of breath hold in pulse graph? If yes, -1 for each.

Are the correct numbers of peaks and valleys found? Both should be in the 35-48 range in respiratory graph, and peakNum2 should be in 50 (45-55 range) in pulse graph. If outside then -1 point per type.

Do not take off points if peakNum1 and valleyNum1 are larger due to plotting after breath hold

Do not take off points if peakNum2 is larger due to incorrect plotting (points were taken off in part 6)

Is RR calculated correctly? This should be ~ 21 bpm. (Anything from 16-26 is fine) If outside this range -1

Is HR calculated properly? This should be ~ 69 bpm. (Anything from 64-74 is fine). If outside this range -2

Was hard coding used? If yes, -0.5 (for 1-2); -1 (for 3-4); -1.5 (for 5-6); -2 (for more than 6)

Correct colors and styles used for markers? If no, -1

Are the correct variables defined? If no -1 or 2 depending on severity

peakNum1 = 40

valleyNum1 = 43

peakNum2 = 50

RR = 21.42

HR = 69.26

Did they submit an actual m file?

If no – 1
