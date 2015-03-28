#!/usr/bin/env python


class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children
    def __repr__(self):
        return self.name
def recursiveTree(node):
    print node.name
    isNone = node.children is None
    if(isNone):
        return
    for n in node.children:
        recursiveTree(n)
def size(children):
    return 0 if children is None else len(children)

def stackTree(node):
    stack = [node]
    visited = set([])
    while(len(stack) > 0):
        cur_node = stack[-1]
        #print cur_node.name
        cur_children = cur_node.children
        pushed = False
        for i in range(0, size(cur_children)):
            if not cur_children[i] in visited:
                stack.append(cur_children[i])
                pushed = True
                if cur_children[i].children is None:
                    print "stack : ", stack
                break
        if not pushed:
            visited.add(stack.pop())

def main():
    a = Node("a", None)
    g = Node("g", None)
    e = Node("e", None)
    f = Node("f", None)

    b = Node("b", [a,g])
    d = Node("d", [e,f])
    c = Node("c", [b,d])
    #recursiveTree(c)
    stackTree(c)
 
if __name__ == "__main__":
    main()     
