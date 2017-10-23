from marshpillow import *
from benchlingapi.base import *


@add_schema
class Folder(MyBase):
    items = {}

    FIELDS = ["name"]
    RELATIONSHIPS = [
        Many("sequences", "where Folder.id <> Sequence.folder")
    ]

    def create(self):
        super().create(only=("name", "description", "type", "owner"))

@add_schema
class Primer(MyBase):
    FIELDS = ["bases", "bind_position", "color", "start", "end", "strand", "overhang_length"]


@add_schema
class Annotation(MyBase):
    items = {}
    FIELDS = ["name", "start", "end", "color", "strand", "type", "description", "editURL", "length"]


@add_schema
class Sequence(MyBase):
    items = {}

    FIELDS = ["id"]
    RELATIONSHIPS = [
        One("folder", "find Sequence.folder <> Folder.id"),
    ]
    annotations = fields.Nested(Annotation.Schema, many=True)
    primers = fields.Nested(Primer.Schema, many=True)

@add_schema
class Entity(MyBase):

    FIELDS = ["id", "name"]

    @classmethod
    def me(cls):
        return cls.find("me")