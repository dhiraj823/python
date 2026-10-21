def goodday(name,ending):
    print("Good day, " + name + "!" + ending)

goodday("dhiraj", " have a nice day!")
goodday("sachin", " have a great day!")
goodday("sachin", " have a wonderful day!")


def goodday(name,ending):
    print("Good day, " + name + "!" + ending)
    return "done"

result = goodday("dhiraj", " have a nice day!")
print(result)