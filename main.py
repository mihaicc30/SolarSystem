from SolarSystem import tui
import json
import os
# Task 17: Import the modules csv, tui and visual
# TODO: Your code here
from tui import *
from visual import *
import csv

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
# TODO: Your code here
records = []

# i know it is not 100% completed and i am still testing my project, will leave these for now here
categories = {"Planets": [], "Not-Planets": [], "Gravity-Low": [], "Gravity-Medium": [], "Gravity-High": [],
              "meanRadius": []}
summary = {"OrbitedPlanet": {"small": [], "large": []}}


#


def run():
    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    welcome()

    while True:
        menu1 = {1: "Local Data", 2: "Process Data", 3: "Visualise Data", 4: "Save Data", 5: "Exit"}
        menu2 = {1: "Retrieve entity", 2: "Retrieve entity details", 3: "Categorise entities by type",
                 4: "Categorise entities by gravity", 5: "Summarise entities by orbit"}
        menu3 = {1: "Entities by type", 2: "Entities by gravity", 3: "Summary of orbits", 4: "Animate gravities"}
        menu4 = {1: "Export as JSON", 2: "Export as TXT", 3: "Quit"}
        # created these dictionaries to avoid code repetition when starting/completing a task

        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        choice = menu()

        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        # TODO: Your code here
        if choice == 1:
            started(menu1[choice])
            x = source_data_path()
            if x:
                with open(x, "r") as db:
                    csv_reader = csv.reader(db, delimiter=",")
                    head = next(csv_reader)
                    for row in csv_reader:
                        records.append(row)
            completed(menu1[choice])
        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.2
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "small" if the mean radius of the entity is below 100 and "large" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.
        # TODO: Your code here
        elif choice == 2:  # first menu 2nd choice
            started(menu1[choice])
            completed(menu1[choice])
            choice2 = process_type()  # start the submenu
            global categories
            if choice2 == 1:  # 2.1.Retrieve entity
                started(menu2[choice2])
                list_entities()
                completed(menu2[choice2])

            elif choice2 == 2:  # 2.2.Retrieve entities details
                started(menu2[choice2])
                xname, xindex = entity_details()
                list_entity(xname, xindex)
                completed(menu2[choice2])

            elif choice2 == 3:  # 2.3 categorise by type, planet or non planet
                started(menu2[choice2])
                categories["Planets"].clear()
                categories["Not-Planets"].clear()
                for row in records:
                    if row != "eName":
                        if "TRUE" in row:
                            categories["Planets"].append(row[0])
                        else:
                            categories["Not-Planets"].append(row[0])
                print(str(len(categories["Planets"])) + " Planets: ")
                list_categories(categories["Planets"])
                print(str(len(categories["Not-Planets"])) + " Not-Planets: ")
                list_categories(categories["Not-Planets"])
                completed(menu2[choice2])
                #######################
                with open("types.txt", "w") as F:
                    F.write(str(len(categories["Planets"])))
                    F.write("\n")
                    F.write(str(len(categories["Not-Planets"])))
                #################

            elif choice2 == 4:  # 2.4 Categorise entities by gravity
                started(menu2[choice2])
                minn, maxx = gravity_range()
                categories["Gravity-Low"].clear()
                categories["Gravity-Medium"].clear()
                categories["Gravity-High"].clear()
                for row in records:
                    if row[8] != "gravity":
                        if float(row[8]) < minn:
                            categories["Gravity-Low"].append(row[0])
                        elif minn <= float(row[8]) < maxx:
                            categories["Gravity-Medium"].append(row[0])
                        elif float(row[8]) >= maxx:
                            categories["Gravity-High"].append(row[0])
                print(str(len(categories["Gravity-Low"])) + " Low Gravity:")
                list_categories(categories["Gravity-Low"])
                print(str(len(categories["Gravity-Medium"])) + " Medium Gravity:")
                list_categories(categories["Gravity-Medium"])
                print(str(len(categories["Gravity-High"])) + " High Gravity:")
                list_categories(categories["Gravity-High"])
                completed(menu2[choice2])
                #######################
                with open("gravities.txt", "w") as F:  # writing the results to a file which i plan to load in other places
                    F.write(str(len(categories["Gravity-Low"])))
                    F.write("\n")
                    F.write(str(len(categories["Gravity-Medium"])))
                    F.write("\n")
                    F.write(str(len(categories["Gravity-High"])))
                #################

            elif choice2 == 5:  # 2.5 Summarise entities by orbit
                started(menu2[choice2])
                from tui import orbits
                global summary
                to_orbit = tui.orbits()
                for row in records:
                    if row[10] != "meanRadius":
                        if row[0] in to_orbit:
                            if float(row[10]) < 100:
                                summary["OrbitedPlanet"]["small"].append(row[0])
                            else:
                                summary["OrbitedPlanet"]["large"].append(row[0])
                list_categories(summary)
                #######################
                with open("to_orbit.txt", "w") as F:  # writing the results to a file which i plan to load in other places
                    F.write(str(len(summary["OrbitedPlanet"]["small"])))
                    F.write("\n")
                    F.write(str(len(summary["OrbitedPlanet"]["large"])))
                #################
                completed(menu2[choice2])


        # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
        # operation has completed.
        #
        # To visualise the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
        # - Check what option has been selected
        #   - if the user selected the option to visualise the entity type then
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
        #       non-planets.
        #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
        #       and non-planets
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the entity gravity then
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to display a bar chart for the gravities
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
        #       - Use the appropriate function in the module visual to display subplots for the orbits
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has completed.
        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.
        # TODO: Your code here
        elif choice == 3:
            started(menu1[choice])
            completed(menu1[choice])
            choice3 = visualise()  # start the submenu
            if not choice3:
                print(error(choice3))
            else:
                if choice3 == 1:  # Entities by type
                    started(menu3[choice3])
                    entities_pie(categories)
                    completed(menu3[choice3])
                elif choice3 == 2:  # Entities by gravity
                    started(menu3[choice3])
                    entities_bar(categories)
                    completed(menu3[choice3])
                elif choice3 == 3:  # Summary of orbits
                    started(menu3[choice3])
                    from visual import orbits
                    orbits("summary")
                    completed(menu3[choice3])
                elif choice3 == 4:  # Animate gravities
                    started(menu3[choice3])
                    gravity_animation(categories)
                    completed(menu3[choice3])

        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
        #
        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets
        # in alphabetical order.
        # TODO: Your code here

        # i know its not OOP, just needed more time to get here:( sorry
        elif choice == 4:
            started(menu1[choice])
            completed(menu1[choice])

            choice4 = save()
            if choice4 == 1:  # write as json
                started(menu4[choice4])
                file_name = str(input("How would you like to name your file? "))
                x = str(file_name + ".json")
                with open(x, "w") as file:
                    json.dump(records, file)
                completed(menu4[choice4])

            elif choice4 == 2:  # write as txt
                started(menu4[choice4])
                file_name = str(input("How would you like to name your file? "))
                x = str(file_name + ".txt")
                with open(x, "w") as file:
                    file.writelines("%s\n" % item for item in records)
                completed(menu4[choice4])

            elif choice4 == 3:  # quit
                started(menu4[choice4])
                print("Program will now quit the saving menu.")
                completed(menu4[choice4])


        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        # TODO: Your code here
        elif choice == 5:
            print("Program will now exit.")
            break


        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message
        # TODO: Your code here
        else:
            error(choice)
    print("Have a nice day. Thank you for using our service :)")


if __name__ == "__main__":
    run()
