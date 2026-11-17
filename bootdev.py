unecessary = [5, 6, 2, 3]
necessary = [4, 5, 3, 5]

def is_unecessary(a, b):
    if a > b:
        print("unecessary")
    else:
        print("necessary")

def iterate(unecessary, necessary):
    for a, b in zip(unecessary, necessary):
        is_unecessary(a, b)

iterate(unecessary, necessary)
