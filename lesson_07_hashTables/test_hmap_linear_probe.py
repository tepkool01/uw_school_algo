import pytest
from HMapLinearProbe import HMapLinearProbe


@pytest.fixture
def hmap():
    return HMapLinearProbe()


def test_insert(hmap):
    hmap.insert('key1', 1)
    hmap.insert('key2', 2)
    assert hmap.get_by_key('key1') == 1
    assert hmap.get_by_key('key2') == 2


def test_remove(hmap):
    hmap.insert('key1', 100)
    hmap.insert('key2', 200)
    assert hmap.size == 2
    hmap.remove('key1')
    assert hmap.size == 1
    assert hmap.get_by_key('key1') is None


def test_rehash(hmap):
    for i in range(10):
        hmap.insert(f'key{i}', i)

    assert hmap.capacity == 20
    assert hmap.size == 10
    assert hmap.get_by_key('key0') == 0
    assert hmap.get_by_key('key1') == 1
    assert hmap.get_by_key('key8') == 8
    assert hmap.get_by_key('key9') == 9
