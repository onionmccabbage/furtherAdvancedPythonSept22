from collections import namedtuple
# we invoke pytest like this:
# python -m pytest using_pytest.py

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
# we can set sensible defaults
Task.__new__.__defaults__ = (None, None, False, None)
# here are some pytests to exercise our named tuple

def test_default():
    '''using no parameters should invoke the defaults'''
    t1 = Task() # invokes the defaults
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    '''check that we can acces members of a named tuple using dot notation'''
    t = Task('have a cup of tea', 'Ada')
    assert t.summary == 'have a cup of tea'
    assert t.owner   == 'Ada'
    assert (t.done, t.id) == (False, None)