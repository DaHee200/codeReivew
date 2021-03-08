# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다.
#1<=
# b=밤에 미끄러지는 길이 <= a=낮에 올라가는 길이<=v=총 올라가야하는 길이
#1,000,000,000 <=
# 2 1 5
import sys
import math


a, b, v = map(int, sys.stdin.readline().split())

m = (v-b)/(a-b)
print(math.ceil(m))




