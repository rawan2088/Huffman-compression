import json

from .HuffmanTree import build_huffman_tree, generated_codes
from .shortCodes import shortCode_generator



def compress(text: str, huffman_codes: dict, short_codes: dict) -> str:
    out = []
    for ch in text:
        if ch in huffman_codes:
            out.append(huffman_codes[ch])
        else:                                       # rare symbol
            out.append(huffman_codes["others"] + short_codes[ch])

    return "".join(out)


def compress_file(in_path, out_path, minLimit):
    with open(in_path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
 
    chars = sorted(set(text))
    root = build_huffman_tree(text, minLimit)
    huffman_codes = generated_codes(root)
    short_codes, numOfBits = shortCode_generator(chars)

    unCompressedSize = numOfBits*len(text)
    bits = compress(text, huffman_codes, short_codes)
    CompressedSize = len(bits)
    header = json.dumps({"length": len(text), "n_bits": len(bits),
            "huffman": huffman_codes, "shortCodes": short_codes}, ensure_ascii=False)
    with open(out_path, "wb") as f:
            f.write(header.encode("utf-8") + b"\n")
            f.write(int(bits or "0", 2).to_bytes((len(bits) + 7) // 8, "big"))

    print(f"Uncompressed Size: {unCompressedSize} \n"
          f"Compressed Size: {CompressedSize}")        
