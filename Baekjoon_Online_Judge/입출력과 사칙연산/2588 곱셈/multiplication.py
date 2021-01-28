# BOJ 2588 Multiplication

a = int(input())
b = int(input())

print(""+str(a*(b%10))+'\n'+str(a*((b//10)%10))+'\n'+str(a*(b//100))+'\n'+str(a*b))