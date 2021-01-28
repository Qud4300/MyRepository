s = input().strip()
L = ''
for i in range(ord('a'),ord('z')+1):
    L += str(s.find(chr(i)))+' '
print(L.strip())
