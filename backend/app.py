from flask import Flask
from flask import Blueprint
from endpoints.blueprint import register_blueprints

app = Flask(__name__)


if __name__ == "__main__":
    bp = Blueprint('endpoints', __name__)
    register_blueprints(bp)
    app.register_blueprint(bp)
    app.run(debug=False)
