
import heapq

class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman():
    n = int(input("Enter number of characters: "))
    heap = []

    for i in range(n):
        ch = input("Enter character: ")
        freq = int(input("Enter frequency: "))
        heapq.heappush(heap, Node(ch, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new = Node(left.ch + right.ch, left.freq + right.freq)
        new.left = left
        new.right = right

        heapq.heappush(heap, new)

    def display(node, code=""):
        if node.left:
            display(node.left, code + "0")
        if node.right:
            display(node.right, code + "1")
        if not node.left and not node.right:
            print(node.ch, ":", code)

    display(heap[0])

huffman()
