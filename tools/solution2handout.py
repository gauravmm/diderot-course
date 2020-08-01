#!/usr/bin/env python3

import json
import argparse
from pathlib import Path

def main(args):
    ip = json.loads(args.input.read_bytes().decode("UTF-8"))

    # Change cells
    num_removed = 0
    new_cells = []
    for c in ip["cells"]:
        if c["cell_type"] == "code":
            if ("## SOLUTION ##" in "".join(c["source"])):
                num_removed += 1
                continue
            else:
                c["outputs"] = []
                c["execution_count"] = None
        c["metadata"] = {}
        new_cells.append(c)

    ip["cells"] = new_cells
    print(f"Removed {num_removed} cells; new document has {len(new_cells)} cells.")

    args.output.write_bytes(json.dumps(ip).encode("UTF-8"))


if __name__ == "__main__":
    p = argparse.ArgumentParser("Strip code cells starting with `## SOLUTION ##` from ipynb files.")
    p.add_argument("input", type=Path)
    p.add_argument("output", type=Path)
    main(p.parse_args())
