def outer():
    x=1

    def inner():
        x=2
        return 2
    
    inner()
    return inner(), x

print(outer())