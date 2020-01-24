from flask.views import MethodView
from flask import current_app as app


class ExampleView(MethodView):
    method_decorators = []

    def get(self, id):
        app.logger.debug('Get on /example/{}'.format(id))
        return 'Test', 200

    def post(self):
        app.logger.debug('Post on /example/')
        return 'OK', 201

    def search(self):
        app.logger.debug('Search on /example/')
        return 'Test', 200
