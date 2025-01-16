from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DecisionNode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    average_prediction = db.Column(db.Float, nullable=False)
    left_child_id = db.Column(db.Integer, db.ForeignKey('decision_node.id'))
    right_child_id = db.Column(db.Integer, db.ForeignKey('decision_node.id'))

    left_child = db.relationship('DecisionNode', remote_side=[id], backref='left_child_ref', lazy=True)
    right_child = db.relationship('DecisionNode', remote_side=[id], backref='right_child_ref', lazy=True)

    def __repr__(self):
        return f'<DecisionNode {self.name}: {self.average_prediction}>'