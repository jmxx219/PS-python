alpha = ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']
string = input()

for i in alpha:
    string = string.replace(i, '*')
print(len(string))
