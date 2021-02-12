try:
    from .production import *
except ImportError:
    try:
        from .local import *
    except ImportError as e:
        print(e)
        e.args = tuple(["%s did you create production.py?" %(e.args[0])])
        raise e
