class Recovery:
    def __init__(self, bitmap):
        self.bitmap = bitmap

    def recover_files(self):
        recovered = []
        current = []

        for i in range(len(self.bitmap)):
            if self.bitmap[i] == 1:
                current.append(i)
            else:
                if current:
                    recovered.append(current)
                    current = []

        if current:
            recovered.append(current)

        return recovered