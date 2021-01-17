### Observations

* `s2.py` will see `m2.py` from `p1.py` only if imported in `p1/__init__.py`
* `p1/__init__.py` only gets called when `p1` is imported somewhere
* running `python p1` actually executes the code in `p1/__main__.py`
