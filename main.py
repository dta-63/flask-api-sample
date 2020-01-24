import os
from logging.config import fileConfig
import connexion
from connexion.resolver import MethodViewResolver

fileConfig(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config/logging.cfg'), disable_existing_loggers=False)

# Create the application instance
app = connexion.App(__name__, specification_dir='openapi')
app.app.config.from_pyfile(os.getenv('APP_SETTINGS_PATH') or 'config/dev.cfg')

options = {"swagger_ui": True}
app.add_api('api.yml', options=options, resolver=MethodViewResolver('api'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
