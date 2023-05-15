def read_data():
    # Open the file "laptops.txt" in read mode using a context manager
    with open("laptops.txt", "r") as file:
        # Read all lines of the file and store them as a list of strings
        values = file.readlines()
    
    # Create an empty list to store the parsed data
    data = []
    # Iterate over each string in the list of lines
    for value in values:
        # Remove any trailing whitespace and split the string by commas
        # to create a list of values
        parsed_values = value.rstrip().split(",")
        # Append the list of parsed values to the data list
        data.append(parsed_values)
    
    # Return the complete list of parsed data
    return data
