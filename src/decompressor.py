import json
from .shortCodes import shortCode_generator


def decompress(bits: str, huffman_codes: dict, short_codes: dict, original_length: int) -> str:
    reverse_huff = {code: ch for ch, code in huffman_codes.items()}
    reverse_short = {code: ch for ch, code in short_codes.items()}
    num_bits = len(next(iter(short_codes.values()))) if short_codes else 0

    result = []
    buffer = ""
    i = 0
    while len(result) < original_length:
        buffer += bits[i]
        i += 1

        if buffer in reverse_huff:
            ch = reverse_huff[buffer]
            if ch == "others":
                code = bits[i:i + num_bits]
                i += num_bits
                result.append(reverse_short[code])
            else:
                result.append(ch)
            buffer = ""
    return "".join(result)

def decompress_file(in_path: str, out_path: str):
    with open(in_path, "rb") as f:
        header = json.loads(f.readline().decode("utf-8"))
        value = int.from_bytes(f.read(), "big")
 
    n = header["n_bits"]
    bits = f"{value:0{n}b}" if n else ""

    short_codes = header["shortCodes"]
    text = decompress(bits, header["huffman"], short_codes, header["length"])
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)