import os

from src.compressor import compress_file
from src.decompressor import decompress_file


if __name__ == "__main__":
    mode = input("Compress or decompress? (c/d): ").strip().lower()
    src = input("Input file: ").strip()
    dst = input("Output file: ").strip()
 
    if mode == "c":
        minLimit = float(input("Minimum symbol probability (e.g. 0.01): "))
        compress_file(src, dst, minLimit)
    elif mode == "d":
        decompress_file(src, dst)
        print("Done.")
    else:
        print("Please enter c or d.")