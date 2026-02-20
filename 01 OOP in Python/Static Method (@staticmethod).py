class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 5)) #we can call the static method directly using the class name without creating an instance of the class
m=Math()
print(m.add(10, 20))
