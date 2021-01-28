# BOJ 2941 Croatian Alphabet
com_char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for c in com_char:
    word = word.replace(c, '#')
print(len(word))
