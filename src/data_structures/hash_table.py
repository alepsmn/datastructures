"""Tabla hash con encadenamiento (cada bucket guarda una lista de pares)."""

CAPACIDAD_INICIAL = 8
CARGA_MAXIMA = 0.75

class HashTable:
    """Mapa clave -> valor.
    Representacion:
        self.buckets : lista de longitud m; cada casilla es una lista de pares (clave, valor)
        self.n       : numero de pares guardados (NO es len(self.buckets))
    """

    def __init__(self, capacidad=CAPACIDAD_INICIAL):
        """Crea m buckets vacios y pone n a 0."""
        self.buckets = [[] for _ in range(capacidad)]
        self.n = 0

    def _find(self, clave):
        """Metodo interno auxiliar creado por mi - refactor"""
        index = self._hash(clave)
        for i, (k, _) in enumerate(self.buckets[index]): # recorre solo el bucket del index indicado
            if k == clave:
                return (index, i)
        return (index, None)

    def _hash(self, clave):
        """Devuelve el INDICE de bucket de esta clave: un entero en [0, m).
        Dos pasos, no los mezcles: entero a partir de la clave, y luego % m.
        """
        total = 0
        for c in clave:
            total = total*31 + ord(c)
        return total % len(self.buckets)
    
    def put(self, clave, valor):
        """Inserta el par, o sobrescribe el valor si la clave ya estaba.
        n solo aumenta cuando la clave es nueva.
        Al final, si el factor de carga pasa de CARGA_MAXIMA, redimensiona.
        """
        pair = (clave, valor)
        index, i = self._find(clave)
        if i is not None:
            self.buckets[index][i] = pair
            return
        self.buckets[index].append(pair)

        self.n += 1
        if self.n/len(self.buckets) > CARGA_MAXIMA:
            self._resize()

    def get(self, clave):
        """Devuelve el valor de la clave. KeyError si no esta."""
        index, i = self._find(clave)
        if i is not None:
            return self.buckets[index][i][1]

        raise KeyError(clave)

    def __contains__(self, clave):
        """True si la clave esta en la tabla. Habilita `clave in tabla`."""
        _, i = self._find(clave)
        return i is not None

    def __len__(self):
        """Numero de pares guardados. Habilita `len(tabla)`."""
        return self.n

    def _resize(self):
        """Duplica m y recoloca TODOS los pares en la tabla nueva.
        Ojo: el indice depende de m, asi que no sirve copiar los buckets tal cual.
        """
        old_buckets = self.buckets
        new_buckets = [[] for _ in range(2*len(old_buckets))]
        self.buckets = new_buckets
        for bucket in old_buckets:
            for k,v in bucket:
                index = self._hash(k)
                pair = (k, v)
                self.buckets[index].append(pair)

    def delete(self, clave):
        """Elimina el par. KeyError si no esta. (Hazlo al final, cuando el resto este verde.)"""
        index, i = self._find(clave)
        if i is not None:
            del self.buckets[index][i]
            self.n -= 1
            return
        raise KeyError(clave)
