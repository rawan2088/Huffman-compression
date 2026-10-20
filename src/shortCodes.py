import math

def shortCode_generator(text: str)-> dict:
    distinctChars = list(set(text))

    distinctChars.sort()
    numOfBits  = math.ceil(math.log2(len(distinctChars)))

    result = {}
    for i in range(distinctChars):
        result[distinctChars[i]] =  f"{i:0{numOfBits}b}" 

    return result
    

                           

