from collections import Counter
import heapq

class HuffmanNode:
    def __init__(self, char=None, freq=0, is_others = False):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.is_others = is_others

# overloading the comparison method
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text: str, minLimit: float) -> HuffmanNode:
    frequency = Counter(text)

    minLimit *= len(text) 

    heap=[]
    others = HuffmanNode(char = "others", is_others = True)
    for char, freq in frequency.items():
        if freq<= minLimit:
            others.freq+= freq
        else:
            node = HuffmanNode(char, freq)
            heapq.heappush(heap, node)    
        # heapq.heappush(heap, node)

    if others.freq > 0: 

        heapq.heappush(heap, others)

    while(len(heap)> 1):
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        combinedNode = HuffmanNode(freq = first.freq + second.freq)
        combinedNode.left = first 
        combinedNode.right = second

        heapq.heappush(heap, combinedNode)

    return heap[0]


def generated_codes(root: HuffmanNode, currentCode: str="", codes: dict = None) -> dict:

    if codes is None:
        codes = {}

    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = currentCode
        return

    generated_codes(root.left, currentCode + "0", codes)
    generated_codes(root.right, currentCode + "1", codes)

    return codes



    
