''' 1. WAGE CALCULATOR '''

def wages(hours, rate):
    if hours <= 40:
        return hours * rate
    else: 
        return (hours - 40) * rate * 1.5 + 40 * rate

# Condition 1. The employee worked 40 or less hours and gets paid at the normal rate.
# Condition 2. The employee worked for more than 40 hours and gets paid 1.5x the normal rate for each additional hour worked.
# You calculate additional hours worked multiplied by the 1.5x rate and add the rate paid at 40 hours worked. 
# Wages is name of the function, hours and rate are the inputs.

''' 2. BLOOD DONATION COMPATIBILITY '''

def canDonateBlood(donor, recipient):
    if donor == "A" and recipient == "A":
        return True
    elif donor == "A" and recipient == "AB":
        return True
    elif donor == "B" and recipient == "B":
        return True
    elif donor == "B" and recipient == "AB":
        return True
    elif donor == "AB" and recipient == "AB":
        return True
    elif donor == "O":
        return True
    else: 
        return False

''' 3. LEAP YEARS '''

def leap(year):
    if year % 4 == 0 and year % 100 != 0: 
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 != 0:
        return False

# Check to see if it is a leap year:
# 1. Is it divisible by 4?
# 2. If so, it cannot be divisible by 100.
# 3. If it is divisible by 100, it must also be divisible by 400. 

''' 4. NUMBER OF DAYS IN A MONTH '''

def daysInMonth(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 29 if leap(year) else 28
    else: 
        return 30

# Jan, Mar, May, July, Aug, Oct, Dec are the months with 31 days.
# Feb is the only month affected by a leap year

''' 5. POINT IN RECTANGLE '''

def pointInRect(x, y, rx, ry, rw, rh):
    if rx <= x <= rx + rh and ry >= y >= ry-rh:
        return True
    else: 
        return False

# Find the boundaries in which x,y can fit in the rectangle.
# rx and ry are the top left coordinate of the rectangle
# rw is the width of the rectangle
# rh is the height of the rectangle 

''' 6. RECTANGLE IN RECTANGLE '''

def rectInRect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x2 <= x1 <= x2 + w2 and y2 >= y1 >= y2 - h2 and x2 <= w1 <= x2 + w2 and y2 >= h1 >= y2 - h2:
        return True
    else:
        return False


# x1 and y1 are the coordinates of the top left corner of the rectangle (Same for x2 and y2)
# w1 is the width (w2)
# h1 is the height (h2)

''' 7. OVERLAPPING RECTANGLES '''

def overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    if pointInRect(x1, y1, x2, y2, w2, h2) or pointInRect(x1 + w1, y1 - h1, x2, y2, w2, h2) or \
        pointInRect(x1 + w1, y1, x2, y2, w2, h2) or pointInRect(x1, y1 - h1, x2, y2, w2, h2):
        return True
    else: 
        return False

























