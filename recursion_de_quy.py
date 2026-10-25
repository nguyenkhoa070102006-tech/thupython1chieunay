
def compute_factorial(n):
    if n==0:
        return 1
    else:
        return n*compute_factorial(n-1)

if __name__=='__main__':
    a = compute_factorial(3)
    print(a)
