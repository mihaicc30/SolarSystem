def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # TODO: Your code here
    x = len("Solar Record Management System")
    print(3 * x * "-")
    print(x * "-" + "Solar Record Management System" + x * "-")
    print(3 * x * "-")


def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # TODO: Your code here
    print("""
    Please choose from the following options:
    1. Local Data
    2. Process Data
    3. Visualise Data
    4. Save Data
    5. Exit
    """)

    option = int(input("    Input: "))
    if option > 5 or option < 1:
        print("Sorry, that option is not available. Try again.")
    else:
        return option


def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f"{operation} has \033[0;32mstarted\033[0m.")


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    # TODO: Your code here
    print(f"{operation} has \033[0;33mcompleted\033[0m.")


def error(error_msg):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    # TODO: Your code here
    print("Error! {} not possible.".format(error_msg))


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # TODO: Your code here
    import os.path
    path = str(input("Please enter the file path.\n"))
    if path.endswith(".csv") and os.path.isfile(path):
        return path
    else:
        print("Error! File path is not suitable.")
        return None


def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    option = input("""
    1. Retrieve entity
    2. Retrieve entity details
    3. Categorise entities by type
    4. Categorise entities by gravity
    5. Summarise entities by orbit
    
    Input: """)
    if not option:
        print()
    elif int(option) > 5:
        print("Sorry, that is not an option.")
        return None
    else:
        return int(option)


def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    # TODO: Your code here

    e_name = input("Please enter the name of an entity.\n")
    # print("You have entered the entity", e_name + ".")
    if e_name:
        return e_name
    else:
        return None


def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    # TODO: Your code here
    entity = str(input("Name the entity.\n"))
    entity_index = []
    number_of_indexes_to_see = input("How many indexes you would like to see?\nIndex numbers: ")
    if not number_of_indexes_to_see:
        number_of_indexes_to_see == 0
    else:
        for i in range(int(number_of_indexes_to_see)):
            entity_index.append(int(input("What index would you like to see? ")))
    return [entity, entity_index]


def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # TODO: Your code here

    temp2 = []
    with open(source_data_path()) as file:
        for line in file.readlines():
            if line.startswith(entity):
                temp1 = line.strip().split(",")
                if len(cols) > 0:
                    for elem in cols:
                        temp2.append(temp1[elem])  # if cols is not empty
                else:
                    print(temp1)  # print all entity
                if temp2:
                    print(temp2)  # print the section of the entity


def list_entities():
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    list_entity(str(input("Enter an entity.\n")))


def list_categories():
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # TODO: Your code here
    categories = {"": [], "": []}


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """

    # TODO: Your code here
    min_gravity = float(input("Input min value of gravity: "))
    max_gravity = float(input("Input max value of gravity: "))
    return min_gravity, max_gravity


def orbits():
    """
    Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    # TODO: Your code here
    print("Type 'x' to finish calling entities..")
    to_orbit = []
    while True:
        entities = input("Enter an entity name: ")
        if entities != "x":
            to_orbit.append(entities)
        else:
            return to_orbit


def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    menu = {
        1: "Entities by type",
        2: "Entities by gravity",
        3: "Summary of orbits",
        4: "Animate gravities"
    }
    print("""
      1: Entities by type
      2: Entities by gravity
      3: Summary of orbits
      4: Animate gravities
      """)
    while True:
        for choice in menu:
            choice = int(input("    Input: "))
            if 0 < choice < 5:
                return choice
            else:
                print("Your selection is invalid.")
                return None


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # TODO: Your code here
    while True:
        choice = int(input("""Choose from the following menu 
        how you would like to save your data:

        1. Export as JSON
        2. Export as TXT
        3. Quit
        """))
        if choice == 1:
            file_name = str(input("How would you like to name your file? "))
            x = str(file_name + ".json")
            x = open(x, "w")
            x.close()
            print("Program will now quit.")
            return choice
        elif choice == 2:
            file_name = str(input("How would you like to name your file? "))
            x = str(file_name + ".txt")
            x = open(x, "w")
            x.close()
            print("Program will now quit.")
            return choice
        elif choice == 3:
            print("Program will now quit.")
            break
        else:
            print("You input an invalid option. Try again.")

