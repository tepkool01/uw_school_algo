import pytest
from hw import Dijkstras

graph = {
    'kirkland': {'seattle': 11.1, 'renton': 16.7},
    'seattle': {'kirkland': 11.1, 'renton': 12.2, 'burien': 10.4},
    'burien': {'seattle': 10.4, 'renton': 8.6},
    'renton': {'burien': 8.6, 'seattle': 12.2, 'kirkland': 16.7}
}


@pytest.fixture
def dijkstras():
    return Dijkstras(graph)


def test_dijkstras(dijkstras):
    assert dijkstras.get_shortest_distance('kirkland', 'kirkland') == 0
    assert dijkstras.get_shortest_distance('kirkland', 'seattle') == 11.1
    assert dijkstras.get_shortest_distance('kirkland', 'burien') == 21.5
    assert dijkstras.get_shortest_distance('kirkland', 'renton') == 16.7
