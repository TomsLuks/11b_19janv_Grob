vards = input("Ievadi savu vārdu: ")

try:
    with open("vards.txt", "w") as f:
        f.write(vards)
except (FileExistsError, ValueError):
    print("Error: Fails jau pastāv vai ievade nav derīga!")
with open("vards.txt", "r") as f:
    name = f.read()

print("Sveiks, " + vards + "!")