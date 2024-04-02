# list
# create

numbers = [0, 1, 2, 3, 4]
chars = ['a', 'b','c', 'd']
users = ['Allen', 'Chen', 'John', 'May']       

#access, update -> index(자리번호) -> 0
print(numbers[0])
print(users[-4])

users[-1] = 'Spencer'
print(users)


# delete -> index 
del users[-1]
print(users)
del users[0]
print(users)

del users
print(users)


a = 3
del a
print(a)








