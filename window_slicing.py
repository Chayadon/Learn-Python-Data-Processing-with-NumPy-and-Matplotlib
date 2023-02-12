from numpy.random import default_rng

rng = default_rng()

num = rng.integers(low=0, high=100, endpoint=True,size=7)
print(num)

ws = 3
for i in range(0,len(num) - ws + 1 ):
    for j in range(i ,i + ws):
        print(num[j],end=" ")
    print("")


