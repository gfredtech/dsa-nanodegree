import sys
from collections import Counter


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root


def insert_element_into_list(node, sorted_frequencies):
    for index, element in enumerate(sorted_frequencies):
        if node.value < element.value:
            sorted_frequencies.insert(index, node)
            break
        elif index == len(sorted_frequencies) - 1:
            sorted_frequencies.append(node)
            break
    pass


def encode_tree(root, string, encodes):
    if root.right is None and root.left is None:
        encodes[root.key] = string
    else:
        if root.left is not None:
            encode_tree(root.left, string + "0", encodes)
        if root.right is not None:
            encode_tree(root.right, string + "1", encodes)


def huffman_encoding(data):
    if not data:
        return data, None
    else:
        frequencies = Counter(data)
        sorted_frequencies = frequencies.most_common()
        mapped_frequencies = list(map(lambda x: Node(x[0], x[1]), sorted_frequencies))
        tree = None

        while len(mapped_frequencies) > 1:
            first_element = mapped_frequencies.pop(0)
            second_element = mapped_frequencies.pop(0)
            root_node = Node(first_element.value + second_element.value, first_element.value + second_element.value)
            root_node.left = first_element
            root_node.right = second_element
            insert_element_into_list(root_node, mapped_frequencies)
            if len(mapped_frequencies) == 0:
                tree = Tree(root_node)
        if tree is None and len(mapped_frequencies) == 1:
            first_element = mapped_frequencies.pop(0)
            tree = Tree(Node(first_element.value, first_element.value))
            tree.root.left = Node(first_element.key, first_element.value)

        encoded_characters = dict()
        encode_tree(tree.root, '', encoded_characters)
        encoded_string = ''
        for char in data:
            encoded_string += encoded_characters[char]
        return encoded_string, tree


def huffman_decoding(data, root):
    if root is None:
        return data

    def decode(data, root, index, decoded_string):
        if root.left is None and root.right is None:
            decoded_string += root.key
            return index, decoded_string
        elif data[index] == "0":
            return decode(data, root.left, index + 1, decoded_string)
        else:
            return decode(data, root.right, index + 1, decoded_string)

    index = 0
    decoded_string = ""
    while index <= len(data) - 1:
        index, decoded_string = decode(data, root, index, decoded_string)
    return decoded_string
    pass


def character_frequencies(data):
    frequencies = dict()
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def sort_frequencies(data):
    items = list(data.items())
    items.sort(key=lambda x: x[1])
    return items


def test(a_great_sentence):
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree.root)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


test('The bird is a word')
test('f')
test('AAAAAAA')
