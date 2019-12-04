def validate_input(n):
    if type(n) != int or n < 0:
        print('invalid input')
        return False
    else:
        return True


def fibonacci(n, tortoise=0, hare=1):
    if validate_input(n):
        if n == 0:
            return tortoise
        elif n == 1:
            return hare
        else:
            for i in range(2, n):
                fib = tortoise + hare
                print(fib)
                tortoise = hare
                hare = fib
            return fib


# def lucas(n, tortoise=2, hare=1):
#       if validate_input(n):
#         if n == 0:
#             return tortoise
#         elif n == 1:
#             return hare
#         else:
#             for i in range(2, n):
#                 luc = tortoise + hare
#                 print(luc)
#                 tortoise = hare
#                 hare = luc
#             return luc

def lucas(n):
            return fibonacci(n, tortoise=2, hare=1)          

def sum_series(n, tortoise=0, hare=1):
  if tortoise == 2:
    print('lucas mode')
    return lucas(n)
  else:
    print('fibonacci gang')
    return fibonacci(n, tortoise, hare)


