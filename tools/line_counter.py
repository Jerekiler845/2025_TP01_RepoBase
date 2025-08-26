#!/usr/bin/env python3
import os

def count_lines(root='.'):
    total = 0
    for dirpath, _, filenames in os.walk(root):
        if any(part.startswith('.') for part in dirpath.split(os.sep)):
            continue
        for f in filenames:
            if f.startswith('.'):
                continue
            path = os.path.join(dirpath, f)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
                    total += sum(1 for _ in fh)
            except Exception:
                pass
    return total

if __name__ == "__main__":
    print(count_lines())
