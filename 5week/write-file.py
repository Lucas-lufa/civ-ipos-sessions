# with is a context manger
#tell seek 

open("my_new_file","w")

with open ( "my_new_file", "w") as f:
    f = open("my_new_file","r", encoding="utf-8")


with open("my_new_file", 'r',encoding='utf-8') as f:
    f.seek()



