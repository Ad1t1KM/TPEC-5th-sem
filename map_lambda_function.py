# The lambda function to cube a number
cube = lambda x: x**3

def fibonacci(n):
    # This function generates the first n Fibonacci numbers (starting from 0).
    a, b = 0, 1
    result = []
    
    # Handle the case where n is 0 or less
    if n <= 0:
        return []
        
    for _ in range(n):
        result.append(a)
        # Calculate the next numbers in the sequence
        a, b = b, a + b
        
    return result

if __name__ == '__main__':
    # Read the input n
    n = int(input())
    
    # 1. Get the list of the first n Fibonacci numbers
    fib_list = fibonacci(n)
    
    # 2. Use map() to apply the cube lambda function to every element
    # map() returns a map object, so we convert it to a list using list()
    cubed_fibonacci = list(map(cube, fib_list))
    
    # 3. Print the resulting list
    print(cubed_fibonacci)