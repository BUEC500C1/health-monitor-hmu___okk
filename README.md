EC500 - Health Monitor App 
======

## E ONeill, M Reardon P Ntwari Y Hu

See our diagram with in/out requirements: [here](https://docs.google.com/drawings/d/1FXb8c75xwbaKGcj1nLO9n2uSQYTBvNJJKbBac1Zvgxg/edit?usp=sharing)

# BP and Pulse Values
 
hmu_vitals.py has code that returns blood pressure and pulse values. The amount of data returned may depend on the user, but the default is an hour worth of data. The code takes the increment and converts that into amount of data values to give back. For example: a 1 second increment returns 3600 values because one hour contains 3600 seconds. 
The function bp returns a list of tuples of both systolic and diastolic blood pressure. 
The function pulse returns a list of one value.
They are the same size lists. 
When calling both functions, specificy the sec as 1, or any other value needed that is less than or equal to 5. 

There are some precautions put int he code to not give absolutely wild numbers. For example, the diastolic pressure is limited to a certain range, given the randomly simulated systolic pressure. 
In addition, once a systolic pressure is randomly simulated, the next one must be within 5 integer units of this. This is to prevent a reading of 110 to 79, which would be unrealistic. 

# DISPLAY
display.py imports the bp and pulse lists and draws directly from this information. The source of the data may be changed, but the display code assumes a list of tuples for the blood pressure and a list for pulse. 
The display is basically a print function that gives the date and the time before giving the blood pressure and pulse. 
It is important to notice, the values are displayed every five (5) seconds. That is to say, even if the hmu_vitals.py simulates values every 1 second (or less depending on user's wish), the display shows the values every 5 seconds, or every fifth simulated value.
The pulse should be between 60 to 100. 
This is an example of the output. 

************************VITALS*************************
****************DATE:  2020-03-23  *********************
19:13:34   Blood Pressure   139  /  86
19:13:34   Pulse  76
19:13:39   Blood Pressure   139  /  86
19:13:39   Pulse  74
19:13:44   Blood Pressure   134  /  85
19:13:44   Pulse  74
19:13:49   Blood Pressure   134  /  88
19:13:49   Pulse  68
19:13:54   Blood Pressure   133  /  89
19:13:54   Pulse  62
19:13:59   Blood Pressure   133  /  87
19:13:59   Pulse  61
19:14:04   Blood Pressure   126  /  80
19:14:04   Pulse  63
19:14:09   Blood Pressure   123  /  81
19:14:09   Pulse  60
19:14:14   Blood Pressure   117  /  76
19:14:14   Pulse  61
19:14:19   Blood Pressure   117  /  74
19:14:19   Pulse  60
19:14:24   Blood Pressure   116  /  74
19:14:24   Pulse  60
19:14:29   Blood Pressure   120  /  81
19:14:29   Pulse  62

# Data Base and AI
The database pulls from the hmu_vitals.py module every 2 seconds. This saves the values into a text file and keeps track of the average of the most recent 5 values to be able to understand trends.

