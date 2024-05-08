class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass

veh = Vehicle()
lv = LandVehicle()
veh2 = veh
print(veh is lv) # * The is operator checks whether two variables refer to the same object.
print(veh2 is veh)
