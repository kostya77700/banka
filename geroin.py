uu =[]
q=int(input()) 
uu.append(q)
w = q
kk =input ('хотите продолжить')
while kk =='да':
    q=int(input()) 
    uu.append(q)
    kk =input ('хотите продолжить')
print(uu)
def uiu(uu):
    tt=len(uu)
    for i in range(tt):
        print('*'*uu[i])
uiu(uu)