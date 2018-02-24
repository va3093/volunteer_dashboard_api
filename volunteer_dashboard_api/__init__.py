from flask import Flask
from volunteer_dashboard_api.users import users

app = Flask(__name__)
app.register_blueprint(users)

