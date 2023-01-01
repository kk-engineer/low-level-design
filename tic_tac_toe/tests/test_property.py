class C(object):
    def __init__(self):
        self.x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        print(value)
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x


c = C()
c.x = 'KK'  # setter called
foo = c.x    # getter called
print(foo)
del c.x      # deleter called