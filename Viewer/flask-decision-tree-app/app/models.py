class DecisionNode:
    def __init__(self, id, name, average_prediction, left_child=None, right_child=None):
        self.id = id
        self.name = name
        self.average_prediction = average_prediction
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return f'<DecisionNode {self.name}: {self.average_prediction}>'

class DecisionTree:
    def __init__(self):
        # Пример инициализации дерева вручную
        self.root = DecisionNode(1, 'Root', 50.0,
                                 left_child=DecisionNode(2, 'Left Child', 30.0),
                                 right_child=DecisionNode(3, 'Right Child', 70.0))

    def get_prediction(self, node_id):
        # Поиск узла по id
        node = self._find_node(self.root, node_id)
        return node.average_prediction if node else None

    def _find_node(self, current_node, node_id):
        if current_node is None:
            return None
        if current_node.id == node_id:
            return current_node
        left_result = self._find_node(current_node.left_child, node_id)
        if left_result:
            return left_result
        return self._find_node(current_node.right_child, node_id)