INITIAL_CAPACITY = 8
HASH_CST = 31
MAX_LOAD = 0.75

class HashTable:
    """Mapa clave -> valor.
    Representacion:
        self.buckets : lista de longitud m; cada casilla es una lista de pares (clave, valor)
        self.n       : numero de pares guardados (NO es len(self.buckets))
    9 metodos
    """
    def __init__(self, capacity=INITIAL_CAPACITY):
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    def _hash(self, key):
        total = 0
        for c in key:
            total = total*HASH_CST + ord(c)
        return total % len(self.buckets)

    def _find(self, key):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.buckets[index]):
            if k == key:
                return (index, i)
        return (index, None)

    def _resize(self):
        old_buckets = self.buckets
        new_buckets = [[] for _ in range(2*len(old_buckets))]
        self.buckets = new_buckets
        for bucket in old_buckets:
            for k,v in bucket:
                index = self._hash(k)
                pair = (k, v)
                self.buckets[index].append(pair)

    def put(self, key, value):
        pair = (key, value)
        index, i = self._find(key)
        if i is not None:
            self.buckets[index][i] = pair
            return
        self.buckets[index].append(pair)
        self.size += 1

        if self.size / len(self.buckets) > MAX_LOAD:
            self._resize()

    def get(self, key):
        index, i = self._find(key)
        if i is not None:
            return self.buckets[index][i][1] # 0-key, 1-value
        raise KeyError(key)

    def delete(self, key):
        index, i = self._find(key)
        if i is not None:
            del self.buckets[index][i]
            self.size -= 1
            return
        raise KeyError(key)

    def __contains__(self, key):
        _, i = self._find(key)
        return i is not None

    def __len__(self):
        return self.size