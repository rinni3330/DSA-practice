def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = int(input("Enter number: "))
print(fibonacci(n))


#iteration
def fib(m):
    a = 0
    b = 1
    for i in range(2, m+1):
        c = a + b
        a = b 
        b = c
    return b 

m = int(input("Enter number: "))
print(fib(m))