# Name: Robert Mooy
# Section: 09

# Data Definition
# A HuffNode is a
# Binary Tree which consists of
# Binary Tree
# Number
# String
class HuffmanNode:
	def __init__(self, char, freq):
		self.char = char  # actually the character code (number)
		self.freq = freq  # is a number
		self.code = None  # is a string
		self.left = None  # is a BT
		self.right = None # is a BT

   # add any necessary functions you need

# Node Node -> Boolean
# Returns true if tree rooted at node a comes before tree rooted at node b 
def comes_before(a, b):
    if a.freq < b.freq:
       return True
    if a.freq == b.freq:
       if a.char < b.char:
          return True
       else:
          return False
    else:
       return False

# File -> List
# Returns a list of length 256 and counts the frequency/occurance of each character in the file
def cnt_freq(filename):
    alist = [0] * 256
    textlist = []
    try:
       text = open(filename, encoding='utf-8-sig')
    except FileNotFoundError:
       raise IOError("File not Found")
    for line in text:
       for char in line:
           textlist.append(char)
    textlist = textlist[:-1]
    if len(textlist) == 0:
       return None
    #insert_sort_helper(textlist)
    for char in textlist:
        cnt = 0
        for char2 in textlist:
           if char == char2:
              cnt += 1
              alist[ord(char)] = cnt
    text.close()
    return alist 

# List -> Value
# The function is given a list, and it performs an insertion sort on the list, returns a sorted list
def insert_sort_helper(alist):
    for pos in range(1, len(alist)):
        index = pos
        value = alist[index]
        while index > 0 and value < alist[index-1]:
           alist[index] = alist[index-1]
           index -= 1
           alist[index] = value
    return alist

# List -> BT
# Is given a list of frequencies and creates a BT of the list. It returns the root of the BT 
def create_huff_tree(char_freq):
    nodes = []
    if char_freq == None:
       return None
       
    for i in range(0, 256):
       if char_freq[i] != 0:
          node = HuffmanNode(i, char_freq[i])
          nodes.append(node)
    while len(nodes) > 1:
       node = findMin(nodes)
       nodes.remove(node)
       node2 = findMin(nodes)
       nodes.remove(node2)

       freq = (node.freq + node2.freq)
       char = min_helper(node.char, node2.char)
       newnode = HuffmanNode(char, freq)
       newnode.left = node
       newnode.right = node2
       nodes = [newnode] + nodes
    return nodes[0]

# Num Num -> Num
# Determines if a is smaller than b, or vice-versa
# Helper function for create_huff_tree
def min_helper(nodechar1, nodechar2):
    if nodechar1 < nodechar2:
       return nodechar1
    else:
       return nodechar2

# List -> Num
# Finds the minimum in a list of nodes
# Helper function for create_huff_tree
def findMin(alist):
    min = alist[0]
    for i in range(0, len(alist)):
        cur = alist[i]
        if comes_before(cur, min):
           min = cur
    return min

# Node -> List
# Returns a list of the character's respective integer ASCII representation
def create_code(node):
    alist = [""] * 256
    code_helper(node, alist)
    return alist

# Node Str -> List
# Finds the code for each character and returns it to the correct position in the list
# Helper function for create_code
def code_helper(node, alist, cd = ""):
    if node.left != None:
       code_helper(node.left, alist, cd + "0")
    if node.right != None:
       code_helper(node.right, alist, cd + "1")
    if node.left == None and node.right == None:
       node.code = cd
       alist[node.char] = node.code

# File -> File
# Takes a file of characters and returns and new file with the encoded characters
def huffman_encode(in_file, out_file):
   textlist = []
   try:
      text = open(in_file, encoding='utf-8-sig')
   except FileNotFoundError:
      raise IOError("File not Found")
   outfile = open(out_file, 'w') 
   for line in text:
       for char in line:
           textlist.append(char)
   if len(textlist) == 0:
      text.close()
      outfile.close()
      return
   text.close()
   freqs = cnt_freq(in_file)
   hufftree = create_huff_tree(freqs)
   code = create_code(hufftree)
   with open(in_file, encoding='utf-8-sig') as infile:
         text = infile.read()
         for line in text:
            for char in line:
               encodedtext = code[ord(char)]
               outfile.write(encodedtext)
   outfile.write("\n")
   infile.close()
   outfile.close() 

# List File -> File
# Takes a frequency list and an encoded characters file and returns a new file with the decoded characters
def huffman_decode(freqs, encoded_file, decode_file):
    hufftree = create_huff_tree(freqs)
    textlist = []
    text = open(encoded_file, encoding='utf-8-sig')
    for line in text:
       for char in line:
           textlist.append(char)
    outfile = open(decode_file, 'w')
    charlist = decode_helper(hufftree)
    string = decode_helper2(textlist, hufftree)
    for i in charlist:
        char = i * freqs[ord(i)]
        outfile.write(char)
    text.close()
    outfile.close()

# List Node Num String -> String
# Helper function for huffman_decode. Finds the character for each code and adds it to the string
def decode_helper2(text, tree, index = 0, string = ""):
    for i in text:
        index += 1
        if i == "1":
           if tree.right == None:
              string = string + chr(tree.char)
           else:
              decode_helper2(text[index:], tree.right, index)
        if i == "0":
           if tree.left == None:
              string = string + chr(tree.char)
           else:
              decode_helper2(text[index:], tree.left, index)
    return string

# Tree List -> List
# Helper function for huffman_decode. Returns a list of each character in the tree.
def decode_helper(hufftree, alist = []):
    if hufftree != None:
       if chr(hufftree.char) not in alist:
          alist += [chr(hufftree.char)]
       decode_helper(hufftree.left, alist)
       decode_helper(hufftree.right, alist)
    return alist[::-1]

# BT -> String
# Takes a tree and returns a string that states where each letter is on the tree. 0 = leaf node and 1 = node
def tree_preord(node):
    if node.char == None:
       return ""
    return preord_helper(node)

# Node String -> String
# Is the helper function for tree_preorder that traverses through each node and gives leaf nodes a "0" value and nodes "1"
def preord_helper(node, result = ""):
    if node.right != None and node.left != None:
       result += "1"
       preord_helper(node.left, result)
       result += chr(node.char)
       preord_helper(node.right, result)
    if node.right == None and node.left == None:
       result += "0"       
    return result
