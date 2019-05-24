# Recap 7
# Lists

rappers = ["Nas", "Rakim", "MF DOOM", "Mos Def", "Killer Mike", "DMX"]
print(rappers)
print(rappers[-1])
print(rappers[-4])
print(rappers[1:4])

# Inserts 'Tupac' in the 2nd index
rappers[2] = "Tupac"
print(rappers)
print("*" * 36)

# 2D lists
twoDList = """
2, 4, 9
1, 5, 1
7, 6, 0 
"""
# print(twoDList)
matrix = [[2, 4, 9], [1, 5, 1], [7, 6, 0]]
print(f"{matrix[0][1]} {matrix[0][0]} {matrix[2][2]}")
print("*" * 36)

# Going through each item inside the 2D list
for row in matrix:
    for item in row:
        if item == 4:
            a = item
        elif item == 2:
            b = item
        elif item == 0:
            c = item
print(f"{a} {b} {c} Blaze It!!!")
print("*" * 36)

new_list = [5, 3, 7, 2, 9]

# Appending a number
new_list.append(13)
print(new_list)

# Insert a number in a specific index
new_list.insert(3, 420)
print(new_list)

# Remove the objects inside the list with clear
new_list.clear()
print(new_list)
new_list = [23, 9, 4, 3, 56, 21]

# Remove the last item in the list
new_list.pop()
print(new_list)

# Index Method
x = new_list.index(56)
y = new_list.index(4)
z = new_list.index(23)
print(f"Index of 56: {x}\nIndex of 4: {y}\nIndex of 23: {z}")

# Sorting a list in ascending order
new_list.sort()
print(new_list)

# Sorting the list in descending order
new_list.reverse()
print(new_list)

# Copying the list (copy method)
numbers_copy = new_list.copy()
numbers_copy.insert(2, 420)
print(f"The copy: {numbers_copy}")
print(f"The original: {new_list}")
print("*" * 36)

# Remove the duplicates in a list
sad_cafe = [43, 98, 23, 21, 666, 23, 21, 7, 34, 9]
uniques = []
for sad_person in sad_cafe:
    if sad_person not in uniques:
        uniques.append(sad_person)
uniques.sort()
print(uniques)
