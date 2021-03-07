def judge(scores):
    return sorted(scores[1:3])#這邊輸入你要回傳的值

'''
scores = [10, 10, 3, 10, 9, 10, 2, 10, 6, 5]
print(judge(scores))
'''

def checkRepeat(plays):
    return len(plays) > len(set(plays))

plays=[80, 11, 86, 45, 54, 31, 46, 11, 61, 42] #True

#plays= [54, 35, 69, 52, 29, 5, 4, 45, 23, 84] #False

#print(checkRepeat(plays))

def sumOfDigit(num):
    return sum([int(c) for c in str(num)])

'''
print(sumOfDigit(120)) #3
print(sumOfDigit(35)) #8
print(sumOfDigit(261)) #9
print(sumOfDigit(999)) #27
'''

def nine():
    table = [i*j for i,j in range(1,10)]
    print(table)

#nine()

'''
範例一:
input: N=1，W=[[819, 958, 508, 969, 565, 800, 703]]
output: 508 (7個整數中最小的是508)

範例二:
input: N=2, W=[[740, 516, 725, 718, 861, 634, 723],
               [914, 747, 580, 593, 722, 877, 595]]
output: 516 (14個整數中最小的是516)
'''

def findMin(N, W):
    return min([min(w) for w in W])

#N=2
#W=[[740, 516, 725, 718, 861, 634, 723],[914, 747, 580, 593, 722, 877, 595]]
N=1
W=[[819, 958, 508, 969, 565, 800, 703]]
#print(findMin(N,W))

def mostValue(nums, K):
    L = [nums[i] + nums[j] for i in range(len(nums)) for j in range(i+1,len(nums)) if nums[i]+nums[j]<=K]
    return max(L) if len(L) > 0 else -1 


nums = [100,200,500,2000]
K = 1000
#Output: 700

#print(mostValue(nums,K))

def isPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return False 
    return True

#for i in range(0,20):
    #print(i , isPrime(i))

def soldiers(m,n):
    m = [i for i in range(m,n) if i%3 ==2 and i%5 ==3 and i%7 == 2]
    return m

m = 20
n=200
#print(soldiers(m,n))

#g = (x*x for x in range(1,6))
#print(g)

#nums= [[1,-2,-3],[1,5,6]]
#ans = map(abs,nums)
#print(ans)

#友好數(amicable pair)、婚約數（betrothed numbers）

def divisorsum(n):
    return sum([sum({i,n//i}) for i in range(1,int(n**0.5)+1) if n%i==0])-n

def amicable_pair(num):
    #求出num以下的所有amicable pair
    return [(i,divisorsum(i)) for i in range(1,num) if i == divisorsum(divisorsum(i)) and i < divisorsum(i) ]

#print(amicable_pair(100000))

def betrothed_numbers(num):
    return [(i,divisorsum(i)-1) for i in range(2,num) if i == divisorsum(divisorsum(i)-1)-1 and i < divisorsum(i)]

#print(betrothed_numbers(1000))

def isPrime(n):
    return n>=2 and not any(n%i==0 for i in range(2,int(n**0.5+1)))
    
def nextPrime(n):
    while n > 0:
        n += 1
        if isPrime(n):
            return n
''' 
n=1
for i in range(20):
    n = nextPrime(n)
    print(f'{n} is a {i}th prime.')

'''

def rotateRight(arr):
    A = arr[::-1] #利用切片上下翻轉
    return list(map(list,(zip(*A)))) #行列互換，再利用map函數將zip內的元組轉列表

arr = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
#print(rotateRight(arr))

def rotateLeft(arr):
    A = list(map(list,(zip(*arr))))[::-1]
    return A

#print(rotateLeft(arr))
'''
mulFuncs = [lambda x: x*i for i in range(1,6)]

for func in mulFuncs:
    print(func(1))
'''
#arr = [36,88,125,19]
#print(sorted(arr,key= lambda x: (x%2==0, x%10)))

#scores= [(9, 6, 11), (10, 9, 6), (13, 8, 14), (13, 8, 11), (14, 15, 8)]
#print(sorted(scores,key= lambda x: x[0]*2+x[1]*3+x[2]))

hands = ["3c", "Qc", "Js", "Kh", "2h", "5c", "As", "Jd"]
suits = {'c':1, 'd': 2, 'h':3, 's':4}
values= {'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, '2': 15}
#print(sorted(hands, key= lambda c: (values[c[0]],suits[c[1]])))

'''
s = input() #測試範例輸入 Sorting1234
L=sorted(s, key= lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), s.index(x)))
print("".join(L)) #預期結果: ortingS1324
'''

'''
from collections import Counter

def trans(article):
    return ''.join([c.lower() if c.isalpha() else ' ' for c in article])

article = "How are you? I am fine, thank you. And you you you you you? You are so smart."
article = trans(article)
print(article)
count = Counter(article.split())
print(count)
'''

def findPeak(A):
    for i in A:
        if A[i+1] - A[i] < 0:
            return i
    return -1

A=[2,3,8,5,1]
print(findPeak(A))

Str = "The   secret    password   is     5678."
def enterPassword(Str):
    trans= ''.join(['A' if c==' ' else ' ' for c in Str])
    return list(map(len, trans.split()))
    
print(enterPassword(Str))