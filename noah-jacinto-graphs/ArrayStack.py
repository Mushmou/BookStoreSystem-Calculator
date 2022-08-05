from os import X_OK
import numpy as np
from Interfaces import Stack


class ArrayStack(Stack):
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemthods should be implemented. 
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple, 
        s = ArrayStack()
        print(s)
        print(len(s))
    '''
             
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0

    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)
    
    def resize(self):
        '''
            Resize the array
        '''
        b = self.new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def get(self, i : int) -> object:
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[i]
    
    def set(self, i : int, x : object) -> object:
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i: int, x : object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''

        if i < 0 or i > self.n: raise IndexError()
        if self.n >= len(self.a): self.resize()
        
        '''
        if self.n >= len(self.a): self.resize()
        stems from
        if self.n == len(self.a): self.resize()
        if self.n + 1 > len(self.a): self.resize()
        '''

        # for j in range(self.n,i):
        #     self.a[j] = self.a[j-1]
        # self.a[i] = x
        # self.n += 1

        #stack = [0]
        #stack = [a]
        #stack = [a, 0]
        #stack = [a, b]
        #stack = [a, b, 0, 0]
        #self.n-1 is the last element
        #i-1 represents the position to add

        #stack = [0]
        #stack = [a]
        #stack = [a, 0]
        #stack = [c, b, a, 0]
        #stack = head -> [c, b, a, 0] <- tail

        for j in range(self.n-1, i-1, -1):
            self.a[j+1] = self.a[j]
        self.a[i] = x 
        self.n += 1

    def remove(self, i : int) -> object :
        '''
            remove element i and shift all j > i one 
            position to the left
        '''

        # x = self.a[i]
        # for j in range(self.n,i):
        #     self.a[j] = self.a[j+1]
        # self.n = self.n-1

        #stack = [a,b,c,0]
        #stack = [a,b,c,0]
                    # start
                    #want to change a to b
                    #self.n represents the tail
        #stack = []
        if i < 0 or i > self.n: raise IndexError()
        x = self.a[i]
        for j in range(i+1, self.n, 1):
            self.a[j-1] = self.a[j]
            #first iteration changes index 0 to index 1
            #second iteration changes index 1 to index 2
            #third iteration changes index 2 to index 3
        self.n -= 1
        if len(self.a) >= self.n * 3: self.resize()
        return x

    def push(self, x : object) :
        #Change self.n to zero to switch the top and bottom
        self.add(0, x)
    
    def pop(self) -> object :
        #Change self.n to zero to switch the top and bottom
        return self.remove(0)

    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n
        
    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x





# testStack = ArrayStack()
# testStack.push(5)
# testStack.push(4)
# testStack.push(3)
# testStack.push(2)
# testStack.push(1)
# print("Before POP")
# print(testStack)
# testStack.pop()
# print("After POP")
# print(testStack)
