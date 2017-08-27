class Node(object):
    def __init__(self, e, left = None, right = None):
        self.e = e
        self.left = left  # left is small
        self.right = right  # right is big

    def __str__(self):
        return "{" + str(self.e) + "}"

# def tree_to_list(node):
#     print "starting", node
#     tmp = Node(node.e)
#     if node.left is not None and node.right is not None:
#         left_list = tree_to_list(node.left)
#         right_list = tree_to_list(node.right)
#
#         tmp.left = left_list.left
#         tmp.right = right_list
#         left_list.left.right = tmp
#         left_list.left = right_list.left
#         right_list.left.right = left_list
#         right_list.left = tmp
#
#         tmp = left_list
#
#     elif node.left is not None:
#         left_list = tree_to_list(node.left)
#
#         tmp.left = left_list.left
#         tmp.right = left_list
#         left_list.left.right = tmp
#         left_list.left = tmp
#
#         tmp = left_list
#
#     elif node.right is not None:
#         right_list = tree_to_list(node.right)
#
#         tmp.left = right_list.left
#         tmp.right = right_list
#         right_list.left.right = tmp
#         right_list.left = tmp
#
#     else:
#         tmp.left = tmp
#         tmp.right = tmp
#
#     print "done with", node, " got ", dll_as_str(tmp)
#     return tmp


def tree_to_list(node):
    print "starting", node
    ret = node
    if node.left is not None:

    if node.right is not None:
        left_list = tree_to_list(node.left)
        right_list = tree_to_list(node.right)

        ret.left = left_list.left
        ret.right = right_list
        left_list.left.right = ret
        left_list.left = right_list.left
        right_list.left.right = left_list
        right_list.left = ret

        ret = left_list

    if node.left is not None:
        left = tree_to_list(node.left)

        ret.left = left_list.left
        ret.right = left_list
        left_list.left.right = ret
        left_list.left = ret

        ret = left_list

    elif node.right is not None:
        right_list = tree_to_list(node.right)

        ret.left = right_list.left
        ret.right = right_list
        right_list.left.right = ret
        right_list.left = ret

    else:
        ret.left = ret
        ret.right = ret

    print "done with", node, " got ", dll_as_str(ret)
    return ret

def as_list(input_node, forwards):
    current = input_node
    l = []
    while True:
        l.append(current.e)
        if forwards:
            current = current.right
        else:
            current = current.left
        if current == input_node:
            break
    return l

def dll_as_str(head):
    return str(as_list(head, forwards=True)) + " <-> " + str(as_list(head.left, forwards=False))

one = Node(1)
two = Node(2)
three = Node(3)
one.right = two
two.right = three
three.right = one
one.left = three
two.left = one
three.left = two

#  2
# 1

#     4
#  2     6
# 1 3   5 7
#tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))

# tree from https://en.wikipedia.org/wiki/Binary_search_tree
tree = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, right=Node(14, Node(13))))

dll = tree_to_list(tree)
print as_list(dll, forwards=True)
print as_list(dll.left, forwards=False)

