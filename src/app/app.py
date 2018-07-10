from utils import factory

application = factory.bootstrap_app()
if application.config['DEBUG']:
    import ptvsd, time
    ptvsd.enable_attach(secret=None,address=('0.0.0.0',3000))
    time.sleep(10)
if __name__ == '__main__':
    application.run(host='0.0.0.0')

