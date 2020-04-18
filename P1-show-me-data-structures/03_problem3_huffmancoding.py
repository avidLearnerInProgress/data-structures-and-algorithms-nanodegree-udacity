import sys
from operator import itemgetter

'''
Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.
You then will need to create encoding, decoding, and sizing schemas.
'''

class Node(object):
    def __init__(self):
        self.value, self.left, self.right = None, None, None

    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def set_left_children(self, children):
        self.left = children
        
    def set_right_children(self, children):
        self.right = children
        
    def get_left_children(self):
        return self.left
    
    def get_right_children(self):
        return self.right
    
    def has_left_children(self):
        return self.left != None
    
    def has_right_children(self):
        return self.right != None

    def __repr__(self):
        return f"Node: ({self.get_value()}, {self.has_left_children()}, {self.has_right_children()})"
    
    def __str__(self):
        return f"Node: ({self.get_value()}, {self.has_left_children()}, {self.has_right_children()})"


class Tree(object):
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = value
        
    def get_root(self):
        return self.root


#global variables
hfrequency = dict({})
htree = Tree()
hcode = dict({})

def generate_frequencies(data):
    for letter in data:
        if letter in hfrequency:
            hfrequency[letter] += 1
        else:
            hfrequency[letter] = 1
    return hfrequency

def build_htree(char_freqs):    
    #create nodes beforehand for tree
    char_values = char_freqs
    root_node = None
    while len(char_values) > 1:
        c1, f1 = char_values[-1]
        c2, f2 = char_values[-2]
        char_values = char_values[:-2]
        new_node = Node()
        new_node.set_left_children(c1)
        new_node.set_right_children(c2)
        char_values.append((new_node, f1 + f2))
        char_values.sort(key = itemgetter(1), reverse = True)
        root_node = new_node
    htree.set_root(root_node)    
    return root_node

def traverse_htree(node, code=''):
    if type(node) is str:
        return {node: code}        
    left_node = node.get_left_children()
    right_node = node.get_right_children()
    hcode.update(traverse_htree(left_node, code + "0"))
    hcode.update(traverse_htree(right_node, code + "1"))
    return hcode

def process(data):
    #generate frequencies and sort
    freq_list = list(generate_frequencies(data).items())
    freq_list.sort(key = itemgetter(1), reverse = True)

    #build tree bottom-up and create codes
    traverse_htree(build_htree(freq_list))
    
def hencoding(data):
    if len(data) == 0:
        return ("There was no message encoded as original string is empty!", None)
    encoded_string = ''
    process(data)
    #use lookup map to encode instead of traversing tree
    for char in data:
        encoded_string += hcode[char]
    return encoded_string, htree

def decode_message(data, node):
    if type(node) is str:
        return data, node
    if data[0] == "0" and node.has_left_children():
        return decode_message(data[1:], node.get_left_children())
    elif data[0] == "1" and node.has_right_children():
        return decode_message(data[1:], node.get_right_children())

def hdecoding(data, htree):
    decoded_msg = '' 
    #traverse tree for each char
    while len(data) > 0:
        data, char = decode_message(data, htree.get_root())
        decoded_msg += char
    return decoded_msg

if __name__ == "__main__":
    codes = {}

    #Test case 1
    sentence = "Quick brown fox jumped over the lazy dog"
    print(f"The size of the data is: {sys.getsizeof(sentence)}\n")
    print(f"The content of the data is: {sentence}\n")
    
    encoded_data, tree = hencoding(sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = hdecoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    

    # Test case 2
    another_sentence = "Yet another lllllllllllllllllloooooooooooooooooooooonnnnnnnnnnnnnnnnnggggggggggggggggg string"
    print ("The size of the data is: {}\n".format(sys.getsizeof(another_sentence)))
    print ("The content of the data is: {}\n".format(another_sentence))

    encoded_data, tree = hencoding(another_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = hdecoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    # Test case 3
    yet_another_sentence = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print ("The size of the data is: {}\n".format(sys.getsizeof(yet_another_sentence)))
    print ("The content of the data is: {}\n".format(yet_another_sentence))

    encoded_data, tree = hencoding(yet_another_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = hdecoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    # Test case 4
    yet_one_last_string = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(yet_one_last_string)))
    print ("The content of the data is: {}\n".format(yet_one_last_string))
    encoded_data, tree = hencoding(yet_one_last_string)

    if tree is not None:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        
        decoded_data = hdecoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print(encoded_data)