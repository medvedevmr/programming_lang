class Stack:
    
    def __init__(self,stack_in):
        self.stack = stack_in
        
    def pop(self):
        if len(self.stack) == 0:
            return None
        
        pop_element = self.stack.pop()
        return pop_element
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        
        return self.stack[-1]
    
    def push(self,val):
        self.stack.append(val)
        return self.stack
    
    

new_stack = Stack([1,2,3])

new_stack.push(4)
print(new_stack.stack)

new_stack.pop()
print(new_stack.stack)

print(new_stack.peek())