beer = 99

# while beer > 0:
#     bottle = "bottle" if beer == 1 else "bottles"
#     print(f"{beer} {bottle} of beer on the wall")
#     beer -= 1
# print("More bottles of beer on the wall.")

for count in range(99,0,-1):
    bottle = "bottle" if beer == 1 else "bottles"
    print(f"{beer} {bottle} of beer on the wall")
    beer -= 1
print("More bottles of beer on the wall.")