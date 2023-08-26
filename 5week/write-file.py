# with is a context manger
# tell seek read

open("my_new_file","w")

with open ( "my_new_file", "w",encoding="utf-8") as f:
    f.write("Hello  😊\n😊 World")

with open("my_new_file", 'r',encoding='utf-8') as f:
    print(f.read())
    f.seek(0)
    print(f.read())

with open("my_new_file", 'r',encoding='utf-8') as f:
    print(f.read())
    f.tell()
    f.seek(0)
    f.tell()

with open("my_new_file", "r+", encoding='utf-8') as f:
    print(f.read()) # prints the content
    f.write("Hello😊😊\nWorld")
    print(f.read()) # prints the content

with open("fictional_image","br" ) as image:
    image.seek(((960 * 540)* 3 * 3)+ 9)
    pixel = image.read(1)
