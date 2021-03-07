#이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

#string모듈 사용
import string


# string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


txt = input().upper()
#txt=mississipi
txt_list = list(set(txt)) 
# txt_list=[m, i, s, p]

n_num=[]
for i in txt_list:
    count = txt.count(i)
    #중복 문자 삭제적 txt에서 문자를 카운트 받아 n_num에 넣어 준다
    n_num.append(count)
    #n_num=[1, 4, 4, 1]


if n_num.count(max(n_num)) >= 2 :
    #n_num의 최대값의 갯수가 2개보다 크면 '?'를 출력하고
    print('?')
else:
    print(txt_list[(n_num.index(max(n_num)))])
# txt_list=[m, i, s, p]
    #n_num=[1, 4, 4, 1]
    # max(n_mun)=4이고 n_num.index(4)는 n_num[1,2]에 위치한다
    #  n_num[1,2]는 txt_list의 i와s기 때문에 2개이디 때문에 '?'를 출력한다

