from benchlingapi import *
from marshmallow import pprint
import pytest
from copy import copy


@pytest.fixture
def folders():
    return Folder.all()

# TODO: Presence of "sequences" relationship in folder causes sequences to be an empty list rather than a list of sequence objects
def test_folders(login, folders):
    f = folders[0]
    assert type(f) is Folder

def test_entity(login):
    me = Entity.me()
    print(me.__dict__)

def test_folder_sequences(login, folders):
    f = folders[0]
    seqs = f.sequences
    s = seqs[0]
    assert type(s) is Sequence
    s.update()
    assert type(s.folder) is Folder


def test_folder_create(login, folders):
    me = Entity.me()
    f = Folder(name="NewFolder", description="", owner=me.id, type="ALL")
    r = f.create()
    print(r)


