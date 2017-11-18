import yaml
import logging

import bar
from foo import Foo

log = logging.getLogger(__name__)


def setup_logging():
    import logging.config
    with open('log_config.yaml') as f:
        conf = yaml.load(f)
        logging.config.dictConfig(conf)


def main():
    log.info('Entering main ...')
    log.debug('This is a demo for logging.')
    f = Foo()
    f.do_foo(42)
    bar.bar()
    log.info('Leaving main ...')


if __name__ == '__main__':
    setup_logging()
    main()
