def chop(lis):
    del lis[1]
    del lis[-1]


t = [1, 2, 3, 4]

print(t)
print(chop(t))  # returns None
print(t)
