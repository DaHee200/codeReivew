#상근이가 원하는 나무의 길이=m
#나무의 높이 =h
#높이의 최댓값=
#h의 합 >=m
import sys
n,m = map(int,sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
# start(L), mid , end(R) := 톱의 높이
L = 0
R = max(h)
max_mid=0

h.sort(reverse = True)

while L <= R:
    tree=0
    mid = (L+R)//2
    for i in range(n):
        if mid < h[i]:
            tree += h[i] - mid
            if tree > m :
                break
    if m <= tree :
        if m == tree :
            max_mid=mid
            break
        else :
            L = mid+1
            if mid > max_mid:
                max_mid=mid
    else:
        if m == tree :
            max_mid=mid
            break
        else :
            R = mid-1

print(max_mid)