def mulby(n):
    def mult(x):
        return x * n

    return mult


f = mulby(5)
print(f(10))
