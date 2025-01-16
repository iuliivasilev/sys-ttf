from flask import render_template, jsonify, Blueprint
from .models import DecisionTree

main = Blueprint('main', __name__)

# Главный маршрут для отображения веб-страницы
@main.route('/')
def index():
    tree = DecisionTree()  # Инициализируем дерево вручную
    tree_dict = tree.to_dict()  # Преобразуем дерево в словарь для передачи в шаблон
    return render_template('index.html', tree=tree_dict)

# Маршрут для получения средней прогнозируемой величины в узле
@main.route('/node/<int:node_id>')
def get_node_prediction(node_id):
    tree = DecisionTree()  # Инициализируем дерево вручную
    prediction = tree.get_prediction(node_id)  # Получаем прогноз для узла
    return jsonify({'prediction': prediction})