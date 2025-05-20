Kullanım
=======

Graf Oluşturma
------------

Kenar listesinden graf oluşturmak için :func:`create_graph_from_edges` fonksiyonunu kullanabilirsiniz:

.. code-block:: python

    from shortestpath2220674052.shortestpath import create_graph_from_edges

    edges = [
        ('A', 'B', 5),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('C', 'D', 2)
    ]

    graph = create_graph_from_edges(edges)

En Kısa Yol Bulma
---------------

İki nokta arasındaki en kısa yolu bulmak için :func:`get_shortest_path` fonksiyonunu kullanabilirsiniz:

.. code-block:: python

    from shortestpath2220674052.shortestpath import get_shortest_path

    path, distance = get_shortest_path(graph, 'A', 'D')
    print(f"En kısa yol: {path}")
    print(f"Toplam mesafe: {distance}")

Dijkstra Algoritması
-----------------

Eğer tüm mesafeleri ve öncül düğümleri hesaplamak isterseniz :func:`dijkstra` fonksiyonunu kullanabilirsiniz:

.. code-block:: python

    from shortestpath2220674052.shortestpath import dijkstra

    distances, predecessors = dijkstra(graph, 'A')
    print(f"Tüm mesafeler: {distances}")
    print(f"Öncül düğümler: {predecessors}") 