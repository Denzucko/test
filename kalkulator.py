while True:
    print("Simple calculator")
    calculate = input(">>> ")
    if calculate == "keluar":
        print("Thanks You");
        break
    hasil123 = eval(calculate)
    print(hasil123)