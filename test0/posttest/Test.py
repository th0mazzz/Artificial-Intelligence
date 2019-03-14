#!/usr/bin/python3

import sys

def ProblemOne():
    f = open(sys.argv[1], 'rU')
    lines = f.read().split('\n')
    f.close()

    return_list = []

    for each in lines:
        temp = each.split(',')
        #print(temp)
        if not (temp[len(temp) - 1] == '' or len(temp) == 1):
            club = [temp[0]]
            temp = temp[1:len(temp)]
            temp.sort()
            club.extend(temp)
            return_list.append(club)


            #print(return_list)
    output = open(sys.argv[2], 'w')
    for club in return_list:
        string = ''
        for thing in club:
            string = string + str(thing) + ','
        string = string[:len(string) - 1]
        output.write(string)
        output.write('\n')
        #output.write(str(club) + '\n')

    output.close()



'''Problem 2'''
class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)

class Dlist:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def __str__(self):
        current = self.start
        if current == None:
            return '[]'
        string = ''
        while not current == None:
            string = string + str(current.value) + ','
            current = current.next
        string = '[' + string[:len(string) - 1] + ']'
        return string
        
    def insert(self, value):
        if self.start == None:
            self.start = Node(value)
            self.end = self.start
        elif value <= self.start.value:
            #print(self.start.value, self.end.value)
            newnode = Node(value)
            self.start.previous = newnode
            newnode.next = self.start
            self.start = newnode
            
        elif value >= self.end.value:
            #if value == 7:
            #    print("here")
            #print(self.start.value, self.end.value)
            newnode = Node(value)
            self.end.next = newnode
            newnode.previous = self.end
            self.end = newnode
        else:
            #print(value, self.end.value, "here")
            current = self.start
            while value > current.value:
                current = current.next
            #print(value, self.end.value)
            newnode = Node(value)
 
            current.previous.next = newnode
            newnode.previous = current.previous
            current.previous = newnode
            newnode.next = current
        self.size = self.size + 1
            
    def delete(self, value):
        if self.start == None:
            return False
        elif self.size == 1 and self.start.value == value:
            self.start = None
            self.end = None
            self.size = self.size - 1
            return True
        elif self.start.value == value:
            self.start = self.start.next
            self.start.previous = None
            self.size = self.size - 1
            return True
        elif self.end.value == value:
            self.end = self.end.previous
            self.end.next = None
            self.size = self.size - 1
            return True
        else:
            current = self.start
            while not current.value == value and not current.next == None:
                current = current.next
            if current.value == value:
                current.previous.next = current.next
                current.next.previous = current.previous
                self.size = self.size - 1
                return True
            return False
        

    def tolist(self):
        returned_list = []
        current = self.start
        
        while not current == None:
            nextnode = current.next
            #print(current.value)
            returned_list.append(current.value)

 
            self.delete(current.value)
            current = nextnode
        return returned_list


def insert_all(the_dlist, the_input_list):
    for element in the_input_list:
        #print(element)
        the_dlist.insert(element)
        
a = Dlist()
insert_all(a,[4,5,2,3,2,7])
print(a.tolist())
