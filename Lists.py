"""names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:4])
for i in range(5):
    print(names[i])
names[0] = 'Jon'
print(names[0])

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for i in numbers:
    if max <= i:
        max = i

print(max)"""


"""matrix = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
print(matrix[0][1])

for i in matrix:
    for j in i:
        print(j)"""

"""numbers = [5, 2, 1, 7, 4, 2, 5]
numbers2 = numbers.copy()
numbers.append(13)
numbers.insert(2, 20)
numbers.remove(2)
# numberd.clear()
numbers.pop()
print(numbers.index(20))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers2)"""

numbers = [10,15,6,2,4,7,2,1,5,8,5,4,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)