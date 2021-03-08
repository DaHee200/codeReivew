#100째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. 
# (1 ≤ M ≤ N ≤ 1,000,000) 
# M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
import math
import sys

def isPrime(i) :
    if i > 1:
        j = int(math.sqrt(i)) 
        #제곱근인것은 약수! 
        # i의 제곱근, 제곱근으로 할시 소수점이끼기때문에 int로 소수점을 제외시킴
        for x in range(2, j+1):
            # 소수의 정의가 1을 제외하기 때문에 2부터 시작해서 뒤의 j+1은 미만이기때문에 
            if i % x == 0: 
                # 2와 J+1사이의 값들  나머지가 0일경우 약수기때문에 false
                return False
        return True


M, N = map(int, sys.stdin.readline().split())

for k  in range(M, N+1):
    if isPrime(k) : 
    #return True 생략
        print(k)