Input:
n=int(input("enter the total number of terms: "))
x=0
y=1
for i in range(n):
    print(x)
    z=x
    x=y
    y=z+y
Output:
enter the total numbers of terms: 15
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
