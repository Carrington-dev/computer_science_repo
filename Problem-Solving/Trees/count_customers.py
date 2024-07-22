def re_c(file_name):
    counter = 0
    with open(file_name, "r") as f:
        context = dict()
        for i in f.readlines():
            id = (i[0:-1].split(", ")[1])
            if context.get(id) != None:
                counter += 1
            else:
                context[id] = 1
        
    return counter

print(re_c("reads.txt"))