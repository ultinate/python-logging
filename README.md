Logger demo
===========

Requires python 3.6.

Run `pip install -r requirements.txt` to install dependencies.

Run `python demo.py` for logging demo.


Demonstrated logging behavior
-----------------------------

Each log message is redirected to three places (logging "handlers")
as defined in `log_config.yaml`:
  * console (level INFO and higher)
  * file `debug.log` (level DEBUG and higher)
  * file `error.log` (level ERROR and higher)
