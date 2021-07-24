class Items(object):
    def __init__(self, count=0, name=""):
        self.data = (name, count)
        pass

    def set_item(self, idx, val):
        print " setting item value to "
        self.data[idx] = val

    def get_item(self, item):
        return self._data[item]

    @property
    def name(self):
        return self.data[0]

    @property
    def count(self):
        return self.data[1]

class Cart(object):
    items = Items()

    def __init__(self, cartItem=0, cost=0.0):
        self.__cart = [cartItem, cost]
        pass


    def



