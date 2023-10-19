N=int(input("entrer  le nbre des note  en total"))
T=[]
T1=[]
M=0
for i  in range(N):
    A=int(input("entrer les notes"))
    M=M+A
    T.append(A)
for i in range (N):
    if T[i]>(M/N):
        T1.append(T[i])
print(T1)



