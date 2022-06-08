def switch():
    switcher = {
    'kisses' : "I love you!!",
    'hugs' : "You are awesome and my favourite human!!"
    }
    result = input("choose kisses or hugs: ")
    return switcher.get(result)
print(switch())