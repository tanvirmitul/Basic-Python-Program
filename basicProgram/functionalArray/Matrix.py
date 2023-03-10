matrix=[
    [1,2,3],
    [4,5,6],
]
# for r in matrix:
#     for c in r:
#         print(c)
i=0
j=0
while i<len(matrix):
    while j<len(matrix):
        print(matrix[j])
        j=j+1
    i=i+1