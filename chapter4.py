# Chapter 4

# Exercise 4
# d) b and c are both true

# Exercise 5
# d) ABC Zap ABC


# Exercise 6
ERROR_NON_NUMERIC = 'Please enter a numerical value.'

def num_checker(num_to_check):
    try:
        float(num_to_check)
        return True
    except:
        return False


def computepay(hours, rate):
    hours = float(hours)
    rate = float(rate)

    normal_hours = 40.0
    overtime_pay = 1.5
    if hours > normal_hours:
        return ((hours - normal_hours) * overtime_pay * rate) + (normal_hours * rate)
    else:
        return hours * rate


# Check to see if hours and rate are numeric.
while True:
    hours = input('Enter Hours: ')
    if num_checker(hours):
        break
    print(ERROR_NON_NUMERIC)

while True:
    rate = input('Enter Rate: ')
    if num_checker(hours):
        break
    print(ERROR_NON_NUMERIC)

print('Pay: ', computepay(hours, rate))


# Exercise 7
ERROR_BAD_SCORE = "Bad score."
grades = ('A', 'B', 'C', 'D')


def computegrade(score):
    score = int(score * 100)
    x = 90
    y = 101
    for grade in grades:
        if score in range(x, y):
            return grade
        elif score < 60:
            return 'F'
            break
        if grade == 'A':
            y = y - 1
        x = x - 10
        y = y - 10


while True:
    score = input('Enter Score: ')
    if num_checker(score):
        score = float(score)
        try:
            assert (score >= 0.0)
            assert (score <= 1.0)
            print(computegrade(score))
            break
        except:
            print(ERROR_BAD_SCORE)

    else:
        print(ERROR_NON_NUMERIC)



