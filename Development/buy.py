from read import read_data
import datetime
import os


final_amount = 0



def buy_laptops(billnum):
    # Prompting the user to input customer details
    get_provider_name = input("Please provide the full name of provider:")
    get_provider_contact = input("Please provide the Contact numberr:")
    get_provider_address = input("Please provide the address:")

    # Checkibf if the customer details are provided
    if (len(get_provider_name) > 0 and len(get_provider_contact) > 0 and len(get_provider_address) > 0):
        # Calling start function with customer details and bill number
        start(get_provider_name, get_provider_contact,
              get_provider_address, billnum)
    else:
        
        print("!!!!!Please complete all required fields!!!!!")
        input("Press enter to return")


def start(get_provider_name, get_provider_address, get_provider_contact, billnum):
    data = read_data()
    print("╭──────────────────────────────╮")
    print("│       SELECT AN OPTION       │")
    print("├──────────────────────────────┤")
    print("│                              │")
    print("│ 1. Razer Blade               │")
    print("│                              │")
    print("│ 2. XPS                       │")
    print("│                              │")
    print("│ 3. Alienware                 │")
    print("│                              │")
    print("│ 4. Swift 7                   │")
    print("│                              │")
    print("│ 5. MacBook Pro 16            │")
    print("│                              │")
    print("╰──────────────────────────────╯")

    try:
        # prompt user to select an option or return to menu
        print("Enter 99 to return to main menu")
        print("Choose ID no 1-5 to select your desired option")
        choice = input("Please select your option :")
        # Loop thorugh the data to check if user's coice matches the number
        for i in range(len(data)):
            if (int(choice) == i+1):
                # If the user's choice matches an number, pass the provider details,
                details(get_provider_name, get_provider_address,
                        get_provider_contact, i, billnum)
            if (choice == "99"):
                # If the user enters 99, return None to go back to th emenu
                return None
            if (choice > str(len(data)) or choice < "0"):
                # If the user enter an invalid choice, prompt them to enter their choice again and restart the function
                print("You are requested to enter your choice properly")
                input("Press enter")
                start(get_provider_name, get_provider_address,
                      get_provider_contact, billnum)
    except:
        # If there is an error with the user's input, prompt them to enter their choice again an drestart the function
        if (choice > str(len(data)) or choice < "0"):
            print("You are requested to enter your choice properly")
            input("Press enter")
            start(get_provider_name, get_provider_address,
                  get_provider_contact, billnum)


def VATBill(get_provider_name, get_provider_address, get_provider_contact, ID, quantity, billnum):

    data = read_data()
    date_time = datetime.datetime.now()
    amount = data[int(ID)][2].replace("$", "")
    total_cost = float(amount)*int(quantity)
    VAT_Percent = "13%"
    amount_after_VAT = total_cost+(0.13*total_cost)
    global final_amount
    final_amount += amount_after_VAT
    if (os.path.exists(get_provider_name+billnum+"-bill.txt")):
        with open(get_provider_name + billnum + "-bill.txt", "a") as file:
            file.write(f"""
*************************************************************************************************
\t \t \t             Laptop Name={data[int(ID)][0]}   
|------------------------------------------------------------------------------------------------|
\t \t \t             Brand={data[int(ID)][1]}      
|------------------------------------------------------------------------------------------------|
\t \t \t             Price={data[int(ID)][2]}    
|------------------------------------------------------------------------------------------------|
\t \t \t             Quantity={quantity}     
|------------------------------------------------------------------------------------------------|
\t \t \t            VAT={VAT_Percent} 
|------------------------------------------------------------------------------------------------|
\t \t \t             Total Cost (without VAT )=${total_cost} 
|------------------------------------------------------------------------------------------------|
\t \t \t             Total Cost=${amount_after_VAT}
*************************************************************************************************        

            """)
    else:
        with open(get_provider_name + billnum + "-bill.txt", "w") as file:
            file.write(f"""
                     Buyer Name = {get_provider_name}
                     Buyer contact = {get_provider_address}
                     Buyer address = {get_provider_contact}
                     Selling Date and Time ={date_time.strftime("%d-%m-%Y")}
*************************************************************************************************
\t \t \t             Laptop Name={data[int(ID)][0]}   
|------------------------------------------------------------------------------------------------|
\t \t \t             Brand={data[int(ID)][1]}      
|------------------------------------------------------------------------------------------------|
\t \t \t             Price={data[int(ID)][2]}    
|------------------------------------------------------------------------------------------------|
\t \t \t             Quantity={quantity}     
|------------------------------------------------------------------------------------------------|
\t \t \t             VAT={VAT_Percent} 
|------------------------------------------------------------------------------------------------|
\t \t \t             Total Cost (without VAT )=${total_cost} 
|------------------------------------------------------------------------------------------------|
\t \t \t             Total Cost=${amount_after_VAT}
*************************************************************************************************      

            """)


def details(get_provider_name, get_provider_address, get_provider_contact, ID, billnum):
    # Prompt user to input desired quantity of laptops
    quantity = input("Enter the desired number of laptops:")

    # Generate VAT bill for the customer and update laptop quantity
    VATBill(get_provider_name, get_provider_address, get_provider_contact, ID, quantity, billnum)
    update(ID, quantity)

    # Ask user if they want to make another purchase or return to the main menu
    again(get_provider_name, get_provider_address, get_provider_contact, billnum)


def final_Amount(get_provider_name, billnum):
    global final_amount  # Access the global variable final_amount
    with open(get_provider_name + billnum + "-bill.txt", "a") as file:  # Open the bill file in append mode
        file.write(f"""  # Write the final amount to the bill file
*********************************

Final Amount = {final_amount}

*********************************

        """)  # End of the string to write to the file



final_amount = 0


def update(ID, quantity):
    # Read the data from file into a list of lists
    data = read_data()

    # Update the quantity of the selected laptop
    current_quantity = int(data[int(ID)][3])
    new_quantity = current_quantity + int(quantity)
    data[int(ID)][3] = str(new_quantity)

    # Write the updated data back to file
    with open("laptops.txt", "w") as file:
        for line in data:
            # Convert the line list to a comma-separated string
            line_str = ",".join(line)
            # Write the line string to file and add a newline character
            file.write(line_str + "\n")



def again(get_provider_name, get_provider_address, get_provider_contact, billnum):
    print(f"""
╭───────────────────────────────╮
│        What would you like    │
│             to do?            │
├───────────────────────────────┤
│                               │
│ 1. Place a new order          │
│                               │
│ 2. checkout                   │
│                               │
╰───────────────────────────────╯
    """)
    choice = input("please choose either 1 or 2:")
    if (choice == "1"):
        start(get_provider_name, get_provider_address,
              get_provider_contact, billnum)
    elif (choice == "2"):

        print("Your purchase has been successfull!!!")
        final_Amount(get_provider_name, billnum)
        with open(get_provider_name + billnum + "-bill.txt", "r")as bill:
            print(bill.read())
        input("Press enter to return back")
    else:
        print("You are requested to enter properly!!")
        print("Press enter to return back")
        again(get_provider_name, get_provider_address,
              get_provider_contact, billnum)
