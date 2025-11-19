if __name__=='__main__':
    n = int(input())
    arr = []
    
    for _ in range(n):
        command = input().split()
        op = command[0]
        
        if op=="insert":
            arr.insert(int(command[1]), int(command[2]))
        elif op == "print":
            print(arr)
        elif op == "append":
            arr.append(int(command[1]))
        elif op == "remove":
            arr.remove(int(command[1]))
        elif op == "pop":
            arr.pop()
        elif op == "reverse":
            arr.reverse()
        elif op == "sort":
            arr.sort()