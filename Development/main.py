from operation import display_data
from buy import buy_laptops
from sell import sell_laptops
print("""
                                                
██████╗ ██╗███████╗███████╗    ██╗      █████╗ ██████╗ ████████╗ ██████╗ ██████╗     ███████╗████████╗ ██████╗ ██████╗ ███████╗███████╗
██╔══██╗██║╚══███╔╝██╔════╝    ██║     ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██║  ███╔╝ ███████╗    ██║     ███████║██████╔╝   ██║   ██║   ██║██████╔╝    ███████╗   ██║   ██║   ██║██████╔╝█████╗  ███████╗
██╔══██╗██║ ███╔╝  ╚════██║    ██║     ██╔══██║██╔═══╝    ██║   ██║   ██║██╔═══╝     ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝  ╚════██║
██║  ██║██║███████╗███████║    ███████╗██║  ██║██║        ██║   ╚██████╔╝██║         ███████║   ██║   ╚██████╔╝██║  ██║███████╗███████║
╚═╝  ╚═╝╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝         ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                                                            
    """)
while True:
    try:
        print('''
                               ╔══════════════════════════════════════════════════╗
                               ║               select the option                  ║
                               ╠══════════════════════════════════════════════════╣
                               ║   [1] Display Available Products                 ║
                               ║   [2] Sell to customer                           ║
                               ║   [3] Purchase From Supplier                     ║
                               ║                                                  ║
                               ║   [9] Exit                                       ║
                               ╚══════════════════════════════════════════════════╝
    ''')
        n = int(input('Select an option from the above: '))
        # Perform the selected action based on the user's input
        if n == 1:
            # Display the list of laptops
            display_data()
            input("Please press Enter to continue...")
        elif n == 2:
            # Sell laptops
            with open("billnum.txt", "r") as bill:
                billnum = bill.read()
            sell_laptops(billnum)
            with open("billnum.txt", "w") as bill:
                bill.write(str(int(billnum)+1))
        elif n == 3:
            # Buy laptops
            with open("billnum.txt", "r") as billnum:
                billnum = billnum.read()
            buy_laptops(billnum)
            with open("billnum.txt", "w") as billnum:
                billnum.write(str(int(billnum)+1))
        elif n == 9:
            # Exit the program
            print("""
                EXITING............
                Thank you for your visit. Have a great day!

                """)
            break
        else:
            # If the user enters an invalid option, prompt them to select an option properly
            print("Please Select The Option Properly")
    except:
        # If the user enters an invalid input, prompt them to select an option properly
        print("Please select the option properly")
        input("Press Enter")
