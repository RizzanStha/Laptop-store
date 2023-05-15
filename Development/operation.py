from read import read_data


def display_data():
    # initialize an empty list to store the data
    data = []
    print('                          The options of laptops are loading...')
    print(' ─────────────────────────────────────────────────────────────────────────────────────────────────────────')
    print('|  ID  || Name              || Brand           || Price       || Quantity || Processor  || Graphics Card ||')
    print(' ─────────────────────────────────────────────────────────────────────────────────────────────────────────')
    # read the data from the file and store it in the list
    data = read_data()
    # iterate over the list and print each element in the table format
    for i in range(len(data)):
        element = data[i]
        print('|', str(i+1).ljust(5),
              '||', element[0].ljust(18),
              '||', element[1].ljust(18),
              '||', element[2].ljust(10),
              '||', element[3].ljust(10),
              '||', element[4].ljust(10),
              '||', element[5].ljust(10), '||')
        print(' ─────────────────────────────────────────────────────────────────────────────────────────────────────────')
