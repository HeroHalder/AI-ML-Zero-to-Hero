nums = [1, 2, 2, 3, 4, 5, 5, 6]
unique=set(nums)
odd={x for x in unique if x%2==1}
cube={x**3 for x in odd}
print(list(cube))
