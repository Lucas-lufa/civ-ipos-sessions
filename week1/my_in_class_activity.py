crazy_list = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(crazy_list[3][1][2][0])

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']
for animal in animals:
    if animal == "Zebra":
        print("Found.")
else:
    print("Not found.")

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']
try:
    animals.index("Zebra")
except ValueError:
    print("Not found.")

animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']
print("Giraffe" == animals[1])


animals = ['Lion', 'Tiger', 'Elephant', 'Giraffe', 'Cheetah']
characteristics = ['Brave','striped','big','tall','fast']

# turnery expression
# list comprehension
# dictionary comprehension