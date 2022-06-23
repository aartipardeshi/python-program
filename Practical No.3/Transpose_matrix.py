#Find transpose of matrix

A=[[3,4,2],
   [6,2,1],
   ]
result=[[0,0],
        [0,0],
        [0,0]]

for a in range(len(A)):
    for b in range(len(A[0])):
        result[b][a]=A[a][b];

print("The Transpose of matrix:");
for r in result:
    print(r);
