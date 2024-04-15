file = open(r'C:\Users\okanl\OneDrive\Documents\Python\president_height.csv', mode = 'rt')
# print(file.read())
file_list = file.readlines()
print(file_list)
file_list.pop(0)
print(file_list)
names = []
heights = []
for line in file_list:
    print(line)
    val = line.split(',')
    print(val)

    height = int(val[2].strip('\n'))
    print(height)
    heights.append(height)
    names.append(val[1])

print(heights)
print(names)
max_height = max(heights)
index_max_height = heights.index(max_height)
print(index_max_height)
print(names[index_max_height])

# max_height = (0)
# x = 0
# for x in range(3):
#     for each in heights:
#         heights > max_height
#         max_height = heights
#         print ('max_height')
#         x + 1
