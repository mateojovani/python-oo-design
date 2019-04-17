from Spot import Spot
SPOT_SIZES = {
    1: 'SMALL',
    2: 'COMPACT',
    3: 'LARGE'
}


class Level:
    SPOTS_PER_ROW = 10
    SMALL_SPOTS = 0.1
    COMPACT_SPOTS = 0.6
    LARGE_SPOTS = 0.3

    def __init__(self, no, num_spots):
        self.no = no
        self.available_spots = num_spots
        self.rows = int(num_spots/Level.SPOTS_PER_ROW)
        self.spots = self.init_spots(num_spots)

    def fill_spots(self, spots, type, num_spot):
        num_spot += 1
        row = int(round(num_spot/Level.SPOTS_PER_ROW))
        spot = Spot(num_spot, self.no, row, type)
        spots[row][type].append(spot)

    def init_spots(self, num_spots):
        sizes = {}
        for _, size in SPOT_SIZES.items():
            sizes[size] = []
        spots = list(map(lambda _: sizes, [0]*self.rows))

        small_spots = int(Level.SMALL_SPOTS * num_spots)
        compact_spots = int(Level.COMPACT_SPOTS * num_spots)
        large_spots = num_spots - compact_spots - small_spots

        cur = 0 # in order fill
        for _ in range(small_spots):
            self.fill_spots(spots, SPOT_SIZES[1], cur)
        for _ in range(compact_spots):
            self.fill_spots(spots, SPOT_SIZES[2], cur)
        for _ in range(large_spots):
            self.fill_spots(spots, SPOT_SIZES[3], cur)

        return spots

    def spots_available(self, spot_type, num_spots):
        for row in range(0, self.rows):
            cur = 0 # get next available spot
            row_spots = self.spots[row][spot_type]
            while not row_spots[cur].is_available():
                cur += 1
                if cur == len(row_spots): break
            if cur == len(row_spots): cur -= 1

            for pos in range(cur, cur + num_spots):
                if not (row_spots[pos] and row_spots[pos].is_available()):
                    break # can't park in this row
            else: return row_spots[cur:cur + num_spots]
        else: return False

    def is_full(self):
        return self.available_spots == 0