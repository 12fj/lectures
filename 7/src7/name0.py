# Reformats "last, first" as "first last"

name = input("Name: ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
