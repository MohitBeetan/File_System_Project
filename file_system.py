import json

class FileSystem:
    def __init__(self):
        # ---------------- ORIGINAL ----------------
        self.bitmap = self.load_bitmap()
        self.files = {}

        # ---------------- NEW FEATURES ----------------
        self.data = {}              # store file content
        self.directories = {"root": {}}   # directory system
        self.access_count = {}      # track file usage

        # load saved data
        self.load_files()

    # ---------------- ORIGINAL ----------------
    def load_bitmap(self):
        try:
            with open("bitmap.json", "r") as f:
                return json.load(f)
        except:
            return [0]*10

    def save_bitmap(self):
        with open("bitmap.json", "w") as f:
            json.dump(self.bitmap, f)

    # ---------------- NEW: FILE STORAGE ----------------
    def load_files(self):
        try:
            with open("storage.json", "r") as f:
                data = json.load(f)
                self.files = data.get("files", {})
                self.data = data.get("data", {})
                self.directories = data.get("directories", {"root": {}})
                self.access_count = data.get("access_count", {})
        except:
            pass

    def save_files(self):
        with open("storage.json", "w") as f:
            json.dump({
                "files": self.files,
                "data": self.data,
                "directories": self.directories,
                "access_count": self.access_count
            }, f)

    # ---------------- ORIGINAL + ENHANCED ----------------
    def create_file(self, name, size, directory="root"):
        if name in self.files:
            return "❌ File already exists"

        blocks = []

        # original allocation logic
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

        # NEW
        self.data[name] = ""
        self.access_count[name] = 0

        # directory mapping
        if directory not in self.directories:
            self.directories[directory] = {}

        self.directories[directory][name] = "file"

        self.save_bitmap()
        self.save_files()

        return f"✅ {name} → {blocks}"

    # ---------------- ORIGINAL + ENHANCED ----------------
    def delete_file(self, name):
        if name not in self.files:
            return "❌ File not found"

        for b in self.files[name]:
            self.bitmap[b] = 0

        del self.files[name]

        # NEW cleanup
        self.data.pop(name, None)
        self.access_count.pop(name, None)

        self.save_bitmap()
        self.save_files()

        return f"🗑 {name} deleted"

    # ---------------- ORIGINAL ----------------
    def show_bitmap(self):
        return self.bitmap

    def crash(self):
        self.files = {}
        return "💥 System crashed!"

    def get_files(self):
        return self.files

    # ---------------- NEW: WRITE FILE ----------------
    def write_file(self, name, content):
        if name not in self.files:
            return "❌ File not found"

        self.data[name] = content
        self.access_count[name] += 1

        self.save_files()
        return "✍️ Data written"

    # ---------------- NEW: READ FILE ----------------
    def read_file(self, name):
        if name not in self.files:
            return "❌ File not found"

        self.access_count[name] += 1
        return self.data.get(name, "")

    # ---------------- NEW: DIRECTORY ----------------
    def create_directory(self, name):
        if name in self.directories:
            return "❌ Directory already exists"

        self.directories[name] = {}
        self.save_files()

        return f"📁 Directory {name} created"

    def get_directory(self, name="root"):
        return self.directories.get(name, {})

    # ---------------- NEW: RECOVERY SUPPORT ----------------
    def restore_files(self, recovered):
        self.files = {}

        for i, blocks in enumerate(recovered):
            name = f"recovered_{i}"
            self.files[name] = blocks
            self.data[name] = ""
            self.access_count[name] = 0

        self.save_files()

    # ---------------- NEW: ACCESS STATS ----------------
    def get_access_count(self, name):
        return self.access_count.get(name, 0)

    # ---------------- NEW: BITMAP IMPROVEMENTS ----------------
    def reset_bitmap(self):
        self.bitmap = [0] * len(self.bitmap)
        self.files = {}
        self.data = {}
        self.access_count = {}
        self.directories = {"root": {}}

        self.save_bitmap()
        self.save_files()

        return "🔄 Disk reset"

    def validate_bitmap(self):
        used_blocks = set()

        for blocks in self.files.values():
            used_blocks.update(blocks)

        for i in range(len(self.bitmap)):
            if self.bitmap[i] == 1 and i not in used_blocks:
                return f"⚠️ Inconsistency at block {i}"

        return "✅ Bitmap consistent"

    def get_free_blocks(self):
        return [i for i, b in enumerate(self.bitmap) if b == 0]

    def bitmap_visual(self):
        return "".join(["█" if b == 1 else "_" for b in self.bitmap])