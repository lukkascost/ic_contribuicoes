
from Classes import DecisionTree

tree = DecisionTree()
tr_data, class_, attrs = tree.read_data('resturant.dat')

tree1 = tree.create_tree(tr_data, class_, attrs)

tree.show_tree(tree1, ' ')
