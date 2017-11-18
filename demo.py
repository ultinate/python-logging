import yaml
import logging

import bar
import foo

log = logging.getLogger(__name__)


def setup_logging():
    with open('log_config.yaml') as f:
        conf = yaml.load(f)
        logging.config.dictConfig(conf)


def main():
    log.info('Entering main ...')
    log.debug('This is a demo for logging.')
    f = foo.Foo()
    f.do_foo(42)
    bar.bar()
    log.info('Leaving main ...')


if __name__ == '__main__':
    main()

