import pytest
from HMapChain import HMapChain


@pytest.fixture
def hmap():
    return HMapChain()


def test_insert(hmap):
    hmap.insert('key1', 100)
    hmap.insert('key2', 200)
    assert hmap.get_by_key('key1') == 100
    assert hmap.get_by_key('key2') == 200


def test_remove(hmap):
    hmap.insert('key1', 100)
    hmap.insert('key2', 200)
    assert hmap.size == 2
    hmap.remove('key1')
    assert hmap.get_by_key('key1') is None
    assert hmap.size == 1


def test_rehash(hmap):
    for i in range(20):
        hmap.insert(f'key{i}', i)

    assert hmap.capacity == 20
    assert hmap.size == 20
    assert hmap.get_by_key('key0') == 0
    assert hmap.get_by_key('key1') == 1
    assert hmap.get_by_key('key2') == 2
    assert hmap.get_by_key('key18') == 18
    assert hmap.get_by_key('key19') == 19
