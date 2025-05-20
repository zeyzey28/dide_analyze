# ShortestPath2220674052

En kısa yol bulucu Python paketi. Bu paket, verilen bir graf üzerinde Dijkstra algoritmasını kullanarak en kısa yolu bulan bir Python paketidir.

## Özellikler

* Graf oluşturma
* Dijkstra algoritması ile en kısa yol hesaplama
* Başlangıç ve bitiş noktaları arasındaki en kısa yolu bulma

## Kurulum

### Test PyPI'dan Kurulum

```bash
pip install --index-url https://test.pypi.org/simple/ shortestpath2220674052==0.1.1
```

### Geliştirici Kurulumu

```bash
git clone https://github.com/zeyzey28/shortestpath.git
cd shortestpath
pip install -e .
```

## Kullanım

### Graf Oluşturma

```python
from shortestpath2220674052.shortestpath import create_graph_from_edges

edges = [
    ('A', 'B', 5),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('C', 'D', 2)
]

graph = create_graph_from_edges(edges)
```

### En Kısa Yol Bulma

```python
from shortestpath2220674052.shortestpath import get_shortest_path

path, distance = get_shortest_path(graph, 'A', 'D')
print(f"En kısa yol: {path}")
print(f"Toplam mesafe: {distance}")
```

### Dijkstra Algoritması

```python
from shortestpath2220674052.shortestpath import dijkstra

distances, predecessors = dijkstra(graph, 'A')
print(f"Tüm mesafeler: {distances}")
print(f"Öncül düğümler: {predecessors}")
```

## Dokümantasyon

Detaylı dokümantasyon için aşağıdaki adımları izleyin:

1. Sphinx bağımlılıklarını yükleyin:
```bash
pip install sphinx sphinx-rtd-theme
```

2. Dokümantasyonu oluşturun:
```bash
cd docs
make html
```

3. Oluşturulan dokümantasyonu görüntüleyin:
```bash
open _build/html/index.html
```

## Testler

Testleri çalıştırmak için:

```bash
python -m pytest tests/test_shortestpath.py -v
```

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## Yazar

Zeynep Oğulcan 