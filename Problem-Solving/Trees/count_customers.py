def re_c():
    counter = 0
    with open("reads.txt", "r") as f:
        context = dict()

        for i in f.readlines():
            id = (i[0:-1].split(", ")[1])
            if context.get(id) != None:
                counter += 1
            else:
                context[id] = 1
        
    return counter

print(re_c())