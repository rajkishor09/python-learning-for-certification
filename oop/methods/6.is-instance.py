class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass

veh = Vehicle()
lv = LandVehicle()
print(isinstance(veh, Vehicle))
print(isinstance(veh, LandVehicle))

print(isinstance(lv, LandVehicle))
print(isinstance(lv, Vehicle)) # True, because its base class