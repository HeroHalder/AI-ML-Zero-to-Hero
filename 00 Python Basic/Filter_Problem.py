nums = [2, 3, 4, 5, 6, 7, 8, 9]
prime=list(filter(lambda x: all(x%i!=0 for i in range(2,x)),nums))
print(prime)
