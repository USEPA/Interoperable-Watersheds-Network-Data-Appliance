from util import factory
import ptvsd


# ptvsd.enable_attach(None, address=('0.0.0.0',5001))
# ptvsd.wait_for_attach()

application = factory.bootstrap_app()

if __name__ == '__main__':
    application.run(host='0.0.0.0')

