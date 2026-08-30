# Custom Exception (Custom error handling for invalid options or stock)
class InvalidVehicleChoiceError(Exception):
    pass
class NegativeValueError(Exception):
    pass

# OOP Concept: Parent Class (Vehicle)
class Vehicle:
    def __init__(self, brand, rent_per_day):
        self.brand = brand
        self.rent_per_day = rent_per_day
    def display_info(self):
        return f"Brand: {self.brand} | Rent per Day: ${self.rent_per_day}"

# Inheritance: Child Class (Car inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, rent_per_day, doors):
        super().__init__(brand, rent_per_day)
        self.doors = doors
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} | Doors: {self.doors}"

# Main Program Function
def rent_vehicle():
    print("_____ Welcome to vehicle Rental System _____")
    print("1. Toyota corolla (Daily Rent: $50)")
    print("2. Honda Civic (Daily Rent: $70")

    try:
        choice = int(input("Enter Vehicle choice (1 or 2): "))
        if choice not in [1,2]:
            raise InvalidVehicleChoiceError("Invalid choice! Please select 1 or 2.")
        days = int(input("Enter number of days for rent: "))
        if days < 0:
            raise NegativeValueError("Days cannot be negative!")

        if choice == 1:
            selected_car = Car("Toyota Corolla", 50, 4 )
            total_bill = selected_car.rent_per_day * days
        else:
            selected_car = Car("Hona Civic", 70, 4)
            total_bill = selected_car.rent_per_day * days

        result_text = f"{selected_car.display_info()} | Total Days: {days} | Total Bill: ${total_bill}"
        print(f"\nSuccess! {result_text}")

        # File Handling (Saving rental record to a text file)
        with open("rental_record.txt", "a") as file:
            file.write(result_text + "\n")
        print("Record Successfully saved to 'rental_record.txt'!")

    # Handling Custom Exceptions and Built-in Exceptions
    except InvalidVehicleChoiceError as e:
        print(f"\nCustom error: {e}")
    except NegativeValueError as e:
        print(f"\nCustom error: {e}")
    except ValueError:
        print("\nInput Error! Enter valid number only!")
    except Exception as e:
        print(f"\nAn unexpected error occured: {e}")

# Program Execution
if __name__ == "__main__":
    rent_vehicle()

