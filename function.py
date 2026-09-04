def calcsum(a,b):
  sum=a+b
  print(a+b)
  return(sum)

calcsum(30,5)

calcsum(10,45)

calcsum(20,34)

def print_hello():
  print('hello')
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

def calc_avg(a,b,c):
  sum=a+b+c
  avg=sum/3
  print(avg)
  # return avg

calc_avg(100,200,45)

def cal_multi(a,b=3):
  print(a*b)
  # return a*b
cal_multi(1)

def cal_porb(a,b=5):
  print(a*b)
  # return a*b
cal_porb(2)

cities=['magura','jhenaidha','khulna','jashore']
heroes=['thor','hulk','captain america','iron man']

def print_len(list):
  print(len(list))

print_len(cities)
print_len(heroes)

cities=['magura','jhenaidha','khulna','jashore']
heroes=['thor','hulk','captain america','iron man']
def print_list(list):
  for item in list:
    print(item,end=' ')
print_list(cities)


def cal_fact(n):
  fact=1
  for i in range(1,n+1):
    fact*=i
  print(fact)
cal_fact(5)

def evenodd(n):
  if n%2==0:
    print('EVEN')
  else:
    print('ODD')
k=int(input('enter:'))
evenodd(k)

def printInfo(num1, num2):
    print(f'We are adding {num1} and {num2}...')
    return

def addition(num1, num2):
    """This function adds two numbers and returns the value"""
    result = int(num1) + int(num2)
    return result

n1 = input('Enter number1: ')
n2 = input('Enter number2: ')

printInfo(n1, n2)
res = addition(n1, n2)
print('Result is:', res)

def total_sum(*numbers):
    print(sum(numbers))

total_sum(10, 20, 30)  # Output: 60


def show_info(**data):
    print(data)

show_info(name="Tania", age=22,village='tai')

def an():
  return "This function adds two numbers and returns the value"

def  addition(num1, num2):
  num1 = int(num1)
  num2 = int(num2)
  result = num1 + num2
  return result

print(an())
print(addition(20,120))

def maximum(a,b):
  return max(a,b)
print(maximum(10,2))

def max_min_num(a, b):
    if a > b:
        return f"Max: {a}, Min: {b}"
    else:
        return f"Max: {b}, Min: {a}"

# Example usage:
print(max_min_num(300, 10000))