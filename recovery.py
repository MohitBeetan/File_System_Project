class Recovery:
    def __init__(self, bitmap):
        self.bitmap = bitmap

    # ---------------- EXISTING ----------------
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

    # ---------------- NEW: NAMED RECOVERY ----------------
    def recover_with_names(self):
        recovered = self.recover_files()
        named_files = {}

        for i, blocks in enumerate(recovered):
            name = f"recovered_file_{i}"
            named_files[name] = blocks

        return named_files

    # ---------------- NEW: RECOVERY REPORT ----------------
    def recovery_report(self):
        recovered = self.recover_files()

        total_files = len(recovered)
        total_blocks = sum(len(f) for f in recovered)

        return {
            "files_recovered": total_files,
            "blocks_recovered": total_blocks,
            "details": recovered
        }

    # ---------------- NEW: CORRUPTION CHECK ----------------
    def detect_corruption(self):
        corrupted = []

        for i in range(len(self.bitmap)):
            # simple check: isolated single block (possible corruption)
            if self.bitmap[i] == 1:
                left = self.bitmap[i-1] if i > 0 else 0
                right = self.bitmap[i+1] if i < len(self.bitmap)-1 else 0

                if left == 0 and right == 0:
                    corrupted.append(i)

        return corrupted

    # ---------------- NEW: PARTIAL RECOVERY ----------------
    def partial_recovery(self):
        recovered = self.recover_files()
        valid_files = []
        partial_files = []

        for blocks in recovered:
            if len(blocks) > 1:
                valid_files.append(blocks)
            else:
                partial_files.append(blocks)

        return {
            "valid": valid_files,
            "partial": partial_files
        }