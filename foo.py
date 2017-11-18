import logging
logger = logging.getLogger(__name__)


class Foo:

    def __init__(self):
        pass

    def do_foo(self, error_code=''):
        logger.info('Initializing Foo ...')
        logger.debug('Arguments: error={}'.format(error_code))
        if error_code:
            logger.error('Error "{}"'.format(error_code))
