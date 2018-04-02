# Chapter 2 Exercises


# Exercise 2
def greeting(name):
    print('Hello', name)


greeting(input('Enter your name: '))


# Exercise 3
def your_pay(hours, rate):
    print('Pay: ', float(hours) * float(rate))


your_pay(input('Enter Hours: '), input('Enter Rate: '))


# Exercise 4
width = 17
height = 12.0

# Can you guess on the outcomes?
print(width//2)  # The outcome is 8, because 17/2 is 8.5. Double backslash, //, disregards numbers after the decimal.
# print(width/2.0)  Cannot interact type integer with type float.
# print(height/3)  Same reason as above.
print(1 + 2 * 5)  # 11


# Exercise 5
def cel_fahr(celsius):
    print('Fahrenheit: ', float(celsius) * 1.8 + 32.0)


cel_fahr(input('Enter the temp in celsius: '))








