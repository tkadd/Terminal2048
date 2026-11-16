import random


class TwentyFortyEight:
    slices = {
        "L": [slice(4*k, 4*k + 4) for k in range(4)],
        "U": [slice(k, None, 4) for k in range(4)],
        "D": [slice(k + 12, None, -4) for k in range(4)],
        "R": [slice(4*k + 3, 4*k - 1 if k > 0 else None, -1) for k in range(4)]
    }
    neighbours = {
        0: [1, 4], 1: [2, 5], 2: [3, 6], 3: [7],
        4: [5, 8], 5: [6, 9], 6: [7, 10], 7: [11],
        8: [9, 12], 9: [10, 13], 10: [11, 14], 11: [15],
        12: [13], 13: [14], 14: [15], 15: []
    }

    def __init__(self):
        self.score = 0
        self.initialise_board()

    def initialise_board(self):
        self.board = 16*[0]

        for _ in range(2):
            self.add_new_tile()

        return None

    def add_new_tile(self):
        empty_tiles = [i for i in range(16) if (self.board[i] == 0)]

        tile = random.choice(empty_tiles)
        val = random.choices((1, 2), weights=(0.9, 0.1), k=1)[0]

        self.board[tile] = val
        return None

    def compress(self, arr):
        ind = 0
        for val in arr:
            if val:
                arr[ind] = val
                ind += 1
        for i in range(ind, 4):
            arr[i] = 0
        return arr

    def merge(self, arr):
        for i in range(3):
            if arr[i] and (arr[i] == arr[i + 1]):
                arr[i], arr[i + 1] = arr[i] + 1, 0

                self.score += 2**arr[i]
        return arr

    def move(self, dir):
        slc = self.slices[dir]
        new_board = 16*[0]
        for i in range(4):
            row = self.board[slc[i]]
            new_row = self.compress(self.merge(self.compress(row)))

            new_board[slc[i]] = new_row

        if new_board != self.board:
            self.board = new_board
            return True
        else:
            return False

    def game_over_detection(self):
        for i in range(16):
            neighbours_vals = [self.board[j] for j in self.neighbours[i]]
            if (self.board[i] == 0) or (self.board[i] in neighbours_vals):
                return False
        return True


if __name__ == "__main__":
    pass
