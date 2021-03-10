while True:
    bracket = input()
    if bracket == ".":
        break
    bracket_stack = []
    answer = True
    
    for j in bracket:
        if j == "(" or j == "[":
            bracket_stack.append(j)
        
        elif j == ")":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "(":
                bracket_stack.pop()
            else:
                answer = False
                break
                
        elif j == "]":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "[":
                bracket_stack.pop()
            else:
                answer = False
                break

    if answer and not bracket_stack:
        print("yes")
    else:
        print("no")
# while 1: 
#     string = input().rstrip() 
#     true_flag = 1 
#     for cha in string: 
#         if cha == '(' or cha == '[': 
#             stack.append(cha) 
#         elif cha == ')': 
#             if stack and stack[-1] == '(': 
#                 stack.pop() 
#             else: true_flag = 0 
#             break 
#         elif cha == ']': 
#             if stack and stack[-1] == '[': 
#                 stack.pop() 
#             else: true_flag = 0 
#             break 
#         if string == '.': 
#             break 
        # print("yes" if true_flag and not(stack):else "no")
        #삼항연산자
        
