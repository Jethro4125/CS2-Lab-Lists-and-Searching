skert = []
count = 0
for i in range(5):
    scur = int(input("Score: "))
    skert.append(scur)
for U in skert:
    if U >= 75:
        count = count + 1
print(count, "of 5 passed")