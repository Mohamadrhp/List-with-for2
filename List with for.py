color_list = ("red","blue","green",12,7)
for new in color_list:
    if isinstance(new,str):
        print(f"{new} is String")
    else isinstance(new,int):
print("Error")