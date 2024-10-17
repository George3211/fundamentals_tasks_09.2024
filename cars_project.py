# Hiring status tracking dictionary
rental_status = {}
cars = []


# Add car

def add_car(car_id, brand, model, rental_price):
    car = {
        "id": car_id,
        "brand": brand,
        "model": model,
        "rental_price": rental_price,
        "availability": True
    }
    cars.append(car)
    print(f"Car {brand} {model} added successfully!")


# Car rental function


def rent_car(car_id, user):
    for car in cars:
        if car["id"] == car_id and car["availability"]:
            car["availability"] = False
            rental_status[user] = {"car_id": car_id, "rental_price": car["rental_price"], "rental_duration": 0}
            print(f"Car {car['brand']} {car['model']} rented successfully!")
            return
    print("Car not available or invalid car ID.")


# Car return function


def return_car(user, rental_duration):
    if user in rental_status:
        car_id = rental_status[user]["car_id"]
        rental_price = rental_status[user]["rental_price"]
        total_cost = rental_price * rental_duration
        for car in cars:
            if car["id"] == car_id:
                car["availability"] = True
                break
        del rental_status[user]
        print(f"Car returned successfully! Total cost: ${total_cost}")
    else:
        print("No car rented by this user.")


# Function to display available cars


def view_available_cars():
    print("Available cars:")
    for car in cars:
        if car["availability"]:
            print(f'ID: {car["id"]}, Brand: {car["brand"]}, Model: {car["model"]}, \n'
                  f' Rental Price: ${car["rental_price"]} per day')


# view_available_cars()


def returning_car():
    #  function to return the car
    user_name = input("\nPlease, enter your names: ")
    # Prompt the user to enter his names.
    # Prompt the user to enter duration of the rent.
    duration_of_rent = int(input("Please, enter duration of the rent. Keep in mind, that the price is per day.\n"
                                 "If the day has started, the whole day is considered: "))

    if user_name in rental_status:  # Check if the user is in dictionary for rentals.
        return_car(user_name, duration_of_rent)  # calling function to return the car


def renting_car():  # function to rent the car
    while True:  # Loop that let user to input id again if chosen one is not available
        choice = int(input("\nChoose id of car you want to rent: "))
        for car in cars:
            # Check if chosen car is available, if it is, prompt user to input names, if not, prompt you for new input
            if car["id"] == choice and car["availability"]:
                name_user = input("\nPlease, enter your names. ")
                return rent_car(choice, name_user)  # calling function to rent the car
        print("Car not available or invalid car ID.\nPlease, try again.")


def display_cars():  # function to display available cars
    print("\nAvailable Cars:")
    view_available_cars()  # calling function to display available cars


def main_menu():
    """Display the main menu."""
    print("\nWelcome to RentACar")
    print("1. Add car")
    print("2. View Car")
    print("3. Rent a Car")
    print("4. Return a Car")
    print("5. Exit")
    return int(input("Please choose an option (1-5): "))


def main():
    """Main function to run the platform."""
    while True:  # validation to ensure the user enters valid options
        choice = main_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            car_id = int(input("Enter car ID: "))
            brand = input("Enter car brand: ")
            model = input("Enter car model: ")
            rental_price = float(input("Enter rental price per day: "))
            add_car(car_id, brand, model, rental_price)

        elif choice == 2:
            # calling function to display available cars
            display_cars()

        elif choice == 3:
            # Prompt the user to choose id of car and insert his names. Checking if the chosen car is available.
            # If available calling function to rent the car.
            renting_car()

        elif choice == 4:
            # Prompt the user to enter his names and duration of the rent.
            returning_car()

        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            # if the user enter invalid option, receive error message and return for new input
            print("Invalid choice. Please try again.")


main()
