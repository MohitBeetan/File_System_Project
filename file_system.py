import json

class FileSystem:
    def __init__(self):
        self.bitmap = self.load_bitmap()
        self.files = {}

    def load_bitmap(self):
        try:
            with open("bitmap.json", "r") as f:
                return json.load(f)
        except:
            return [0]*10

    def save_bitmap(self):
        with open("bitmap.json", "w") as f:
            json.dump(self.bitmap, f)

    def create_file(self, name, size):
        if name in self.files:
            return "❌ File already exists"

        blocks = []
        for i in range(len(self.bitmap)):
            if self.bitmap[i] == 0:
                blocks.append(i)
                if len(blocks) == size:
                    break

        if len(blocks) < size:
            return "❌ Not enough space"

        for b in blocks:
            self.bitmap[b] = 1

        self.files[name] = blocks
        self.save_bitmap()

        return f"✅ {name} → {blocks}"

    def delete_file(self, name):
        if name not in self.files:
            return "❌ File not found"

        for b in self.files[name]:
            self.bitmap[b] = 0

        del self.files[name]
        self.save_bitmap()

        return f"🗑 {name} deleted"

    def show_bitmap(self):
        return self.bitmap

    def crash(self):
        self.files = {}
        return "💥 System crashed!"

    def get_files(self):
        return self.files