scurs = []
total = 0
for i in range(5):
    scur = int(input("Score: "))
    scurs.append(scur)
for t in scurs:
    total = total + t
print("Total:", total)
print("Average:", total / 5)