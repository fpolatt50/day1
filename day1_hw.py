for x in range(5):
    a = input("Enter Value:  ")
    try:
        val = int(a)
        print("Input is an integer number ", val)
    except ValueError:
        try:
            val = float(a)
            print("Input is a float ", val)
        except ValueError:
            print("It's a string")