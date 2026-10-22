import math

def shortCode_generator(chars: list)-> dict:
    if not chars:
        return {}
    chars = sorted(chars)

    numOfBits  = max(1, math.ceil(math.log2(len(chars))))

    result = {}
    for i in range(len(chars)):
        result[chars[i]] =  f"{i:0{numOfBits}b}" 

    return result, numOfBits
    

                           

