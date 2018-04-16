# Chapter 3 Exercises


# Exercise 1
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hours > 40:
    pay = (40.0 * rate) + ((hours - 40.0) * 1.5 * rate)
else:
    pay = hours*rate
print('Pay: ', pay)

# Exercise 2
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

    if hours > 40:
        pay = (40.0 * rate) + ((hours - 40.0) * 1.5 * rate)
    print('Pay: ', pay)

except:
    print('Error, please enter numeric input')


# Exercise 3
try:
    score = float(input('Enter score: '))
    assert (score <= 1.0)
    assert (score >= 0.0)

    if score >= 0.9:
        print('A')
    elif score > 0.8:
        print('B')
    elif score > 0.7:
        print('C')
    elif score > 0.6:
        print('D')
    else:
        print('F')

except:
    print('Bad score')




