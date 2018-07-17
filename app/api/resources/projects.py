from flask import request
from flask_restful import Resource

projects = []

class Projects(Resource):

    def get(self):
        return {'projects': projects}

class Project(Resource):

    def get(self, id):

        project = next(filter(lambda x: x['id'] == id, projects), None)
        return {'project': project}, 200 if project else 404

    def post(self, id):

        # if id already exists
        if next(filter(lambda x: x['id'] == id, projects), None):
            # bad request
            return {'msg': 'project with id {} already exists'.format(id)}, 400

        data = request.get_json(force=True)
        project = {
            'id': id,
            'name': data['name']
            }
        projects.append(project)
        return {'project': project}, 201

    def delete(self, id):

        global projects

        projects = list(filter(lambda x: x['id'] != id, projects))
        return {'msg':'project deleted'}
