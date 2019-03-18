from flask import Flask

from flask_graphql import GraphQLView
from flask_cors import CORS

from schema import schema


def create_app(config_name):
    app = Flask(__name__)
    app.debug = True
    CORS(app)

    app.add_url_rule(
        '/sm',
        view_func=GraphQLView.as_view(
            'sm',
            schema=schema,
            graphiql=True
        )
    )
    
    return app
