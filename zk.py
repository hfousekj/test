A = [1, 4, 10]

# poradi = 0
#
#
# vysledek = []
#
# #for i in range(0, len(A)):
#
# for i in A:
#     #print(i)
#     if poradi < len(A):
#         vysledek[poradi+1].append(A[poradi])
#
#     elif poradi == len(A):
#          vysledek[poradi+1].append(A[poradi])
#     poradi += 1
#

vysledek = []

#for i in range(0, len(A)):

for i in A:
    #print(i)

    if A.index(i) == len(A):
        vysledek[0].append(A[A.index(i)])
    
    else:
        vysledek[A.index(i) + 1].append(A[A.index(i)])


print(vysledek)

#
#
# for i in range(0, len(A)):
#
#     if poradi == len(A):
#         A[0] = A[poradi]
#
#     elif poradi >= len(A):
#         A[i + 1] = A[i]
#     poradi = poradi + 1
#
# print(A)