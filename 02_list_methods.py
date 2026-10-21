freinds = ["apple","orange",5,345.06,False,"aakash","rohan"]
print(freinds)
freinds.append("harry")
print(freinds)

numbers = [1,34,62,2,6,11]
numbers.sort()
print(numbers)


numbers = [1,34,62,2,6,11]
#numbers.sort()
numbers.reverse()
print(numbers)

numbers = [1,34,62,2,6,11]
#numbers.sort()
#numbers.reverse()
numbers.insert(6,8888)#insert 8888 such that its index in the list is 6
print(numbers)


numbers = [1,34,62,2,6,11]
value =numbers.pop(3)
print(value)
print(numbers)

numbers = [1,34,62,2,6,11]
numbers.remove(2)
print(numbers)