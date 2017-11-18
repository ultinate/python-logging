import logging
logger = logging.getLogger(__name__)


def bar():
    logger.info('Entering bar() ...')
    logger.debug('A more detailed debug description.')
