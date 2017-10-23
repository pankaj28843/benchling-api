from marshpillow import MarshpillowBase
from benchlingapi.api import BenchlingAPI
import os
import inflection

class MyBase(MarshpillowBase):

    items = {}

    @classmethod
    def pluralize(cls):
        return inflection.pluralize(cls.__name__.lower())

    @classmethod
    def all(cls, **data):
        r = BenchlingAPI.session.get(cls.pluralize(), data)
        items = cls.load(r[cls.pluralize()])
        for i in items:
            cls.items[getattr(i, "id")] = i
        return items

    @classmethod
    def find(cls, id):
        r = BenchlingAPI.session.get(os.path.join(cls.pluralize(), str(id)))
        return cls.load(r)

    @classmethod
    def where(cls, data):
        found = []
        for item_key, item in cls.items.items():
            passed = True
            for data_key, data_val in data.items():
                item_val = getattr(item, data_key)
                if item_val != data_val:
                    passed = False
            if passed:
                found.append(item)
        return found

    @classmethod
    def post(cls, data):
        print(data)
        return BenchlingAPI.session.post(cls.pluralize(), data)

    @classmethod
    def delete(cls, id):
        return BenchlingAPI.session.delete(cls.pluralize(), id)

    @classmethod
    def patch(cls, id, data):
        r = BenchlingAPI.session.patch(os.path.join(cls.pluralize(), str(id)), data)
        return r

    # instance methods
    def delete(self):
        return self.__class__.delete(self.id)

    def patch(self):
        r = self.__class__.patch(self.id, self.dump())
        self.update()
        return r

    def dump(self, only=None):
        data = None
        if only is None:
            data = self.__class__.Schema().dump(self).data
        else:
            data = self.__class__.Schema(only=only).dump(self).data
        return dict(data)

    def create(self, only=None):
        return self.__class__.post(self.dump)

    def update(self):
        self.__dict__.update(self.__class__.find(self.id).__dict__)
