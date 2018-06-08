from .factory import bootstrap_app
application = bootstrap_app()

if __name__ == '__main__':
    application.run(host='0.0.0.0')
