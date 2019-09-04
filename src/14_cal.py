"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


x = input("Enter comma-separated month and year ").split(',')
y = [int(x) for x in x]


def big_cal(year, m=1) :
        print ("Calendar of March 2019 is:")
        print (calendar.month(year, m, 2, 1))
print(y[1], y[0])

big_cal(y[0], y[1])

"""
def is_even_the_classic(n):
        if n % 2 == 0:
            print('even')
        else:
            print('odd')


is_even_the_classic(num)
"""