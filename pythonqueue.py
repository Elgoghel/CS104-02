# Marwan Elgoghel
# Program: PythonQueue
names = []

for _ in range(10):
    name = input("Enter Name: ")
    names.append(name)

print(names)

for _ in range(10):
    print(names.pop(0))

print(names)