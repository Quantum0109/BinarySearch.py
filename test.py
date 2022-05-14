import random 

data = [i for i in range(101)]
data.reverse()

counter = 0
print(data)

while data != sorted(data):
    random.shuffle(data)
    counter += 1
    print(f"список теперь: {data} за {counter} итераций")
    
