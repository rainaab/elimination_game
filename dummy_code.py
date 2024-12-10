file = open('hungry_caterpillar.txt')
rhyme = file.read().splitlines()

k = 3
current = 0
print (rhyme)
# -1 so its at the right index
current = (k-current)-1
print(current)
rhyme.pop(current)
print ("new list",rhyme)
current = ((current + k) - len(rhyme)) - 1
print (rhyme[current])
rhyme.pop(current)
print(rhyme)
print(rhyme[current])
print("need",current)
current = (k-current) - 1
print("zero current",current)
rhyme.pop(current)
print(rhyme)
current = (k-current) - 1
rhyme.pop(current)
print(rhyme)

# print("num", current)
# print(rhyme[])
# current = ((current + k) - len(rhyme)) - 1
# rhyme.pop(current)
# print("final",rhyme)
# print (rhyme[current])
# rhyme.pop(current)
# print(rhyme)
# print(current)
# print (rhyme[current])

# print("new iteration")
# current = ((current + k) - len(rhyme)) - 1
# rhyme.pop(current)
# print(rhyme)
# print(rhyme[current])

# print("new iteration")
# current = ((current + k) - len(rhyme)) - 1
# rhyme.pop(current)
# print(rhyme)
# print(rhyme[current])

# print("length",len(rhyme))
# print("list:",rhyme)


# current = ((current + k) - len(rhyme)) 
# print(current)
# # rhyme.pop(current)
# # print("final",rhyme)
# # print(rhyme[current])