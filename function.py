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