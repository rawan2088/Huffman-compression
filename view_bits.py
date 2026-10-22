import json
import sys

with open(sys.argv[1], "rb") as f:
    header = json.loads(f.readline().decode("utf-8"))
    value = int.from_bytes(f.read(), "big")

n = header["n_bits"]
print(f"{value:0{n}b}" if n else "")