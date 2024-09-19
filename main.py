from flask import Flask

from controllers.players_controller import players_blueprint
from service.main_service import initial_db

app = Flask(__name__)


if __name__ == '__main__':
    app.register_blueprint(players_blueprint, url_prefix="/api/players")

    initial_db()

    app.run(debug=True)
