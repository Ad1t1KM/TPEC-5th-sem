if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    maxScore = max(arr)
    while maxScore in arr:
        arr.remove(maxScore)
    print(max(arr))