from itertools import izip_longest


class Node(object):
    def __init__(self, e, left=None, right=None):
        self.e = e
        self.left = left
        self.right = right

    def __str__(self):
        return "{" + str(self.e) + "}"


def render_tree(node):
    if node.left is None and node.right is None:
        return str(node.e)

    if node.left is None:
        left = ''
    else:
        left = render_tree(node.left)

    if node.right is None:
        right = ''
    else:
        right = render_tree(node.right)

    left_lines = left.split('\n')
    left_widest = max([len(l) for l in left_lines])
    print 'left widest is ' + str(left_widest)

    right_lines = right.split('\n')
    right_widest = max([len(l) for l in right_lines])
    print 'right widest is ' + str(right_widest)

    result = (' ' * left_widest) + str(node.e) + (' ' * right_widest)
    print 'for', node.e, 'new str len is ', len(result)
    for (l, r) in izip_longest(left_lines, right_lines, fillvalue=''):
        left_side = l + ' ' * (left_widest - len(l))
        padding = ' ' * len(str(node.e))
        right_side = ' ' * (right_widest - len(r)) + r
        result += '\n' + left_side + padding + right_side

    return result

#        10
#   11        4
# 12  13    12  14
tree = Node(10,
            Node(11,
                 Node(666),
                 Node(13)
                 ),
            Node(4,
                 Node(12,
                      Node(9)
                   ),
                 Node(7555)
                 )
            )

tree = Node(4, Node(12, Node(15, None, Node(16))), Node(14, Node(20, Node(500))))

print render_tree(tree)
