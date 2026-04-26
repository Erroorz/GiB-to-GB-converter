# easily convert between gigbytes and gigabytes :3

bytes = 0
bytes2 = 0
print("********************")
print("Convert data to Gib")
print("********************")
print("1. convert Gb to Gib")
print("2. convert Gib to Gb")
print("********************")

choice = int(input("Choose the conversion rate: "))

if choice == 1:
    fir_uchoice = input("Type first data type (kB,MB,GB,TB,PB): ")
    b_amount = float(input(f"How many {fir_uchoice} would you like to convert:"))
    
    if fir_uchoice == "kB":
        bytes = 1000
    elif fir_uchoice == "MB":
        bytes = 1000000
    elif fir_uchoice == "GB":
        bytes = 1000000000
    elif fir_uchoice == "TB":
        bytes = 1000000000000
    elif fir_uchoice == "PB":
        bytes = 1000000000000000
    else:
        print("Invalid data type")
        exit()

    total_bytes = b_amount * bytes

    print("************************")
    sec_uchoice = input("Type second data type (KiB,MiB,GiB,TiB,PiB): ")
    
    if sec_uchoice == "KiB":
        bytes2 = 1024
    elif sec_uchoice == "MiB":
        bytes2 = 1048576
    elif sec_uchoice == "GiB":
        bytes2 = 1073741824
    elif sec_uchoice == "TiB":
        bytes2 = 1099511627776
    elif sec_uchoice == "PiB":
        bytes2 = 1125899906842620
    else:
        print("Invalid data type")
        exit()
    
    conversion = total_bytes/bytes2

    print(f"{b_amount} {fir_uchoice} is equal to {conversion:.3f} {sec_uchoice}")

if choice == 2:
    fir_uchoice = input("Type first data type (KiB,MiB,GiB,TiB,PiB): ")
    b_amount = float(input(f"How many {fir_uchoice} would you like to convert: "))
     
    if fir_uchoice == "KiB":
        bytes = 1024
    elif fir_uchoice == "MIB":
        bytes = 1048576
    elif fir_uchoice == "GiB":
        bytes = 1073741824
    elif fir_uchoice == "TiB":
        bytes = 1099511627776
    elif fir_uchoice == "PiB":
        bytes = 1125899906842620
    else:
        print("Invalid data type")
        exit()
    
    total_bytes = b_amount * bytes

    print("************************")
    sec_uchoice = input("Type second data type (kB,MB,GB,TB,PB): ")
    
    if sec_uchoice == "kB":
            bytes2 = 1000
    elif sec_uchoice == "MB":
            bytes2 = 1000000
    elif sec_uchoice == "GB":
            bytes2 = 1000000000
    elif sec_uchoice == "TB":
            bytes2 = 1000000000000
    elif sec_uchoice == "PB":
            bytes2 = 1000000000000000
    else:
        print("Invalid data type")
        exit()
    conversion = (b_amount * bytes)/bytes2

    print(f"{b_amount} {fir_uchoice} is equal to {conversion:.3f} {sec_uchoice}")
