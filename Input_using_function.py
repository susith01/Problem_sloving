Name_superhero=input()
age=int(input())
height=float(input())
print(Name_superhero,"is secretly a superhero")
print(Name_superhero,"is",age,"years old")
print(Name_superhero,"is",height,"m","tall")
def get_superhero():
    name = input("Name: ")
    age = int(input("Age: "))
    height = float(input("Height (m): "))

    return name, age, height


def display_profile(name, age, height):
    print(f"\n{name} is secretly a superhero.")
    print(f"Age    : {age}")
    print(f"Height : {height} m")


def main():
    name, age, height = get_superhero()
    display_profile(name, age, height)


if __name__ == "__main__":
    main()