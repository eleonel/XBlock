# from https://github.com/Pylons/pyramid/blob/master/pyramid/decorator.py
class call_once_property(object):
    """ Use as a class method decorator.  It operates almost exactly like the
    Python ``@property`` decorator, but it puts the result of the method it
    decorates into the instance dict after the first call, effectively
    replacing the function it decorates with an instance variable.  It is, in
    Python parlance, a non-data descriptor.  An example:

    .. code-block:: python

       class Foo(object):
           @call_once_property
           def jammy(self):
               print 'jammy called'
               return 1

    And usage of Foo:

    .. code-block:: text

       >>> f = Foo()
       >>> v = f.jammy
       'jammy called'
       >>> print v
       1
       >>> f.jammy
       1
       >>> # jammy func not called the second time; it replaced itself with 1
    """
    def __init__(self, wrapped):
        self.wrapped = wrapped
        try:
            self.__doc__ = wrapped.__doc__
        except: # pragma: no cover
            pass

    def __get__(self, inst, objtype=None):
        if inst is None:
            return self
        val = self.wrapped(inst)
        setattr(inst, self.wrapped.__name__, val)
        return val


def make_safe_for_html(html):
    """Turn the text `html` into a real HTML string."""
    html = html.replace("&", "&amp;")
    html = html.replace(" ", "&nbsp;")
    html = html.replace("<", "&lt;")
    html = html.replace("\n", "<br>")
    return html
