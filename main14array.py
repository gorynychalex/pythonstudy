# Поиск в массиве

nX = -1

A = [1,2,3,4,5]
N=len(A)
X=3
for i in range(N):
    if A[i] == X:
        nX=i
        break
if nX>=0:
    print("A[",nX,"]=",X,sep="")
else:
    print("Не найден!")
