# Service example

Example of a flask service using Zalando connexion

## Requirements

- Python 3
- Virtual env
- VSCode or an other IDE
  - [Autopep8 extension](https://marketplace.visualstudio.com/items?itemName=himanoa.Python-autopep8)

## Features

- [x] Flask architecture (modular)
- [x] Logger
- [x] Service documentation (Open api)
- [x] Multiple environments with configuration file
- [x] Docker
- [ ] Gitlab CI
- [ ] Mongo connector
- [ ] Authentication (OIDC)
- [x] Gunicorn for unix system (only present in Dockerfile)
- [ ] Call other Web service
- [ ] Unit test
- [ ] Test coverage
- [ ] Cache
- [ ] Kafka connector

## Launch

- Run `./make.sh` to build the virtual env
- Run `python main.py` or use a launcher in VScode for example
- Access to http://127.0.0.1/
- Access to http://127.0.0.1/ui to see open api documentation

## Helpfull links

- [Python virtual env](https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.htmls)
- [Python 3](https://www.python.org/)
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- [Connexion](https://connexion.readthedocs.io/en/latest/quickstart.html)
- [Open api specification](https://swagger.io/specification/)
- [Flask oidc](https://flask-oidc.readthedocs.io/en/latest/)
