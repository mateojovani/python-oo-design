class Vehicle:
    def __init__(self, plate, spots):
        self.plate = plate
        self.spots = spots


class MotorCycle(Vehicle):
    def __init__(self, plate):
        Vehicle.__init__(self, plate, 1)

    def can_fit_in(self):
        return ('SMALL', 'COMPACT', 'LARGE')


class Car(Vehicle):
    def __init__(self, plate):
        Vehicle.__init__(self, plate, 1)

    def can_fit_in(self):
        return ('COMPACT', 'LARGE')


class Bus(Vehicle):
    def __init__(self, plate):
        Vehicle.__init__(self, plate, 5)

    def can_fit_in(self):
        return ('LARGE', )
