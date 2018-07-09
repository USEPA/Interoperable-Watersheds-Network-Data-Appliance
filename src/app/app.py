from utils import factory

application = factory.bootstrap_app()

if __name__ == '__main__':
    application.run(host='0.0.0.0')

