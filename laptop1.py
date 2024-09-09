file = open("laptop_Data.txt","r")
mydict = {}
LaptopID = 1
for line in file:
    line = line.replace("\n","")
    mydict.update({LaptopID: line.split(",")})
    LaptopID+=1
print(mydict)
file.close()
print("\n")
import datetime
def available_Laptops():
    print("\t \t\t\t\t\t\t\t Welcome to SS1 Supps")
    print("*********************************************************************************************************************************************************")
    print("\t \t\t\t\t\t\t      KAMALPOKHARI || KATHMANDU")
    print("\n")
    print("*********************************************************************************************************************************************************")
    print("S.N.""\t"    "Laptop"      "\t""\t""\t""\t""Name"      "\t""\t"  "Price"    "\t""\t"     "Quantity"     "\t"      "Intel/Generator"     "\t""\t""\t""Processor")
    print("*********************************************************************************************************************************************************")
    file = open("laptop_Data.txt","r")
    a = 1
    for line in file:
        print(a,"\t"+line.replace(",","\t \t"))
        a+=1
       
print("\n")
print("Please choose any of the option given below")

continueLoop = True
while continueLoop == True:
    print("Press 1 to buy from manufacture")
    print("Press 2 to sell to customer")
    print("Press 3 to exit")
    print("\n")

    userinput = int(input("Please select any of the option"))

    if userinput == 1:
        print("Thank you for providing us with these products.")
        available_Laptops()
       
        print("For billing purpose you have to submit your details")
        Rname = input("Enter a name:")
        Rphone = int(input("Enter your phone number:"))

        RValidID = int(input("Please provide the ID of the laptop you want to order"))

        
        while RValidID <= 0 or RValidID > len(mydict):
            print("Please provide a valid Laptop ID:")

            print("\n")

            RValidID = int(input("Please provide the ID of the Laptop you want to order:"))

        OrderQuantity = int(input("Please Provide the number of quantity of the laptop you want to buy:"))
        print("\n")

       #update the text file

        mydict[RValidID][3] = int (mydict[RValidID][3])+int(OrderQuantity)
        file = open("laptop_Data.txt","w")
        for values in mydict.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
            file.write("\n")
        file.close()

       #getting ordered items
        RNameOfProduct = mydict[RValidID][0]
        QuantitySelectedByRental = OrderQuantity
        UnitPriceForRental = mydict[RValidID][2]
        PriceOfSelectedItemForRental = mydict[RValidID][2].replace(",","")
        TotalPriceForRental = int(PriceOfSelectedItemForRental)*int(QuantitySelectedByRental)
       
        OrderedLaptop = []
        OrderedLaptop.append((RNameOfProduct,QuantitySelectedByRental,UnitPriceForRental,TotalPriceForRental))

        ShippingCostForRental = input("Dear user do you want your laptop to be shipped?(Y/N)").upper()

        if ShippingCostForRental == "Y":
            RentalTotal = 0
            ShippingCostForRental = 1500
            for i in OrderedLaptop:
                RentalTotal+= int(i[3])
            GrandTotalForRental = RentalTotal+ShippingCostForRental
            TodayDateAndTime = datetime.datetime.now()
            print("\n")
            print("\t \t \t \t                         Manufacturer Bill ")
            print("\n")
            print("\t \t \t \t KamalPokhari || Kathmandu: Phone no.:123123123")
            print("\n")
            print("-"*90)
            print("Purchase Details are:")
            print("-"*90)
            print("Name of the customer:"+str(Rname))
            print("Contact number of the customer:"+str(Rphone))
            print("Date and time of the purchase:"+str(TodayDateAndTime))
            print("-"*90)
            print("\n")
            print("Laptop Details are:")
            print("Item Name \t\t  Total Quantity \t\t  Unit Price  \t\t\t\t Total")
            print("-"*90)
            for i in OrderedLaptop:
                print(i[0],"\t\t\t", i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
            print("-"*90)
            if ShippingCostForRental:
                print("Your Shipping cost is:", ShippingCostForRental)
                print("Grand Total:"+ str(GrandTotalForRental))
                print("Note: Shipping cost is added to the grand total")
            else:
                print("Grand Total: $"+str(TotalPriceForRental))
            print("\n")
            with open(str(Rname) + str(Rphone) + ".txt", "w") as file:
                file.write("\n")
                file.write("\t \t \t \t                         Laptop Shop Bill \n")
                file.write("\t \t \t \t KamalPokhari || Kathmandu:  Phone no.:123123123 \n")
                file.write("-" * 90 + "\n")
                file.write("Ordering Details are: \n")
                file.write("-" * 90 + "\n")
                file.write("Name of the customer: " + str(Rname) + "\n")
                file.write("Contact number of the customer: " + str(Rphone) + "\n")
                file.write("Date and time of the purchase: " + str(TodayDateAndTime) + "\n")
                file.write("-" * 90 + "\n")
                file.write("\nPurchase Details are: \n")
                file.write("Item Name \t\t  Total Quantity \t\t  Unit Price  \t\t\t\t Total \n")
                file.write("-" * 90 + "\n")
                for i in OrderedLaptop:
                    file.write(i[0] + "\t\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t$" + str(i[3]) + "\n")
                    file.write("-" * 90 + "\n")
                if ShippingCostForRental:
                    file.write("Your Shipping cost is: $" + str(ShippingCostForRental) + "\n")
                    file.write("Grand Total: $" + str(GrandTotalForRental) + "\n")
                    file.write("Note: Shipping cost is added to the grand total \n")
                else:
                    file.write("Grand Total: $" + str(GrandTotalForRental) + "\n")
                    
        TodayDateAndTime=datetime.datetime.now()
        if ShippingCostForRental=="N":
            print("\n")
            print("\t \t \t \t                         Laptop Shop Bill ")
            print("\n")
            print("\t \t \t \t KamalPokhar || Kathmandu: Phone no.:123123123")
            print("\n")
            print("-"*90)
            print("laptop Details are:")
            print("-"*90)
            print("Name of the customer:"+str(Rname))
            print("Contact number of the customer:"+str(Rphone))
            print("Date and time of the purchase:"+str(TodayDateAndTime))
            print("-"*90)
            print("\n")
            print("Purchase Details are:")
            print("Item Name \t\t  Total Quantity \t\t  Unit Price  \t\t\t\t Total")
            print("-"*90)
            for i in OrderedLaptop:
                print(i[0],"\t\t\t", i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
            print("-"*90)
            print("Your total is: "+str(TotalPriceForRental))
            file.close()


    elif userinput == 2:
        print("Thank you for selling")
        available_Laptops()
       
        print("For billing purpose you have to submit your name")
        name = input("Enter a name:")
        phone = str(input("Enter your phone number:"))
        ValidID = int(input("Please provide the ID of the Laptop you want to buy:"))
        print("\n")

        
      #ValidID
 
        while ValidID <= 0 or ValidID > len(mydict):
            print("Please provide a valid Laptop ID:")

            print("\n")

            ValidID = int(input("Please provide the ID of the laptop you want to Buy:"))

        UserQuantity = int(input("Please Provide the number of quantity of the laptop you want to buy:"))
        print("\n")
 
    #ValidQuantity

        GetQuantity = mydict[ValidID][3]
        while UserQuantity <= 0 or UserQuantity > int(GetQuantity):
            print("Dear Admin, the quantity you are looking for is not available in our shop. Please provide the quantity again:")
            print("\n")
            UserQuantity = int(input("Please Provide the number of the quantity of the laptop you want to purchase:"))
        print("\n")

    #update the text file

        mydict[ValidID][3] = int (mydict[ValidID][3])-int(UserQuantity)
        file = open("laptop_Data.txt","w")
        for values in mydict.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
            file.write("\n")
        file.close()
        

    #getting user purchased items
        NameOfProduct = mydict[ValidID][0]
        QuantitySelectedByUser = UserQuantity
        UnitPrice = mydict[ValidID][2]
        PriceOfSelectedItem = mydict[ValidID][2].replace(",","")
        TotalPrice = int(PriceOfSelectedItem)*int(QuantitySelectedByUser)
       
        UserPurchasedLaptop = []
        UserPurchasedLaptop.append((NameOfProduct,QuantitySelectedByUser,UnitPrice,TotalPrice)) 

        ShippingCost = input("Dear user do you wantyour laptop to be shipped?(Y/N)").upper()

        if ShippingCost == "Y":
            Total = 0
            ShippingCost = 1500
            for i in UserPurchasedLaptop:
                Total+= int(i[3])
            GrandTotal = Total+ShippingCost
            TodayDateAndTime = datetime.datetime.now()
            print("\n")
            print("\t \t \t \t                         Laptop Shop Bill ")
            print("\n")
            print("\t \t \t \t KamalPokhari || Kathmandu: Phone no.:123123123")
            print("\n")
            print("-"*90)
            print("laptop Details are:")
            print("-"*90)
            print("Name of the customer:"+str(name))
            print("Contact number of the customer:"+str(phone))
            print("Date and time of the purchase:"+str(TodayDateAndTime))
            print("-"*90)
            print("\n")
            print("Purchase Details are:")
            print("Item Name \t\t  Total Quantity \t\t  Unit Price  \t\t\t\t Total")
            print("-"*90)
            for i in UserPurchasedLaptop:
                print(i[0],"\t\t\t", i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
            print("-"*90)
            if ShippingCost:
                print("Your Shipping cost is:", ShippingCost)
                print("Grand Total:"+ str(GrandTotal))
                print("Note: Shipping cost is added to the grand total")
            else:
                print("Grand Total: $"+str(Total))
            print("\n")
            with open(str(name) + str(phone) + ".txt", "w") as file:
                file.write("\n")
                file.write("\t \t \t \t                         Laptop Shop Bill \n")
                file.write("\t \t \t \t KamalPokhari || Kathmandu:  Phone no.123123123 \n")
                file.write("-" * 90 + "\n")
                file.write("laptop Details are: \n")
                file.write("-" * 90 + "\n")
                file.write("Name of the customer: " + str(name) + "\n")
                file.write("Contact number fo the customer: " + str(phone) + "\n")
                file.write("Date and time of the purchase: " + str(TodayDateAndTime) + "\n")
                file.write("-" * 90 + "\n")
                file.write("\nPurchase Details are: \n")
                file.write("Item Name \t\t  Total Quantity \t\t  Unit Price  \t\t\t\t Total \n")
                file.write("-" * 90 + "\n")
                for i in UserPurchasedLaptop:
                    file.write(i[0] + "\t\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t$" + str(i[3]) + "\n")
                    file.write("-" * 90 + "\n")
                if ShippingCost:
                    file.write("Your Shipping cost is: $" + str(ShippingCost) + "\n")
                    file.write("Grand Total: $" + str(GrandTotal) + "\n")
                    file.write("Note: Shipping cost is added to the grand total \n")
                else:
                    file.write("Grand Total: $" + str(GrandTotal) + "\n")
        TodayDateAndTime = datetime.datetime.now()            
        if ShippingCost=="N":
            print("\n")
            print("\t \t \t \t                         Laptop Shop Bill ")
            print("\n")
            print("\t \t \t \t KamalPokhar || Kathmandu: Phine no.:123123123")
            print("\n")
            print("-"*90)
            print("laptop Details are:")
            print("-"*90)
            print("Name of the customer:"+str(name))
            print("Contact number of the customer:"+str(phone))
            print("Date and time of the purchase:"+str(TodayDateAndTime))
            print("-"*90)
            print("\n")
            print("Purchase Details are:")
            print("Item Name \t\t  Total Quantity \t\t  Unit Price  \t\t\t\t Total")
            print("-"*90)
            for i in UserPurchasedLaptop:
                print(i[0],"\t\t\t", i[1],"\t\t\t",i[2],"\t\t\t","$",i[3])
            print("-"*90)
            print("Your total is: "+str(TotalPrice))
            file.close()
    elif userinput == 3:
        continueLoop = False
    else:
        print("Please enter correct option")

