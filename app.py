from flask import Flask

from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_json import FlaskJSON

from schema import schema


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)

    app.add_url_rule(
        '/sm',
        view_func=GraphQLView.as_view(
            'sm',
            schema=schema,
            graphiql=True   # for having the GraphiQL interface
        )
    )
    

    return app
