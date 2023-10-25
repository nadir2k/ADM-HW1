#Say "Hello, World!" With Python
print("Hello, World!")

#Python If-Else
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        if n>=6 and n<=20:
            print("Weird")
        if n>20:
            print("Not Weird")

#Arithmetic operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    first_line = a+b
    second_line = a-b
    third_line = a*b
    
    print(first_line,"\n",second_line,"\n",third_line, sep="")

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    intdiv = a//b
    fldiv = a/b
    
    print(intdiv,"\n",fldiv,sep="")

#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

#Write a function
def is_leap(year):
    leap = False
    
    if year%400 == 0:
        leap = True
    elif year%100 == 0:
        leap = False
    elif year%4 == 0:
        leap = True
    
    return leap

#Print function
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1,end="")

#Birthday Cake Candles

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps
def kangaroo(x1, v1, x2, v2):
    
    if v2 >= v1: 
        return "NO"
    elif (x2-x1) % (v1-v2) == 0: 
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list1 = []
    for i in range(x + 1):
        for j in range (y + 1):
            for k in range (z + 1):
                if i+j+k != n:
                    list1.append([i,j,k])
    print(list1)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr2 = list(set(arr))
    arr2.sort()
    print(arr2[-2])

#Nested Lists
if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
        
    list_grades = [i[1] for i in list1]
    list_grades_sorted = list(set(list_grades))
    list_grades_sorted.sort()
    second_lowest = list_grades_sorted[1]
    
    students = []
            
    for name, score in list1:
        if score == second_lowest:
            students.append(name)

    for name in sorted(students):
        print(name, end='\n')

#Finding the Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = sum(student_marks[query_name]) / 3
    print("%.2f" % average)

#Merge the Tools!
def merge_the_tools(string, k):
    split_list=[string[i-k:i] for i in range(k, len(string)+k,k)]
    for element in split_list:
        substr = ''
        for c in element:
            if c not in substr:
                substr += c
        print(substr)

#sWAP cASE
def swap_case(s):
    x = s.swapcase()
    return x

#String Split and Join
def split_and_join(line):
    # write your code here
    line = line.split(" ") # a is converted to a list of strings. 
    line = "-".join(line)
    return line

#What's Your Name?
def print_full_name(first, last):
    # Write your code here
    print('Hello ', first,' ', last, '! You just delved into python.', sep='')

#Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

#Find a string
def count_substring(string, sub_string):
    count = 0
    s = [*string]
    sub = [*sub_string]
    for i in range(0, len(s)-len(sub)+1):
        count_sub = 0
        for k in range(0, len(sub)):
            if s[i+k] == sub[k]:
                count_sub = count_sub + 1
            if count_sub == len(sub):
                count = count + 1
    return count

#Introduction to Sets
def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))

# Symmetric Difference
M = int(input()) 
a = input().split()
N = int(input()) 
b = input().split()
x=set(a)
y=set(b)
print ('\n'.join(sorted((y.difference(x)).union(x.difference(y)), key=int)))

#No Idea!
n, m = input().split()
arr = ([int(i) for i in input().split()])
setA=set([int(i) for i in input().split()])
setB=set([int(i) for i in input().split()])
happy = 0

for i in arr:
    if i in setA:
        happy+=1
    if i in setB:
        happy-=1

print(happy)

#Set .add()
n = int(input())
s = set()
for i in range(int(n)):
    s.add(input())
print(len(s))

#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
cmdCount = int(input())
for i in range(cmdCount):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
        s.discard(int(cmd[1]))
        
print(sum(s))    

#Set .union() Operation
n = int(input())
a = list(input().split())
m = int(input())
b = list(input().split())

total = set(a).union(set(b))
print(len(total))

#Set .intersection() Operation
n = int(input())
a = list(input().split())
m = int(input())
b = list(input().split())

total = set(a).intersection(set(b))

print(len(total))

#Set .difference() Operation
n = int(input())
a = list(input().split())
m = int(input())
b = list(input().split())

total = set(a).difference(set(b))

print(len(total))

#Set .symmetric_difference() Operation
n = int(input())
a = list(input().split())
m = int(input())
b = list(input().split())

total = set(a).symmetric_difference(set(b))

print(len(total))

#Set Mutations
n = int(input())
a = set(map(int, input().split()))
numSets = int(input())
for i in range(numSets):
    cmd = input().split()
    s = set(map(int, input().split()))
    if cmd[0] == 'intersection_update':
        a.intersection_update(s)
    elif cmd[0] == 'update':
        a.update(s)
    elif cmd[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(s)
    elif cmd[0] == 'difference_update':
        a.difference_update(s)

print(sum(a))

#collections.Counter()
from collections import Counter
x = input()
x_size = Counter(map(int, input().split()))
n = int(input())
earn = 0
for i in range(n):
    size, price = map(int, input().split())
    if x_size[size]:
        x_size[size] -= 1
        earn += price
print(earn)

#DefaultDict Tutorial
from collections import defaultdict
n, m = map(int, input().split())
A = [input() for i in range(n)]
B = [input() for i in range(m)]
d = defaultdict(list)
for i in range(n):
    d[A[i]].append(i+1)
for i in B:
    if i in A:
        print(" ".join([str(x) for x in d[i]]))
    else:
        print(-1)

#Collections.OrderedDict()
n = int(input())
from collections import OrderedDict
ordered_dictionary = OrderedDict()
for i in range(n):
    item_name, price = input().rsplit(' ', 1)
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + int(price)
for item_name in ordered_dictionary:
    print(item_name, ordered_dictionary[item_name])

#Collections.namedtuple()
from collections import namedtuple
n = int(input())
names = input().split()
total = 0
for i in range(n):
    Students = namedtuple('Student', names)
    student = Students(*input().split())
    total += int(student.MARKS)

print(total/n)

#Word Order
n = int(input())
from collections import Counter
word = [input().strip() for x in range(n)]
count = Counter(word)

print(len(count))
[print(x, end=" ") for x in count.values()]

#Collections.deque()
from collections import deque

n = int(input())
d = deque()
for i in range(n):
    cmd = str(input()).split()
    if cmd[0] == "append":
        d.append(int(cmd[1]))
    elif cmd[0] == "appendleft":
        d.appendleft(int(cmd[1]))
    elif cmd[0] == "pop":
        d.pop()
    elif cmd[0] == "popleft":
        d.popleft()
        
print(*(list(d)))

#Company Logo
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = sorted(input())
    from collections import Counter
    s = Counter(s).most_common()
    for i in range(3):
        print(*s[i])

#Calendar Module
import calendar

mm, dd, yy = map(int,input().split())
print((calendar.day_name[calendar.weekday(yy, mm, dd)]).upper())

#Exceptions
testcasenum = int(input())
for i in range(testcasenum):
    try:
        a, b = map(int, input().split(sep=" "))
        print(a//b)
    except (ZeroDivisionError, ValueError) as error:
        print(f"Error Code: {error}")

#Zipped!
n, x = map(int, input().split())

marks = []
for _ in range(x):
    marks.append(map(float, input().split()))

for i in zip(*marks):
    print(sum(i)/len(i))

#Athlete Sort

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    answer = sorted(arr, key = lambda item: item[k])
    
    for i in answer:
        print(*i)


#ginortS    
# Enter your code here. Read input from STDIN. Print output to STDOUT
print(*sorted(input(), key=lambda c: (c.isdigit(), c.isupper(), c.islower(), c in '02468', c)), sep='')

#Map and Lambda Function
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    f = [0, 1]
    if n==0:
        return []
    if n==1:
        return [0]
    if n==2:
        return [0, 1]
        
    for i in range(n-2):
        f.append(f[-1]+f[-2])
    return f
    # return a list of fibonacci numbers

#Detect Floating Point Number
import re
n = int(input())
for _ in range(n):
    num = input()
    print(bool(re.fullmatch(r'^[-+]?[0-9]*[.][0-9]+', num)))

#Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

#Group(), Groups() & Groupdict()
import re
text = input()
m = re.search(r'([a-zA-Z0-9])\1', text)
print(m.group(1) if m else -1)



