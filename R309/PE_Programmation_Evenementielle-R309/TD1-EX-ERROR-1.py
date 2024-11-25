#EXERCICE 1
def divEntier(x: int, y: int) -> int:
    try:
        if x < y:
            return 0
        else:
            x = x - y
            return divEntier(x, y) + 1
    except ValueError as erreur:
        print(f"Enter a valid value for x and y (int) / {erreur}")
    except ZeroDivisionError as erreur:
        print(f"Enter a valid value for x and y (no 0) / {erreur}")

if __name__ == '__main__':   
    try:
        x = int(input("Enter a value for x : "))
        y = int(input("Enter a value for y : "))
        print(divEntier(x, y))
    except ValueError as erreur:
        print(f"Enter a valid value for x and y (int) / {erreur}")
    except ZeroDivisionError as erreur:
        print(f"Enter a valid value for x and y (no 0) / {erreur}")
