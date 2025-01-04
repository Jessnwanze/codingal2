def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    num - int(input("Enter a number"))

    if num < 0:
        print("sorry, factorial does not exist for negative numbers")
    elif num == 0:
      print("the factorial of 0 is 1")
    else:
      print("the factorial of",num,recur_factorial(num))