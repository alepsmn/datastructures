# Arbol binario de busqueda (BST) — notas

De memoria, sin mirar codigo ni conversacion. Huecos con `??`. Formato en `_plantilla.md`.

Fecha: 8 nov 2026 (frio, varios dias despues). Resultado: 1 correcta (4), 3 parciales (3,5,8),
4 incorrectas (1,2,6,7). La retencion real es baja -> esto justifica el control cronometrado.

## 1. Que le ganas a un array ordenado, si los dos buscan en O(log n)
**R:** Los bst tienen una logica de llenado, se van a un sub arbol u otro dependiendo
de si es mayor o menor  al valor del nodo actual -> ORDEN
**Correccion:** NO RESPONDE. Describes como funciona el BST, pero un array ordenado TAMBIEN
mantiene orden y busca en O(log n) (binaria). El orden no es lo que ganas. Lo que ganas es
`insert`/`delete` en O(log n): en un array ordenado, insertar o borrar obliga a DESPLAZAR
todos los elementos posteriores -> O(n). El BST inserta/borra reenganchando punteros, sin
tocar el resto. Esa es la ventaja, y solo esa.

## 2. Que invariante relaciona un nodo con TODOS sus descendientes (no solo con sus dos hijos), y por que la version "solo los hijos" no basta
**R:** No he entendido del todo la pregunta, diria que es que cada padre tiene la
referencia de solo sus dos hijos, entonces es accesible a cualquier generacion
de descendientes
**Correccion:** INCORRECTA. Confundes la topologia de punteros con el invariante de ORDEN.
El invariante: para CADA nodo, TODO el subarbol izquierdo < nodo.value < TODO el subarbol
derecho. "Solo los hijos no basta" significa esto: que `hijo_izq < padre < hijo_der` se
cumpla en cada nodo NO garantiza un BST. Contraejemplo: raiz 5, hijo izquierdo 3, y 3 tiene
un hijo derecho 6. Localmente 3<5 y 3<6 cumplen, pero 6 esta en el subarbol IZQUIERDO de 5 y
es mayor que 5 -> `search(6)` se iria por la derecha y no lo encontraria. El invariante es
sobre descendientes, no sobre hijos inmediatos.

## 3. Por que cada paso de la busqueda descarta medio arbol, y de que depende ese "medio"
**R:** Esto se da por la condicion del valor del nodo actual, entonces a partir de ella
se elige que arbol descartar para insertar/buscar
**Correccion:** PARCIAL. El mecanismo de descarte, bien: comparas con el nodo y tiras el
subarbol del lado que por el invariante no puede contener el valor. Pero no respondes "de que
depende el medio". Solo descartas de verdad la MITAD si el arbol esta BALANCEADO. En un arbol
degenerado, el lado que descartas puede tener 0 nodos y el otro n-1: descartas casi nada. El
tamano de lo descartado depende del BALANCE. De ahi sale el peor caso (pregunta 7).

## 4. En `insert`/`delete` recursivos, por que la linea es `node.left = self._delete(node.left, v)` y no solo `self._delete(node.left, v)`. Que pasa si te comes la asignacion
**R:** El arbol se pierde, cuando llegas al punto mas bajo en la recursion, vas obteniendo valores que vuelven a sus referencias, por lo que si no se asignan se pierden por el camino
**Correccion:** CORRECTA. Precision: el helper DEVUELVE el subarbol (en `insert`, el caso base
crea un `Node` nuevo y lo retorna). La variable local del hijo no modifica el atributo del
padre; solo la asignacion `node.left = ...` engancha lo devuelto. Sin ella, el nodo creado se
pierde y el arbol no crece -> fue tu bug real: `insert` hacia `return self._insert(...)` sin
asignar `self.root`, y `root` seguia `None` para siempre.

## 5. Los tres casos de `delete` segun el numero de hijos del nodo borrado. En el de dos hijos, que valor concreto sube al hueco y por que ese y no otro
**R:**En este caso uso el del sucesor, es decir el minimo valor del subarbol derecho del
nodo a borrar, de esta manera, al sustituir el valor borrado por este, no entrara en
conflicto para desbalancear el arbol
**Correccion:** PARCIAL. (a) No enumeras los TRES casos: hoja (devuelves None), un hijo
(devuelves el hijo que existe, sube en su lugar), dos hijos (el del sucesor). Solo respondiste
el tercero. (b) El sucesor es correcto, pero el motivo que das es FALSO: no tiene nada que ver
con el balance. El sucesor es el unico valor que preserva el INVARIANTE DE ORDEN: es mayor que
todo el subarbol izquierdo y menor que todo lo demas del derecho, asi que al ponerlo en el
hueco, izquierda sigue siendo menor y derecha mayor. Balance (altura) es otra cosa; aqui no se
toca. Confundes "mantener el orden" con "mantener el balance".

## 6. Que hace `delete` con una clave ausente y que hace `insert` con un duplicado; por que esa eleccion y no lanzar
**R:** Delete devolver el nodo, para mostrar que existe, insert tambien
**Correccion:** INCORRECTA. `delete` de una clave AUSENTE es un no-op silencioso: baja hasta
`node is None`, devuelve None, el arbol queda identico, NO lanza. `insert` de un DUPLICADO lo
ignora: no inserta, devuelve el nodo sin cambios. Por que no lanzar: borrar algo que no esta e
insertar algo que ya esta son operaciones idempotentes, no errores; lanzar obligaria a todo el
que llama a envolver en try/except sin ganar nada. Es la misma decision coherente en las dos
(como `set.discard` en Python). Tu "devolver el nodo para mostrar que existe" no responde al
caso ausente ni al duplicado.

## 7. Peor caso de `search` y con que secuencia concreta de inserciones ocurre
**R:** No lo entiendo del todo pero diria que si se busca un valor cuyo subarbol es muy profundo, por lo que entra en una gran recursion, aunq diria q el problema es memoria mas q tiempo de acceso, no se si desvario
**Correccion:** INCORRECTA, aunque "profundidad" apunta bien. El peor caso de `search` es
O(n), y pasa cuando el arbol DEGENERA en una lista enlazada: insertas en orden creciente (o
decreciente), p.ej. 1,2,3,4,5 -> cada nodo cuelga a la derecha del anterior, altura = n.
Buscar recorre n nodos. El problema es TIEMPO (n comparaciones), no memoria: el coste de
`search` es la ALTURA del arbol. Balanceado -> altura log n -> O(log n); degenerado ->
altura n -> O(n). La pista de profundidad es correcta (profundidad = altura); lo que esta mal
es concluir "memoria" y no dar la secuencia concreta (insercion ya ordenada).

## 8. Decisiones de diseno: elegiste el sucesor (min del subarbol derecho) para el caso de dos hijos; cual era la alternativa simetrica. Y en `insert`, que te ahorra la recursion frente a hacerlo iterativo
**R:** La alternativa era predecesor, es el maximo del subarbol izquierdo, por recursion
ahorra tiempo pero consume memoria para almacenar todas las funciones en accion
**Correccion:** PARCIAL. Predecesor = maximo del subarbol izquierdo: CORRECTA. Pero la
recursion NO ahorra tiempo: es el mismo O(h) que la version iterativa. Lo que te ahorra es
llevar el puntero al PADRE a mano: la pila de llamadas recuerda el camino de vuelta, y por eso
el reenganche `node.left = self._delete(...)` es automatico. Iterativo tendrias que guardar el
padre en una variable aparte para enganchar. El coste de la recursion es memoria O(h) en la
pila. Resumen: no ahorra tiempo, ahorra tener que rastrear el padre; paga con memoria de pila.

---

## Huecos reales a repasar

1. Que ganas frente a un array ordenado: NO es el orden (eso lo da el array tambien), es
   `insert`/`delete` sin desplazar -> O(log n) vs O(n) (preguntas 1 y la idea de coste).
2. El invariante es sobre TODOS los descendientes, no sobre los hijos inmediatos. Saber el
   contraejemplo del nieto que rompe el orden (pregunta 2).
3. Separar dos ejes que mezclas: ORDEN (invariante BST, lo que preserva el sucesor) vs BALANCE
   (altura, de lo que depende el coste). Aparecen en 3, 5 y 7.
4. Peor caso = O(n) por TIEMPO (altura), con insercion ya ordenada que degenera en lista. No
   es un problema de memoria (pregunta 7).
5. Contrato: ausente y duplicado son no-ops silenciosos, no errores; por que (pregunta 6).

## Lista de espera (no ahora)

- Arboles autobalanceados (AVL, rojo-negro): como garantizan altura O(log n) y por que el BST
  simple no lo hace.
- Recorridos: in-order (ordenado), pre-order, post-order, y para que sirve cada uno.
- Borrado con predecesor en vez de sucesor: implementarlo y ver que da un arbol distinto pero
  igual de valido.
