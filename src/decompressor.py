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