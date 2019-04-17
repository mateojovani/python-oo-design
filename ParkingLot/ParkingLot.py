from Level import Level
from Vehicle import Vehicle, MotorCycle, Car, Bus
import random


class ParkingLot:
    SPOTS_PER_LEVEL = 40

    def __init__(self, num_lev):
        self.levels = self.init_levels(num_lev)
        self.vehicles = []

    def init_levels(self, num_lev):
        levels = []
        for level in range(num_lev):
            levels.append(Level(level, ParkingLot.SPOTS_PER_LEVEL))
        return levels

    def park_vehicle(self, vehicle):
        for level in self.levels:
            if not level.is_full():
                # check each type if free
                for spot_type in vehicle.can_fit_in():
                    spots_available = level.spots_available(spot_type, vehicle.spots)
                    if spots_available:
                        for spot in spots_available:
                            spot.park(vehicle)
                        self.vehicles.append(vehicle)
                        return True
        else:
            return False


if __name__ == "__main__":
    pl = ParkingLot(5)
    m = MotorCycle("M_0")
    c = Car("C_0")
    b = Bus("B_0")
    pl.park_vehicle(m)
    pl.park_vehicle(c)
    pl.park_vehicle(b)

    v = (MotorCycle, Car, Bus)

    for num in range(40*5):
        vehicle = v[random.randrange(0, 2)]
        pl.park_vehicle(vehicle("GEN_PLATE_" + str(num)))