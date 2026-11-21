names = []

while True:
    n = input("Name (done to stop): ")
    names.append(n)
    if n == "done":
        break

print(names)
print(len(names), " names stored")