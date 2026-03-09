while True:
    print("Simple calculator")
    calculate = input(">>> ")
    if calculate == "keluar":
        print("Thanks You");
        break
    hasil12 = eval(calculate)
    print(hasil12)