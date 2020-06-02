"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the print f operator (%), print the following feeding in the values of x, y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

"x is %s, y is %s, z is %s" %(x,y,z)


# Use the 'format' string method to print the same thing
"x is {}, y is {}, z is {}".format(x,y,z)


# Finally, print the same thing using an f-string
f"x is {x}, y is {y}, z is{z}"

name = "Eric"
age = 74
f"Hello, {name}. You are {age}."
#'Hello, Eric. You are 74.'

"Hello, {}. You are {}.".format( name, age)
'Hello, Eric. You are 74.'

first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
"Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation)
#'Hello, Eric Idle. You are 74. You are a comedian. You were a member of Monty Python
# print integer and float value 
#print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.333))  
  
 





