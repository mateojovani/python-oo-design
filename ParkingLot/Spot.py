class Spot:
    def __init__(self, no, level, row, spot_type):
        self.no = no
        self.vehicle = None
        self.level = level
        self.row = row
        self.type = spot_type

    def is_available(self):
        return not self.vehicle

    def park(self, vehicle):
        self.vehicle = vehicle
