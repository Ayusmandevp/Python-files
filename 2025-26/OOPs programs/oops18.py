# Multiple Inheritance - Battery and GPS Tracker: Create classes Battery and GPS with respective methods charge and location. Derive a SmartPhone class that inherits both functionalities.


class Battery:
    def charge(self):
        print("Charging the battery")

class GPS:
    def location(self):
        print("Current location is 478, 456")

class SmartPhone(Battery, GPS):
    pass

# Example usage:
phone = SmartPhone()
phone.charge()
phone.location()