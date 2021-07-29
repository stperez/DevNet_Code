# Paso 4: Desafío: Cree un script para permitir al usuario agregar dispositivos. pdf python module 1
from colorama import init, Fore

init(autoreset=True)


# function for add devices
def funcname():
    info = print(Fore.RED +
                 "If you don't want to add more devices, type 'exit'")
    while True:
        try:
            # input for device info
            add_device = input("type the device info > \n")

            # add devices to devices.txt
            if add_device != "exit" and "read":
                with open('devices.txt', 'a') as file:
                    file.write(f'{add_device}\n')
                    file.close()

            # exit the prompt
            if add_device == "exit":
                print("All Done!.\n")
                break

        except Exception:
            print("you has been press other command")


# function for read devices.txt
def read_devices():
    try:
        read = input(
            Fore.CYAN +
            "If you want see the devices list type 'r' or 'q' for exit > ")

        # read file
        if read == "r":
            with open('devices.txt', 'r') as read:
                item = read.read()
                item.strip()
                item.split()
                print(item)
        # exit
        else:
            read == "q"
            print("All Done!.")

    except Exception:
        print("[!] has an error")


# call the functions
funcname()  # add devices
read_devices()  # read devices
