from flask import Blueprint, render_template, request
from flask_restful import Api, Resource
from app.api.resources import Project, Projects

api_app = Blueprint('api_app', __name__,
                   # template_folder='templates',
                   url_prefix='/api')

api = Api(api_app)

@api_app.route('/')
def api_home():
    # return render_template('api.html')
    return 'welcome to the api app!'

# add resources
api.add_resource(Project, '/project/<int:id>')
api.add_resource(Projects, '/projects')
