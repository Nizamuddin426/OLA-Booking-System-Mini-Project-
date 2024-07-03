import re
print("*******************************************")
print("*******************************************")
print("*******************************************")
print("!!!!!!!Welcome to Ola Booking System!!!!!!!")
print("*******************************************")
print("*******************************************")
print("*******************************************")
#creating a main class for developing ola booking system
class OlaBookingSystem:
    def _init_(self):
        self.rate_per_km = 2.0
    #defining function to calculate total cost
    def calculate_trip_cost(self, pickup_point, drop_point, distance):
        total_cost = distance * self.rate_per_km
        return total_cost
    #defining function to get details of the booking from the user
    def book_ride(self):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!Proceed for Booking!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        pickup_points = {
            1: "VIT MAIN GATE",
            2: "CHITTOR BUS STAND",
            3: "RAILWAY STATION"
        }
        print("\n")
        drop_points = {
            1: "NEW BUS STAND",
            2: "OLD BUS STAND",
            3: "VIT 11 GATE"
        }

        print("Pickup Points:")
        for key, value in pickup_points.items():
            print(f"{key}. {value}")
        print("\n")
        print("Drop Points:")
        for key, value in drop_points.items():
            print(f"{key}. {value}")
        #getting input of dropping and pickup details from the user
        pickup_choice = int(input("\n \tEnter pickup point (1-3): "))
        drop_choice = int(input("\n \tEnter drop point (1-3): "))

        pickup_point = pickup_points.get(pickup_choice)
        drop_point = drop_points.get(drop_choice)

        distance_mapping = {
            (1, 1): 5,  
            (1, 2): 8,  
            (1, 3): 3,  
            (2, 1): 5,   
            (2, 2): 7,   
            (2, 3): 3, 
            (3, 1): 5, 
            (3, 2): 7,  
            (3, 3): 7    
        }

        distance = distance_mapping.get((pickup_choice, drop_choice), 0)

        if distance == 0:
            print("Invalid pickup/drop combination. Please try again.")
            return

        #geeting extra option from the user
        print("\nCar Options:")
        print("1. Basic (No A/C)")
        print("2. Average (With A/C)")
        print("3. Luxurious (With A/C and Wi-Fi)")


        car_choice = int(input("\n \tChoose car type (1-3): "))
        car_types = {
            1: "Basic Car",
            2: "Average Car ",
            3: "Luxurious Car"
        }

        car_type = car_types.get(car_choice)

        #assigning the inital cost of the variable to zero
        ac_cost = 0
        wifi_cost = 0

        if car_choice == 2 or car_choice == 3:
            ac_choice = input("Do you want A/C? (Y/N): ")
            if ac_choice.upper() == "Y":
                ac_cost = 5

        if car_choice == 3:
            wifi_choice = input("Do you want Wi-Fi? (Y/N): ")
            if wifi_choice.upper() == "Y":
                wifi_cost = 5  

        
        if car_choice == 1:
            base_cost = 20  
        elif car_choice == 2:
            base_cost = 30  
        elif car_choice == 3:
            base_cost = 40  
        else:
            print("Invalid car choice. Please try again.")
            return
        #calulating total cost of the booking 
        total_cost = base_cost + ac_cost + wifi_cost
        total=total_cost*distance
        #displaying details of the booking to the user
        print("\n\t******Booking Details:*********")
        print(f"\tPickup Point: {pickup_point}")
        print(f"\tDrop Point: {drop_point}")
        print(f"\tCar Type: {car_type}")
        print(f"\tBase Cost: ${base_cost}")
        print(f"\tA/C Cost: ${ac_cost}")
        print(f"\tWi-Fi Cost: ${wifi_cost}")
        print(f"\tTotal Cost: ${total}")
        print("\nBOOKING CONFIRMED........HAVE SAFE JOURNEY!!!!!")

def book():
    print("Booking details have been recorded. Proceed for Booking!!!!!!")
    print("\n")
    ola_system = OlaBookingSystem()
    ola_system.book_ride()

#getting how many times the user wants to book the ola
no_of_tickets = int(input("Enter number of times you want to book: "))
#openning file and wriiting the booking details of the suer in the file as a bill or database
with open("olabookingdetails.txt", 'w') as f:
    for i in range(no_of_tickets):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        phone = input("Enter phone number: ")
        address = input("Enter your address: ")
        pincode = input("Enter pincode: ")
#validating the credenetials that the user has entered
        vname = re.match("^[A-Za-z ]+$", name)
        vage = re.match("^[0-9]{2}$", age)
        vphone = re.match("^[6-9]{1}[0-9]{9}$", phone)
        vaddress = re.match("^[A-Za-z0-9_\-# ]+$", address)
        vpincode = re.match("^[0-9]{6}$", pincode)
#writting the details in the file
        if vname and vage and vphone and vaddress and vpincode:
            f.write(f"Booking Details - {i+1}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Age: {age}\n")
            f.write(f"Phone: {phone}\n")
            f.write(f"Address: {address}\n")
            f.write(f"Pincode: {pincode}\n")
            f.write("\nCredentials recorded! Proceed to booking.\n\n")
            book()
        else:
            print("Enter valid credentials to proceed with the booking.")
        break


