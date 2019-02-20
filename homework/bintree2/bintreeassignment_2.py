#! /usr/bin/python3
import sys

class Node:
    def __init__(self, data):
        self.value = data
        self.smaller = None
        self.larger = None
        
    def __str__(self):
        return str(self.value)

class BinTree:
  
    def __init__(self, A = None): # A is an optional argument containing a list of values to be inserted into the binary tree just after cosntruction
        self.num_of_nodes = 0
        self.root = None
        if not A == None:
            for each in A:
                self.insert(each)

    def size(self):
        return self.num_of_nodes
        
    def insert(self, V): # inserts a new value 
        if self.root == None:
            self.root = Node(V)
            self.num_of_nodes = self.num_of_nodes + 1
        else:
            if not self.has(V):
                self.insert_help(self.root, V)
                
        
    def insert_help(self, current, V):
        if V < current.value:
            if current.smaller == None:
                current.smaller = Node(V)
                self.num_of_nodes = self.num_of_nodes + 1
            else:
                self.insert_help(current.smaller, V)
        else:
            if current.larger == None:
                current.larger = Node(V)
                self.num_of_nodes = self.num_of_nodes + 1
            else:
                self.insert_help(current.larger, V)
        
        
    def has(self, V): # returns True if V is in the list, else False
        return self.has_help(self.root, V)
        
    def has_help(self, current, V):
        if V == current.value:
            return True
        else:
            if V < current.value:
                if current.smaller == None:
                    return False
                else:
                    return self.has_help(current.smaller, V)
            else:
                if current.larger == None:
                    return False
                else:
                    return self.has_help(current.larger, V)
                  
    def has_depth(self, V): #returns the depth of the node if found, if not found, returns the depth it gave up
        if self.root == None:
            return 0
        else:
            return self.has_depth_help(self.root, 1, V)
      
    def has_depth_help(self, current, depth, V):
        if V == current.value:
            return depth
        else:
            if V < current.value:
                if current.smaller == None:
                    return depth
                else:
                    return self.has_depth_help(current.smaller, depth + 1, V)
            else:
                if current.larger == None:
                    return depth
                else:
                    return self.has_depth_help(current.larger, depth + 1, V)
        
        
    def get_ordered_list(self): # returns a list of all values in ordered sequence
        if self.root == None:
            return []
        return self.get_ordered_list_help(self.root)
        
    def get_ordered_list_help(self, current):
        ordered = []
        if not current.smaller == None:
            ordered.extend(self.get_ordered_list_help(current.smaller))
        ordered.append(current.value)
        if not current.larger == None:
          ordered.extend(self.get_ordered_list_help(current.larger)) 
        return ordered
        
    def clear(self): # clears the list of all nodes
        self.clear_help(self.root)
        self.root = None
        
    def clear_help(self, current):
        if not current.smaller == None:
            self.clear_help(current.smaller)            
        if not current.larger == None:
            self.clear_help(current.larger)
        current.smaller = None
        current.larger = None
        
def Process(infilename, outfilename):
    try:
        f = open(infilename, 'r')
        lines = f.read().split('\n')
        f.close()
    except:
        print('Please input the following command:\npython bintreeassignment_2.py <input file name> <output file name>')
        return('bad shit')
          
    ints = [int(x) for x in lines[0].split(',')]
        
    tree = BinTree()
    for each in ints:
        tree.insert(each)
            
    ints2 = [int(x) for x in lines[1].split(',')]
    return_ints = []
    for each in ints2:
        return_ints.append(tree.has_depth(each))

    sum = 0.0
    for each in return_ints:
        sum = sum + each
    avg = sum / len(return_ints)
    #print('Average: ' + str(avg))
    #print('Log2 (' + str(tree.size()) + '): ' + str(math.log(tree.size(), 2)))
        
    F = open(outfilename, 'w')
    sInts = [str(x) for x in return_ints]
    F.write(','.join(sInts)+'\n')
    F.close()

def main():
    try:
        Process(sys.argv[1], sys.argv[2])
    except:
        print('Please input the following command:\npython bintreeassignment_2.py <input file name> <output file name>')
# Testing

main()
