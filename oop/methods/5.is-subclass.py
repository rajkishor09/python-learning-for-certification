class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


print(issubclass(LandVehicle, Vehicle))
print(issubclass(Vehicle, LandVehicle))