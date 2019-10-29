# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked
# above 40 hours.
# Put the logic to do the computation of pay in a function called computepay()
# and use the function to do the computation. The function should return a value.
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.



def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        return (40 * r) + (h - 40) * (r * 1.5)


hrs = input("Enter Hours:")
h = float(hrs)

rt = input("Enter Rate:")
r = float(rt)

p = computepay(h,r)
print(p)
