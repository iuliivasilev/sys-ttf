from flask import render_template, jsonify
from .models import DecisionTree

# Главный маршрут для отображения веб-страницы
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для получения средней прогнозируемой величины в узле
@app.route('/node/<int:node_id>')
def get_node_prediction(node_id):
    tree = DecisionTree()  # Предполагается, что DecisionTree инициализирует дерево
    prediction = tree.get_prediction(node_id)  # Получаем прогноз для узла
    return jsonify({'prediction': prediction})