while True:
    print("Simple calculator")
    calculate = input(">>> ")
    if calculate == "keluar":
        print("Thanks You");
        break
    hasil = eval(calculate)
    print(hasil)