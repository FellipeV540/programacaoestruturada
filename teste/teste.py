def dobra(y):
    global x
    x = y + y
    return x

x = 5
dobra(x)
dobra(x)
print(x)