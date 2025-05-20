import pytest
from shortestpath2220674052.shortestpath import dijkstra, get_shortest_path, create_graph_from_edges


def test_create_graph_from_edges():
    print("\nTest: create_graph_from_edges başlıyor...")
    edges = [
        ('A', 'B', 5),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('C', 'D', 2)
    ]
    
    expected_graph = {
        'A': {'B': 5, 'C': 3},
        'B': {'C': 1},
        'C': {'D': 2},
        'D': {}
    }
    
    result = create_graph_from_edges(edges)
    print(f"Oluşturulan graf: {result}")
    print(f"Beklenen graf: {expected_graph}")
    assert result == expected_graph
    print("Test: create_graph_from_edges başarılı!")


def test_dijkstra():
    print("\nTest: dijkstra başlıyor...")
    graph = {
        'A': {'B': 5, 'C': 3},
        'B': {'C': 1},
        'C': {'D': 2},
        'D': {}
    }
    
    distances, predecessors = dijkstra(graph, 'A')
    
    expected_distances = {
        'A': 0,
        'B': 5,
        'C': 3,
        'D': 5
    }
    
    expected_predecessors = {
        'A': None,
        'B': 'A',
        'C': 'A',
        'D': 'C'
    }
    
    print(f"Hesaplanan mesafeler: {distances}")
    print(f"Beklenen mesafeler: {expected_distances}")
    print(f"Hesaplanan öncüller: {predecessors}")
    print(f"Beklenen öncüller: {expected_predecessors}")
    
    assert distances == expected_distances
    assert predecessors == expected_predecessors
    print("Test: dijkstra başarılı!")


def test_get_shortest_path():
    print("\nTest: get_shortest_path başlıyor...")
    graph = {
        'A': {'B': 5, 'C': 3},
        'B': {'C': 1},
        'C': {'D': 2},
        'D': {}
    }
    
    path, distance = get_shortest_path(graph, 'A', 'D')
    print(f"Test 1 - A'dan D'ye en kısa yol:")
    print(f"Bulunan yol: {path}")
    print(f"Toplam mesafe: {distance}")
    
    assert path == ['A', 'C', 'D']
    assert distance == 5
    print("Test 1 başarılı!")
    
    # Test path not found
    print("\nTest 2 - Yol bulunamama durumu testi:")
    graph = {
        'A': {'B': 1},
        'B': {'C': 1},
        'C': {},
        'D': {}
    }
    
    path, distance = get_shortest_path(graph, 'A', 'D')
    print(f"Bulunan yol: {path}")
    print(f"Toplam mesafe: {distance}")
    
    assert path is None
    assert distance is None
    print("Test 2 başarılı!")
    print("\nTüm testler başarıyla tamamlandı!")

if __name__ == '__main__':
    print("Testler başlıyor...")
    test_create_graph_from_edges()
    test_dijkstra()
    test_get_shortest_path()
    print("\nTüm testler başarıyla tamamlandı!")