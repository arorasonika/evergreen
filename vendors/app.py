# /books/app.py

from flask import Flask, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS, cross_origin

from .database.db_session import db_session
from .schema.schema import schema

app = Flask(__name__)
app.debug = True

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
  return render_template(
    'index.html',
    js_url='//127.0.0.1:8080/main.bundle.js'
  )

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
