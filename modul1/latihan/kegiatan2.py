def random_array():
    random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
    bentuk_string = []
    bentuk_integer = {}
    tmpTuple = []

    dicIndex = 0
    for x in random_list:
        if isinstance(x, str):
            bentuk_string.append(x)
        elif isinstance(x, int):
            bentuk_integer["dictionary"+str(dicIndex)] = x
            dicIndex = dicIndex + 1 
        elif isinstance(x, float):
            tmpTuple.append(x)

    return "Hasil :\nBentuk String "+str(bentuk_string)+"\nBentuk Integer "+str(bentuk_integer)+"\nBentuk Float "+str(tuple(map(float, tmpTuple)))

print(random_array())