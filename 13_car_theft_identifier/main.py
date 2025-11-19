# 1. Create the concept of a car in this world
class Car:
    def __init__(self, licence_plate: str) -> None:
        if len(licence_plate) != 6:
            raise ValueError('Invalid licence plate.')

        self.licence_plate = licence_plate


# 2. Create a place to store stolen cars
class StolenCarRegistry:
    def __init__(self) -> None:
        # Example: Set of license plates that are stolen
        self.stolen_plates: set[str] = set()

    def add_stolen_plates(self, plates: list[str]) -> None:
        for plate in plates:
            self.stolen_plates.add(plate.upper())

    def is_stolen(self, plate: str) -> bool:
        return plate.upper() in self.stolen_plates


# 3. Check for stolen cars
def main() -> None:
    registry: StolenCarRegistry = StolenCarRegistry()
    # Populate with some stolen plates
    registry.add_stolen_plates(['ABC123', 'XYZ999', 'BOB789'])

    print('Welcome to Car Theft Identifier')
    while True:
        plate: str = input('Enter car licence plate: ').strip()
        car: Car = Car(plate)
        if registry.is_stolen(car.licence_plate):
            print(f'❌ Car with plate "{car.licence_plate}" is: REPORTED STOLEN!')
        else:
            print(f'✅ Car with plate "{car.licence_plate}" is: OK')


if __name__ == '__main__':
    main()

# Homework:
# 1. Add a way to remove stolen cars from the StolenCarRegistry.
# 2. Add functionality that counts the total amount of stolen cars.
# 3. Add functionality that displays all the stolen plates.
