"""
Two types of loops in Python:
1) For Loop
2) While loop
"""

# For loops iterate over a given sequence
primes = [2, 3, 5, 7]
#for prime in primes:
    #print(prime)


"""
For loops can iterate over numbers using "range" and "xrange" functions
- range function returns a new list of numbers within that specified range
- xrange function returns an iterator, which is more efficient

range is zero based
"""
# Prints out the numbers 0,1,2,3,4
print("for x in range(5):")
for x in range(5):
    print(x)

# Prints out 3,4,5
print("\nfor x in range 3, 6:")
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
print("\nfor x in range 3, 8, 2")
for x in range(3, 8, 2):
    print(x)


"""
While loops

- Repeat as long as a certain condition is met.
"""
# Prints out 0,1,2,3,4

count = 0
print("\nWhile loop that prints out 0,1,2,3,4")
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

"""
break and continue statements

- break is used to exit a for loop or while loop
- continue is used to skip the current block and return to the 
'for' or 'while' statement.

"""
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

"""
When to use the 'else' clause for loops
- C and C++ don't have this.

use when the loop condtion of the 'for' or 'while' statement fails,
then the 'else' part of the code is executed.
"""

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")