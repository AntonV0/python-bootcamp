# FizzBuzz UML Activity Diagram
```text
Start with NUM = 1
      |
      |
Is NUM <= 100?
      |      \
      |       \
     Yes      No ---- END LOOP
      |
      |
Is NUM a multiple of both 3 and 5?
      |                  |
      |                  |
     Yes                 No
Print "FizzBuzz"         |
      |                  |
      |                  |
      |        Is NUM a multiple of 3?
      |          |                 |
      |          |                 |
      |         Yes                No
      |    Print "Fizz"            |
      |                            |
      |                            |
      |                  Is NUM a multiple of 5?
      |                    |                 |
      |                    |                 |
      |                   Yes               No
      |                Print "Buzz"     Print "NUM"
      |                    \                 /
      |                     \               /
      |                      \             /
      |                       Increment NUM
      |                       (NUM = NUM +1)
      |                             |
      |                  Loop back until NUM > 100
      |                             |
      |                             |
      -------------------------------
                                    |
                                    |
                                 END LOOP

  
## Code for reference:
### Script printing numbers from 1 to 100
for NUM in range(1, 101):
    if NUM % 3 == 0 and NUM % 5 == 0: # multiple of both 3 and 5
        print("FizzBuzz")
    elif NUM % 3 == 0: # multiple of 3
        print("Fizz")
    elif NUM % 5 == 0:  # multiple of 5
        print("Buzz")
    else:
        print(NUM)

### Function implementation
def fizzbuzz(n):
    """Returns a list of strings representing the FizzBuzz sequence from 1 to n. """
    result = [] # list to hold results
    for i in range(1, n + 1): # iterate from 1 to n
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i)) # convert number to string
    return result
