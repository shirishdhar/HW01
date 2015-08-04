# HW01_ex01_04
# Start the Python interpreter and use it as a calculator. 
# Python's syntax for math operations is almost the same as 
# standard mathematical notation. For example, the symbols 
# +, - and / denote addition, subtraction and division, as you would expect. 
# The symbol for multiplication is *.

# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your 
# average time per mile? What is your average speed in miles per hour? 
# (Hint: there are 1.61 kilometers in a mile).
# Average Speed in MPH:

k=10
m=10/1.61
#print('No. of miles is:' + str(m))
tm=43.5
th=tm/60
#print('Time in hours is:' + str(th))
avgt=th/m
mph=m/th
print('Average time per mile is:' + str(avgt))
print('Speed is:' + str(mph))
