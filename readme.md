# Welcome To CodeBuddy!
This code is designed to help T1D camps monitor multiple dexcom users at once. Goal is to be deployed in early June

## To-Do
1. Create Classes
*Each CampBuddy Object contains a list of camper objects and one report object. Each camper contains a status object*

    a. Camper Class

        - Member objects

            - Dexcom username

            - Dexcom password

            - Name

            - dexcom obj

            - data_missing_time (int)

            - low

            - high

            - 4am (bool)

            - 12am (bool)

        - Functions

            - init()

                - arguments

                    - Dexcom username

                    - Dexcom password


                    - Name (string as "first last")
                    - low

                    - high

                - methods

                    - calls create_dexcom()

            - create_dexcom()

                - Creates dexcom obj

            - get_status()

                - methods

                    - Pulls dexcom data from the dex obj for the last 20 minutes

                    - Checks to see if data is missing and for how long

                        - passes time missing to status object

                    - Uses data to return Status obj

    b. CampBuddy Class

        - Member objects

            - Campers = list of camper objs

            - Camper_file = string to file path

            - Low alert (int)

            - High alert (int)

            - Night (bool)

            - Alert_string = formatted string with alert text

        - Functions

            - init()

                - arguements

                    - camper_file = path to camper file

                    - low = low alert

                    - high = high alert

                    - night = bool

                - methods

                    - calls create_camper_list()

            - create_camper_list()

                - arguments

                    - path to camper file

                - methods

                    - parse file and create camper list

            - night_report()

                - methods

                    - iterate through each camper and get their status

                    - sort into low, high, DE, 4AM, 12AM lists

                    - call generate_report()

                - returns

                    - report object from generate_report()

            - day_report()

                - methods

                    - iterate through each camper and get their status

                    - sort into low, high, DE lists

                    - call generate_report() (pass NA into 4AM/12AM)

            - generate_report()

                - arguments

                    - low list

                    - high list

                    - DE list

                    - 4AM list

                    - 12AM list

                    - number_stable

                    - number_reported

                - methods

                    - sort through lists and build report object

                    - return report object

                - returns

                    - formatted report object

    c. Status Class

        - Member objects

            - status_string = "LOW" "HIGH" "STABLE" "DATAERROR"

            - bgvs = [bg, bg, bg, bg]

        - Functions

            - .init()

                - arguments

                    - bgvs = list of available bgvs

                    - status_string = "LOW" "HIGH" "STABLE" "DATAERROR"

    d. Report Class

        - Member objects

            - low list

            - high list

            - DE list

            - 4AM list

            - 12AM list

            - report_string

            - message_string

        - functions

            - init()

                - pass in all lists

            - generate_report_string()

                - methods

                    - format and return a string for use in the graphical interface

                - returns

                    - formatted string

            - generate_pushover_string

                - methods

                    - format and return a string for use in the pushover API

                - returns

                    - formatted string

    e. PushOverManager

        - Member objects

            - TokenDict = {"id":"token"}

        - Functions

            - init()

                - arguments

                    - pathToFile = string path to file

                - methods

                    - call buildDict() and assign completed dict to TokenDict

            - buildDict()
                - arguments 
                    - pathToFile
                - methods
                    - Open and parse file to create dict
                    - assign dict to member variable
            - sendMessage()
                - arguments
                    - message_string = string to send
                    - id = string identifier 
                - methods
                    - use id and message_string to send string


2. Create Main Function

    a. Functionality phase

        - Hardcode necessary values

            - refresh rate

            - file paths

            - low and high values

            - files with limited data

                - actual dexcom data

                - dummy pushover accounts

        - Create looping function

            - call day_report every *refresh rate* seconds

            - print (via report class) and send message (via pushover) to test pushover

    b. graphical phase

        - create python gui

            - get variables via gui

                - refresh rate

                - file paths

                - low and high values

                - day/night toggle

        - web server via flask (automatically refreshes according to refresh rate)

            - basic web app 

                - order top to bottom

                    - small banner

                    - report text

                    - 3 buttons 

                        - push activity

                            - sends current report to specific activity selected from drop down menu

                        - push cabin

                            - sends current report to specific cabin selected from drop down menu

                        - refresh
                        
                            - force refresh regardless of refresh rate variable

        

