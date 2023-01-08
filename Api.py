from DataType import Fraction

# print(Fraction(Fraction('1/3'),Fraction('1/3')))

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op=='^':
        return 3
    return 0
opset={'*','/','+','-','^'}

# Function to perform arithmetic
# operations.
def applyOp(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return Fraction(a,b)
    if op=='^':return a**b


# Function that returns value of
# expression after evaluation.
def func(tokens):
    # stack to store integer values.
    values = [Fraction(0)]

    # stack to store operators.
    ops = []
    i = 0
    while i < len(tokens):


        # Current token is a whitespace,
        # skip it.
        if tokens[i] == ' ':
            i += 1
            continue

        # Current token is an opening
        # brace, push it to 'ops'
        elif tokens[i] == '(':
            if i and tokens[i-1] not in opset:
                ops.append('+')
            ops.append(tokens[i])
            if tokens[i+1]=='+' or tokens[i+1]=='-':
                values.append(Fraction(0))

        # Current token is a number, push
        # it to stack for numbers.
        # elif tokens[i].isdigit() or tokens[i]=='.':


        # Closing brace encountered,
        # solve entire brace.
        elif tokens[i] == ')':

            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # pop opening brace.
            ops.pop()

        # Current token is an operator.
        elif tokens[i] in opset:
            if i-1>=0 and tokens[i-1] in opset:
                return None

            # While top of 'ops' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'ops'
            # to top two elements in values stack.
            while (len(ops) != 0 and
                   precedence(ops[-1]) >=
                   precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # Push current token to 'ops'.
            ops.append(tokens[i])
        else:
            val = ''

            # There may be more than one
            # digits in the number.
            while (i < len(tokens) and
                   (tokens[i].isalnum() or tokens[i]=='.')):
                val+=tokens[i]
                i += 1

            values.append(Fraction(val))

            # right now the i points to
            # the character next to the digit,
            # since the for loop also increases
            # the i, we would skip one
            #  token position; we need to
            # decrease the value of i by 1 to
            # correct the offset.
            i -= 1

        i += 1

    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyOp(val1, val2, op))

    # Top of 'values' contains result,
    # return it.
    # if len(values)==1:
    #     return values[0]
    return values[-1]










































































# def func(string):
#     stack=[]
#     starting_point=[0]
#
#     breakage_point=['(',')','*','+','-']
#     breakage_point=set(breakage_point)
#     temp=''
#     idx=0
#     s=0
#     for i in range(len(string)):
#         ele=string[i]
#         if ele in breakage_point:
#             if temp!='':
#                 stack.append(Fraction(temp))
#                 idx+=1
#                 temp=''
#
#             stack.append(ele)
#             idx+=1
#             if ele=='(':
#                 starting_point.append(idx)
#                 s+=1
#             if ele==')':
#                 s-=1
#             if s<0:
#                 return 'ERROR not correct equation'
#         else:
#             temp+=ele
#     if len(temp):
#         stack.append(temp)
#
#     print(string)
#     print(stack)
#     print(starting_point)


# breakage_point = ['(', ')', '*', '+', '-']
# breakage_point = set(breakage_point)
# def func(string,n,i=0):
#     temp=''
#     while i==n or string[i]==')':
#         if temp=='':
#             return 'ERROR'
#         #now the operation
#         if temp[0]=='(' and temp[-1]==')':
#             m=len(temp)
#             temp=temp[1:m-1]
#         elif temp[0]=='(' or temp[-1]==')':
#             return 'ERROR'
#         #convert to arr
#         arr=[]
#         t=''
#         for char in temp:
#             if char in breakage_point:
#                 if len(t):
#                     arr.append(Fraction(t))
#                     t=''
#                 arr.append(char)
#             else:
#                 t+=char
#         if len(t):
#             arr.append(Fraction(t))
#         res=0
#         for ele in
#
#
#
#
#
#
# func(input())
