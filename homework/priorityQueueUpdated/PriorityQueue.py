#!/usr/bin/python3

class PQueue:
    def OrdinaryComparison(a,b): #ordinary compare_to fxn
        if a < b: return -1
        if a == b: return 0
        return 1
    
    def __init__(self, comparator = OrdinaryComparison): #initializes priority queue / heap
        self.info = []
        self.size = 0
        self.compare_to = comparator
                
    def __str__(self): #the to-string method
        return str(self.info)

    
    def push(self, value): #pushs value into heap; sorts it so that parent >= child
        self.info.append(value)
        self.size = self.size + 1

        current = self.size - 1
        parent = int((current - 1) / 2)

        while(self.compare_to(self.info[current], self.info[parent]) == -1 and parent >= 0):
            self.info[current], self.info[parent] = (self.info[parent], self.info[current])

            current = parent
            parent = int((parent - 1) / 2)

    def pop(self): #pops off the top element and returns it; if empty, returns None
        if self.size == 0:
            return None
        
        oldroot = self.info[0]

        self.info[0] = self.info[self.size - 1]
        del self.info[-1]
        self.size = self.size - 1

        current = 0
        leftchild = 2 * current + 1
        rightchild = 2 * current + 2

        #print('leftchild: ' + str(leftchild))
        #print('rightchild: ' + str(rightchild))

        if self.size == 2 and self.compare_to(self.info[current], self.info[leftchild]) == 1:
            self.info[current], self.info[leftchild] = (self.info[leftchild], self.info[current])
        
        while(leftchild < self.size and rightchild < self.size and
              (self.compare_to(self.info[current], self.info[leftchild]) == 1 or self.compare_to(self.info[current], self.info[rightchild]) == 1)):
            #print('leftchild: ' + str(leftchild))
            #print('rightchild: ' + str(rightchild))
            if self.compare_to(self.info[leftchild], self.info[rightchild]) == 1:
                self.info[current], self.info[rightchild] = (self.info[rightchild], self.info[current])
                current = rightchild
                leftchild = current * 2 + 1
                rightchild = current * 2 + 2
            else:
                self.info[current], self.info[leftchild] = (self.info[leftchild], self.info[current])
                current = leftchild
                leftchild = current * 2 + 1
                rightchild = current * 2 + 2
                
        return oldroot
                
    def peek(self): #returns but does not pop top element; if empty, returns None
        if self.size > 0:
            return self.info[0]
        return None

    def size(self): #returns size of the current priority queue / heap
        return self.size

    def tolist(self):
        returned_list = []
        size = 0
        while size < len(self.info):
            returned_list.append(self.pop())
        return returned_list

    def push_all(self, the_list): #pushs all the elements of the provided list
        for each in the_list:
            self.push(each)

    def internal_list(self): #returns all of the valid elements of your internal list
        return self.info[:self.size]

#Testing

p=PQueue()
p.push_all(list('PETERBR'[::-1]))
print(p.internal_list())
p.pop()
p.pop()
print(p.internal_list())



#a = Pqueue()

# a.push(10)
# a.push(8)
# a.push(12)
# a.push(100)
# a.push(22)
# a.push(2)

#a.pop()
#a.pop()
#a.pop()

#a = Pqueue([1, 3, 3, 5])

#a.push(100)
#a.push(43)
#a.push(9)
#a.push(4)

#a.pop()

# print(a.tolist())

# print('-----')
# print(a)
# print('Size: ' + str(a.size))
# print('-----')
