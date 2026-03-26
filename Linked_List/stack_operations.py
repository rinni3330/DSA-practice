stack = []

def push():
    n = int(input("enter the element to insert:"))
    stack.append(n)
    print("element is inserted:",n)

def pop():
    if not stack:
        print("Underflow")
    stack.pop(-1)
    print("element is deleted")

def peek():
    if not stack:
        print("Underflow")
    print("top most element is",stack[-1])

def get_min():
    if not stack:
        print("Underflow")
        return
    print("minimum element:", min(stack))
    

while(1):
    print("\n1.PUSH\n2.POP\n3.PEEK\n4.MINIMUM ELEMENT\n")
    choice = int(input("enter your choice:"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        get_min()
    elif choice == 5:
        exit()
    else:
        print("Invalid Choice")