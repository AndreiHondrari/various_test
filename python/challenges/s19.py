"""
Write two functions, one that serializes a binary tree, given its root node and one that deserializes the result of the first function from a string to a binary tree.



    1
   / \
  2   3
 /   / \
8   4   5


class Node:
  Node left
  Node right
  int value
"""

from typing import List




class Node:

  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

  @staticmethod
  def parse_elements(elements: List) -> Node:

    element = elements.pop()
    if element == "N":
     	return None

    nod_curr = Node(
      value=int(element),
      left=parse_elements(elements),
      right=parse_elements(elements)
    )
    return nod_curr

  @staticmethod
  def deserializer_from_string(input_string: str) -> Node:
    elements = input_string.split()
    return parse_elements(elements)

  def serialize_to_string(self, node=None):
    if node is None:
    	return "N"

    node = self if node is None else node
    result += f"{node.value}"
    result += " " + self.serializer_to_string(node=node.left)
    result += " " + self.serializer_to_string(node=node.right)
    return result




"""
X - root
L - left
R - right
N - null
"""

"""
    1
   / \
  2   3
 /   / \
8   4   5
"""
input1 = "1 2 8 N N N 3 4 N N 5 N N"
# input1 = "X1 L2 L8 LN RN RN R3 L4 LN RN R5 LN RN"
