import sys

n = int(sys.stdin.readline())
dots = [] 
for i in range(n): 
    dots.append(list(map(int, sys.stdin.readline().split()))) 
dots = sorted(dots, key=lambda x: (x[1], x[0])) 
#sorted는 본체 리스트는 내버려두고 ,정렬한 새로운 리스트를 반환하는 것
#key 옵션(파라미터), reverse옵션(reverse 파라미터)
    
for [i, j] in dots: 
    print(i, j)

