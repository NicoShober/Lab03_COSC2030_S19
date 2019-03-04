import operator
ops = {
       '+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow
       }

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(exp):
    stack = []
    result = 0
    for i in exp:
        if is_number(i):
            stack.append(i)
        else:
            if len(stack) < 2:
                print ('Error: insufficient values in expression')
                break
            else:
                print ('stack: ', stack, 'where i = ', i)
                operand1 = float(stack.pop())
                operand2 = float(stack.pop())
                result = ops[i](operand2,operand1)
                stack.append(str(result))
    return result

print ("Start of Reverse Polish Notation Evaluator")
exp_file = open("Expressions2.txt", 'r')
for line in exp_file:
        exp_list = line.rstrip().split(' ')
        answer = calculate(exp_list)
        print ('RESULT: %f' % answer)
print ("End of Reverse Polish Notation Evaluator")
