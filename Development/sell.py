from operation import display_data
from read import read_data
import datetime
import os


final_amount = 0


def sell_laptops(billnum):
    # Prompting the user to input customer details
    get_customer_name = input("Please provide the full name of customer:")
    get_customer_contact = input("Please provide the Contact number:")
    get_cumtomer_address = input("Please provide the address:")

    # Checking if the customer details are provided
    if (len(get_customer_name) > 0 and len(get_customer_contact) > 0 and len(get_cumtomer_address) > 0):
        # Calling start function with customer details and bill number
        start(get_customer_name, get_customer_contact,
              get_cumtomer_address, billnum)
    else:
        # Displaying error message and prompting user to press enter to return
        print("!!!!!Please complete all required fields!!!!!")
        input("Press enter to return")


def details(get_customer_name, get_cumtomer_address, get_customer_contact, ID, billnum):
    # read data from the file
    data = read_data()

    # get desired quantity from the user
    quantity = input("Enter the desired number of laptops:")

    # check if the desired quantity is available
    if (int(data[int(ID)][3]) - int(quantity)) >= 0 and int(quantity) > 0:
        # if the quantity is available, generate sales bill, update the stock and continue to another sale
        salesBill(get_customer_name, get_cumtomer_address,
                  get_customer_contact, ID, quantity, billnum)
        update(ID, quantity)
        again(get_customer_name, get_cumtomer_address,
              get_customer_contact, billnum)
    else:
        # if the quantity is not available, inform the user and return to the main menu
        print("The selected laptop is out of stock")
        input("Press Enter")
        start()


def salesBill(get_customer_name, get_cumtomer_address, get_customer_contact, ID, quantity, billnum):

    # Read laptop data from file
    data = read_data()

    # Get current date and time
    date_time = datetime.datetime.now()

    # Calculate total cost of purchased laptops
    amount = data[int(ID)][2].replace("$", "")
    total_cost = float(amount)*int(quantity)

    # Calculate shipping cost and total cost after shipping
    shipping_amount = "15%"
    amount_after_shipping = total_cost+(total_cost*0.15)

    # Update global variable to keep track of final amount
    global final_amount
    final_amount += amount_after_shipping

    # Write sales bill to file
    if (os.path.exists(get_customer_name+billnum+"-bill.txt")):
        # If the sales bill file already exists, append the new sales information to it
        with open(get_customer_name + billnum + "-bill.txt", "a") as file:
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
\t \t \t             Shipping Cost={shipping_amount}               
|------------------------------------------------------------------------------------------------| 
\t \t \t             Total Cost (without shipping cost)=${total_cost}   
|------------------------------------------------------------------------------------------------| 
\t \t \t             Total Cost=${amount_after_shipping}   
*************************************************************************************************
            """)
    else:
        # If the sales bill file does not exist, create a new file and write the sales information to it
        with open(get_customer_name + billnum + "-bill.txt", "w") as file:
            file.write(f"""
                     Customer Name = {get_customer_name}
                     Customer Contact = {get_cumtomer_address}
                     Customer Address = {get_customer_contact}
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
\t \t \t             Shipping Cost={shipping_amount}               
|------------------------------------------------------------------------------------------------| 
\t \t \t             Total Cost (without shipping cost)=${total_cost}   
|------------------------------------------------------------------------------------------------| 
\t \t \t             Total Cost=${amount_after_shipping}   
*************************************************************************************************   

            """)


def start(get_customer_name, get_cumtomer_address, get_customer_contact, billnum):
    # read data from file
    data = read_data()

    # display list of laptops
    display_data()

    try:
        # get user choice
        print("Enter 99 to return to  menu")
        print("Choose ID no 1-5 to select your desired option")
        choice = input("Please select your option: ")

        # check if choice is valid
        if choice == "99":
            return None
        elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(data):
            print("Please enter a valid option.")
            input("Press enter to continue")
            start(get_customer_name, get_cumtomer_address,
                  get_customer_contact, billnum)
        else:
            # convert choice to index of selected laptop
            index = int(choice) - 1

            # proceed to get laptop details and generate bill
            details(get_customer_name, get_cumtomer_address,
                    get_customer_contact, index, billnum)

    except Exception as e:
        print("An error occurred: ", e)
        input("Press enter to continue")
        start(get_customer_name, get_cumtomer_address,
              get_customer_contact, billnum)


def final_Amount(get_customer_name, billnum):
    global final_amount
    with open(get_customer_name + billnum + "-bill.txt", "a") as file:
        file.write(f"""
**********************************

Final Amount = {final_amount}

**********************************

        """)


final_amount = 0


def update(ID, quantity):
    # open the laptops.txt file in read mode
    with open("laptops.txt", "r") as file:
        # read the file and store the data in a list of lists
        data = [line.strip().split(",") for line in file]

    # update the quantity of the laptop with the given ID
    data[int(ID)][3] = str(int(data[int(ID)][3]) - int(quantity))

    # open the laptops.txt file in write mode
    with open("laptops.txt", "w") as file:
        # write the updated data to the file, joining each list into a string and adding a newline character at the end
        for line in data:
            file.write(",".join(line) + "\n")


def again(get_customer_name, get_cumtomer_address, get_customer_contact, billnum):
    print(f"""
╭───────────────────────────────╮
│        What would you like    │
│             to do?            │
├───────────────────────────────┤
│                               │
│ 1. Place a new order          │
│                               │
│ 2. Checkout                   │
│                               │
╰───────────────────────────────╯

    """)
    choice = input("pick 1 or 2:")
    if (choice == "1"):
        # if the user selects option 1, call the start function with the relevant parameters
        start(get_customer_name, get_cumtomer_address,
              get_customer_contact, billnum)
    elif (choice == "2"):
        # if the user selects option 2, print a success message and call the final_Amount function with the relevant parameters
        print("Your purchase has been successfull!!!")
        final_Amount(get_customer_name, billnum)
        # open the bill file and print its contents to the console
        with open(get_customer_name + billnum + "-bill.txt", "r")as bill:
            print(bill.read())
            # prompt the user to press enter to return to the main menu
        input("Press enter to return back")
    else:
        # if the user enters an invalid choice, print an error message and call the again function with the relevant parameters
        print("You are requested to enter properly!!")
        print("Press enter to return back")
        again(get_customer_name, get_cumtomer_address,
              get_customer_contact, billnum)
