# python3

import sys
import threading
#import numpy


def compute_height(n, parents):
    # Write this function
    a = {}
    def h(b):
        if b in a:
            return a[b]
        if b == -1:
            return 0
        gar = 1 + ad(parents[b])
        a[b] = gar
        return gar
        
 
    
    
    max_height = -1
    # Your code here
    for node in range(n):
        max_height = max(max_height, height(node))
    return max_height


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    c = input()
    if c == "F":
        c = input()
        if "a" not in filename:
            with open("./test/" + filename, c = "r") as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
                
                print(compute_height(n, parents))
                
    elif c == "I":
        n = int(input())
        parents = list(map(int, file.readline().split()))
        
        print(compute_height(n, parents))
        
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
