def Home():
    print("""
     Enter 1 to Vehicle List.
     Enter 2 to add a new vehicle.
     Enter 3 to remove a vehicle.
     Enter 4 to assign a hire.                          
     Enter 0 to (Exit) the program.          
    """)


Vehicle_List =  {
   '001': {'type':"Car",'name':'Alto','Max_passengers': 3,'condition': 'AC',},
   '002':{'type':"Car",'name':'Audi','Max_passengers': 3,'condition': 'Non AC',},
   '003':{'type':"Car",'name':'BMW','Max_passengers': 4,'condition': 'AC',},
   '004':{'type':"Car",'name':'Mazda','Max_passengers': 4,'condition': 'Non AC',},
   '005':{'type':"Car",'name':'Volvo','Max_passengers': 4,'condition': 'AC',},

   '006': {'type':"Van",'name':'Toyota HiAce','Max_passengers': 10,'condition': 'AC',},
   '007':{'type':"Van",'name':'Ford Galaxy','Max_passengers': 8,'condition': 'Non AC',},
   '008':{'type':"Van",'name':'Nissan NV350 Urvan','Max_passengers': 12,'condition': 'AC',},

   '009': {'type': "ThreeWheel", 'Max_passengers': 3, },
   '010': {'type': "ThreeWheel", 'Max_passengers': 3, },





    
   '011':{'type':"Truck",'name':'Freightliner','size': '7ft',},
   '012':{'type':"Truck",'name':'FUSO','size': '12ft',},

   '013': {'type': "Lorry", 'name': 'Mahindra', 'Max load and size': '25000kg', },
   '014': {'type': "Lorry", 'name': 'Dimo Batta', 'Max load and size': '25000kg',},
   '015': {'type': "Lorry", 'name': 'Mitsubishi', 'Max load and size': '35000kg',},


}


def Vehicles():
   i = 1
   for vehicle, features in Vehicle_List.items():
      print("\t", i,")", " Vehicle: ", vehicle)
      i += 1
      for value in features:
         print("\t", value + ':', features[value])
      print("\n")





def Add_Vehicle():
   print("Add a new Vehicle")

   type = input("Enter the vehicle type you want to add (car,van,threewheeler,truck,lorry): ")

   if type=='car':
      Reg_No = input("Enter Vehicle Registration Number: ")
      Vehicle_List[Reg_No] = {}

      Vehicle_Type = input("Vehicle_Type: ")
      Vehicle_List[Reg_No]["Vehicle_Type"] = Vehicle_Type

      Vehicle_Name = input("Vehicle_Name: ")
      Vehicle_List[Reg_No]["Vehicle_Name"] = Vehicle_Name

      Max_Passengers = input("Maximum passengers: ")
      Vehicle_List[Reg_No]["Max_passengers"] =  Max_Passengers

      Condition = input("Condition: ")
      Vehicle_List[Reg_No]["Condition"] = Condition

      print("Vehicle added Successfully.")

   elif type=='van':
      Reg_No = input("Enter Vehicle Registration Number: ")
      Vehicle_List[Reg_No] = {}

      Vehicle_Type = input("Vehicle_Type: ")
      Vehicle_List[Reg_No]["Vehicle_Type"] = Vehicle_Type

      Vehicle_Name = input("Vehicle_Name: ")
      Vehicle_List[Reg_No]["Vehicle_Name"] = Vehicle_Name

      Max_Passengers = input("Maximum passengers: ")
      Vehicle_List[Reg_No]["Max_passengers"] = Max_Passengers

      Condition = input("Condition: ")
      Vehicle_List[Reg_No]["Condition"] = Condition

      print("Vehicle added Successfully.")

   elif type=='threewheeler':
      Reg_No = input("Enter Vehicle Registration Number: ")
      Vehicle_List[Reg_No] = {}

      Vehicle_Type = input("Vehicle_Type: ")
      Vehicle_List[Reg_No]["Vehicle_Type"] = Vehicle_Type

      Max_Passengers = input("Maximum passengers: ")
      Vehicle_List[Reg_No]["Max_passengers"] = Max_Passengers

      print("Vehicle added Successfully.")

   elif type=='truck':
      Reg_No = input("Enter Vehicle Registration Number: ")
      Vehicle_List[Reg_No] = {}

      Vehicle_Type = input("Vehicle_Type: ")
      Vehicle_List[Reg_No]["Vehicle_Type"] = Vehicle_Type

      Vehicle_Name = input("Vehicle_Name: ")
      Vehicle_List[Reg_No]["Vehicle_Name"] = Vehicle_Name

      Size = input("Size: ")
      Vehicle_List[Reg_No]["Size"] = Size

      print("Vehicle added Successfully.")

   elif type=='lorry':
      Reg_No = input("Enter Vehicle Registration Number: ")
      Vehicle_List[Reg_No] = {}

      Vehicle_Type = input("Vehicle_Type: ")
      Vehicle_List[Reg_No]["Vehicle_Type"] = Vehicle_Type

      Vehicle_Name = input("Vehicle_Name: ")
      Vehicle_List[Reg_No]["Vehicle_Name"] = Vehicle_Name

      Max_load_and_size = input("Max load and size: ")
      Vehicle_List[Reg_No]["Max load and size"] = Max_load_and_size

      print("Vehicle added Successfully.")

   else:
      print("Enter a valid vehicle type")


def Remove_Vehicle():
   print("Remove a Vehicle")

   Reg_No = input("Enter the Registration Number of the vehicle that you want to remove : ")
   del Vehicle_List[Reg_No]

   print("Vehicle removed Successfully.")


while True:
    Home()
    try:
        userInput = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid input")
    else:

        if userInput != 0:

            # to search a Vehicle.

            if userInput == 1:
                Vehicles()


# to add a new vehicle
            elif userInput == 2:
               Add_Vehicle()

# to remove a vehicle
            elif userInput == 3:
               Remove_Vehicle()



# to assign a hire.
            elif userInput == 4:
                Vehicles()
                Reg_no = input("Enter the Registration number of the vehicle you want to hire:  ")
                print("Vehicle having Registration number ", Reg_no, " is ready to Hire for you.")
                print("Have a safe ride! \n")

                End_Ride = input("Enter \"end\" to finish the ride : ")
                if userInput == "end":
                   print("Hire Completed")

            else:
                print("Enter a valid input")
        else:
            print("End")
            break


