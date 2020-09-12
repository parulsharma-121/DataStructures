'''  
Implementation of the stack in Python

'''
def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def pushInStack(stack ,item):
    stack.append(item)

def popFromStack(stack):
    if(isEmpty(stack)):
        print("underflow")
    return stack.pop()

def peek(stack):
    return stack[len(stack)-1]

stack = createStack()
pushInStack(stack, str(10))
pushInStack(stack, str(20))
pushInStack(stack, str(30))
pushInStack(stack, str(40))
print(stack)
popFromStack(stack)
print(stack)
print('top element', peek(stack))
