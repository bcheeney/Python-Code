def Main():
    (count, salesTaxRate, preTaxAmount, postTaxAmount, totalPreTaxAmount, totalPostTaxAmount, highPostTaxAmount, averagePostTaxAmount, saleID) = InitVars()
    #state, date, and taxRate are input and output once
    state = input("Please input the State Where sale was made: ")
    print(state)
    date = input("Please input the Date of Sale in 'Month' 'Day' , 'Year' format: ")
    print(date)
    taxRate = float(input("Please enter the Tax Rate for the sale: "))
    print(taxRate)

#    print("Count is set to: ", count)
        #get the first saleID
    saleID = input("Please enter the Sale ID associated with this sale: ")

    while (saleID != "quit"):
#        (count, preTaxAmount) = InputSale()
        count = count + 1   #increase the count by 1
        print("count is set to: ", count)

        preTaxAmount = InputSale()

#        print("count is set to: ", count)
#        print("preTaxAmount is set to: ", preTaxAmount)
#        print(taxRate, preTaxAmount, totalPreTaxAmount, totalPostTaxAmount, averagePostTaxAmount, count, highPostTaxAmount, saleID)
#        (postTaxAmount, totalPostTaxAmount, averagePostTaxAmount) = CalculateTaxes(taxRate, preTaxAmount, totalPreTaxAmount, totalPostTaxAmount, averagePostTaxAmount, count, highPostTaxAmount, saleID)
        (postTaxAmount, totalPreTaxAmount, totalPostTaxAmount, averagePostTaxAmount) = CalculateTaxes(taxRate, preTaxAmount, totalPreTaxAmount, totalPostTaxAmount, averagePostTaxAmount, count, highPostTaxAmount, saleID)
        (highPostTaxAmount, highSaleID) = CheckHighSale(postTaxAmount, highPostTaxAmount, saleID)
        
        saleID = input("Please Enter the Sale ID of tjhe Next Sale: ")
        
    SalesReport()
    
def InitVars():#initialize variables
    count = 0
    salesTaxRate = 0
    preTaxAmount = 0
    postTaxAmount = 0
    totalPreTaxAmount =0
    totalPostTaxAmount =0
    highPostTaxAmount = 0
    averagePostTaxAmount =0
    saleID = "run"
    return(count, salesTaxRate, preTaxAmount, postTaxAmount, totalPreTaxAmount, totalPostTaxAmount, highPostTaxAmount, averagePostTaxAmount, saleID)
#Students: why don't we initialize saleID, highSaleID, state, or date???                               #(Used as Local Variables in Functions)


#Check the sale ID for the kill flag.  If it is NOT set to quit, then process the sale
def InputSale():
    preTaxAmount = float(input("Please enter the Pre-Tax price of sale: "))
#    print("AAA preTaxAmount is set to: ", preTaxAmount)
    #check for the preTaxAmount limit of $30000
    while(preTaxAmount > 30000):
        print("Sale Amount exceeds Limit. Please re-enter sale price or speak with manager.")
        preTaxAmount = float(input("Enter the Pre-Tax price of sale: "))
    
    return preTaxAmount

def CalculateTaxes(taxRate, preTaxAmount, totalPreTaxAmount, totalPostTaxAmount, averagePostTaxAmount, count, highPostTaxAmount, saleID):
    postTaxAmount = preTaxAmount * (taxRate + 1)
    totalPreTaxAmount = totalPreTaxAmount + preTaxAmount #calculate the TOTAL preTaxAmount
    totalPostTaxAmount = totalPostTaxAmount + postTaxAmount    #calculate the TOTAL postTaxAmount
    averagePostTaxAmount = totalPostTaxAmount / count  #calculate the averagePostTaxAmount
    
    return(postTaxAmount, totalPreTaxAmount, totalPostTaxAmount, averagePostTaxAmount)

def CheckHighSale(postTaxAmount, highPostTaxAmount, saleID):
    if (postTaxAmount > highPostTaxAmount):		#check for the high value
        highPostTaxAmount = postTaxAmount
        highSaleID = saleID
        return(highPostTaxAmount, highSaleID)

    #the following variables are now output for EACH sale
#    output saleID
#    output preTaxAmount
#    output postTaxAmount
    #input the next saleID you want to process, then go start back to the start of the while loop to check for the -1 kill flag
    saleID = input("Please input the next saleID: ")
    

#after the "quit" kill flag is entered and the while conditional has 'failed', you want to output the final report
def SalesReport(count, totalPreTaxAmount, totalPostTaxtAmount, averagePostTaxAmount, totalPostTaxAmount,highPostTaxAmount, highSaleID ):
    print("The Total number of sales processed was: ", count)
    print("The Total value of sales before taxes was : ", totalPreTaxAmount)
    print("The Total value of sales after taxes was : ", totalPostTaxAmount)#output totalPostTaxAmount
    print("The Average value of sales after taxes was : ", averagePostTaxAmount)#output averagePostTaxAmount
    print("The Highest value of a single sale after taxes was : ", highPostTaxAmount)#output highPostTaxAmount
    print("The ID of the Salesperson associated with the highest sale was : ", highSaleID)#output highSaleID

Main()