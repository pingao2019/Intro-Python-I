# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
num=[]
for i in range(5):
    if i%2 ==0:
        num.append(i)
print(num)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

n=[]
even_lis=[x for x in num if x % 2==0]
print(even_lis)
odd_lis=[x for x in num if  x % 2==1]
print(odd_lis)
