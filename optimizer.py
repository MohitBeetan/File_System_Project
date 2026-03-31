class Optimizer:
    def __init__(self, bitmap):
        self.bitmap = bitmap

    # ---------------- EXISTING ----------------
    def defragment(self):
        used = [1 for b in self.bitmap if b == 1]
        free = [0] * (len(self.bitmap) - len(used))
        return used + free

    # ---------------- NEW: FRAGMENTATION COUNT ----------------
    def fragmentation_count(self):
        fragments = 0

        for i in range(len(self.bitmap) - 1):
            if self.bitmap[i] == 1 and self.bitmap[i+1] == 0:
                fragments += 1

        return fragments

    # ---------------- NEW: ACCESS TIME ----------------
    def access_time(self):
        base_time = 100  # base time in ms
        fragments = self.fragmentation_count()

        # more fragmentation = more time
        return base_time + (fragments * 25)

    # ---------------- NEW: DISK HEALTH ----------------
    def disk_health(self):
        fragments = self.fragmentation_count()

        if fragments == 0:
            return "🟢 Excellent"
        elif fragments < 3:
            return "🟡 Moderate"
        else:
            return "🔴 Highly Fragmented"

    # ---------------- NEW: PERFORMANCE ----------------
    def performance(self):
        time = self.access_time()

        if time < 120:
            return "⚡ Fast"
        elif time < 180:
            return "⚠️ Medium"
        else:
            return "🐢 Slow"

    # ---------------- NEW: FULL REPORT ----------------
    def report(self):
        return {
            "fragments": self.fragmentation_count(),
            "access_time": self.access_time(),
            "health": self.disk_health(),
            "performance": self.performance()
        }