def Main():                                                                                                                                                                                                             # Define Main Method, run program functions in straight linear
    ProgramOne()
    ProgramTwo()
    ProgramThree()

def ProgramOne():
    integerList = []

    def DoMath():                                                                                                                                                                                                       # Define Function to calculate Program 1 Basic Math
        localIntegerListSum = sum(integerList)                                                                                                                                                                          # Uses Sum function to add all entries in integer list
        localIntegerListAverage = (localIntegerListSum / 10)
        return(localIntegerListSum, localIntegerListAverage)                                                                                                                                                            # Return local Sum and local Average varibales

    while (len(integerList) < 10):
        userInteger = int(input("Please enter a integer you would like added to the List, press 'enter' when finished:... "))
        if (userInteger not in integerList):                                                                                                                                                                            # Check if user input is already in list, if not add to list and continue
            integerList.append(userInteger)
            print("Thank you. The integer has been added to the List.")
            print("")
        else:
            print("Integer already contained in List.  Please enter a different Integer:...")
            print("")

    (integerListSum, integerListAverage) = DoMath()                                                                                                                                                                     # Function call to do math and set variables for output

    print("The Integers you entered into the list were:")
    print(*integerList, sep = "\n")                                                                                                                                                                                     # * function prints through all elements in list, "\n" formats them vertically
    print("The Sum of the integers entered is: ", integerListSum)
    print("The Average of the integers entered is: ", integerListAverage)

def ProgramTwo():
    def CountWords(stringSentence):                                                                                                                                                                                     # Define function to calculate words in a string / sentence
        whiteSpace = stringSentence.count(" ")                                                                                                                                                                          # Counting characters of white space by tracking "spaces"
        if (stringSentence[0] == " " and stringSentence[-1] == " "):                                                                                                                                                    # White space variation based on possible input formatting mistakes
            totalWords = (whiteSpace - 1)
        elif (stringSentence[0] == " " or stringSentence[-1] == " "):                                                                                                                                                   # White space variation based on possible input formatting mistakes
            totalWords = (whiteSpace)
        elif (stringSentence[0] != " " and stringSentence[-1] != " "):                                                                                                                                                  # White space variation based on possible input formatting mistakes
            totalWords = (whiteSpace + 1)
        
        return(totalWords)
    
    stringSentence = input("Please enter a String to be tested, press 'enter' when finished:... ")

    totalWords = CountWords(stringSentence)                                                                                                                                                                             # Function call to calculate words
    print("Total Words: ", totalWords)

def ProgramThree():
    
    employees = []                                                                                                                                                                                                      # Init List
    salaries = []                                                                                                                                                                                                       # Init List
    bonusRates = []                                                                                                                                                                                                     # Init List
    bonuses = []                                                                                                                                                                                                        # Init List
    processedCount = 0
    
    def CalcBonus(paramSalary, paramBonusPercent):                                                                                                                                                                      # Define function to calculate bonuses (3a)
        salary = paramSalary
        bonus = paramBonusPercent
        
        holidayBonus = round((salary * (bonus / 100)))
        
        return(holidayBonus)                                                                                                                                                                                            # Return employee holdiay bonus
    
    employeeID = input("Please enter the Employee ID for first employee, press 'enter' when finished:... ")
    
    while (employeeID != "quit"):
        salary = float(input("Please enter the Salary of the current employee, press 'enter' when finished:... "))
        bonusRate = float(input("Please enter the Bonus Rate of the current employee in decimal format, press 'enter' when finished:... "))
        print("Processing Employee:... ")
        print(" ")
        
        paramSalary = salary
        paramBonusPercentage = bonusRate
        
        bonus = CalcBonus(paramSalary, paramBonusPercentage)                                                                                                                                                            # Function call to calculate bonus
        
        employees.append(employeeID)                                                                                                                                                                                    # Append list with most recent user input
        salaries.append(salary)                                                                                                                                                                                         # Append list with most recent user input
        bonusRates.append(bonusRate)                                                                                                                                                                                    # Append list with most recent user input
        bonuses.append(bonus)                                                                                                                                                                                           # Append list with most recent user input
        
        processedCount = (processedCount + 1)                                                                                                                                                                           # Iterate count of epmployees completed
#        print(employees, salaries, bonusRates, bonuses)
        print("Employee has been added to report.")
        print(" ")
        
        employeeID = input("Please enter the next Employee ID or 'quit' to finish and display report, press 'enter' when finished:... ")
        print("")
    
    print("Complete Payments Records Processed:")
    print("")
    print("Employee ID / Employee Salary / Bonus Rate / Bonus Earned")
    print("")
    for i in range(processedCount):                                                                                                                                                                                     # For Loop to iterate within range of the number of processed employees
        print(employees[i], " / ", "$", salaries[i], " / ", bonusRates[i],"%", " / ", "$", bonuses[i])                                                                                                                  # Access each list at the current index as it moves through above range, printing list of all employee information in records
        print("")
    
    print("The Total Amount of Bonuses Earned for the year was: $", sum(bonuses))
    print("")
    print("The Average Bonus Earned by empoyees for the year was: $", round((sum(bonuses) / processedCount)))
        

Main()                                                                                                                                                                                                                  # Function Call for Main Method, "Start" of Program
