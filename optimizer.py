class Optimizer:
    def __init__(self, bitmap):
        self.bitmap = bitmap

    def defragment(self):
        used = [1 for b in self.bitmap if b == 1]
        free = [0] * (len(self.bitmap) - len(used))
        return used + free