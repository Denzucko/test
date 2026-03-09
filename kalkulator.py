while True:
    print("Simple calculator")
    calculate = input(">>> ")
    if calculate == "keluar":
        print("Thanks You");
        break
    hasil1 = eval(calculate)
    print(hasil1)