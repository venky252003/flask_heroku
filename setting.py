from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = "postgres://ADL_ADMIN:P0stg4_2017@10.246.5.211:5444/ADL"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False