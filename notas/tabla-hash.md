# Tabla hash — notas

Contestadas de memoria el 7 nov 2026, tres dias despues de implementarla.
Resultado: 6 de 8 correctas. Formato en `_plantilla.md`.

## 1. Por que un array da acceso O(1), y que dos condiciones impone al indice
**R:** el acceso es por aritmetica de indices: con la primera posicion puedes llegar al resto
por suma. Las dos condiciones no me salen; supongo que una es que sean contiguos.
**Correccion:** PARCIAL. La direccion es `base + i * tamano_del_elemento` — hay
multiplicacion, no solo suma. Que sean contiguos y del mismo tamano es el *motivo* de que
sea O(1), no las condiciones. Las dos condiciones son **del indice**: que sea un **entero**
y que este en **`[0, m)`**.

## 2. Las dos piezas que convierten una clave en un indice, y de que depende cada una
**R:** la clave se transforma en un entero mediante una funcion hash, y ese entero se divide
por el numero de buckets; el resto indica la posicion y nunca se sale del rango.
**Correccion:** correcta. Vocabulario: se divide por el **numero de buckets** (`m`), no por
"el tamano de los buckets". El hash depende solo de la clave; la compresion depende de la
clave **y de `m`**.

## 3. Por que `total = total * 31 + ord(c)` y no una suma simple
**R:** una suma simple puede dar colisiones; la forma con pesos no las evita pero reduce
mucho la probabilidad.
**Correccion:** IMPRECISA en lo esencial. No es probabilidad. La suma colisiona
**sistematicamente** en todos los anagramas: `"roma"` y `"amor"` colisionan siempre. Los
pesos hacen la funcion **sensible al orden** y eliminan esa familia entera. Las colisiones
siguen siendo inevitables (claves infinitas, `m` finito), pero dejan de ser sistematicas.

## 4. Que es un bucket y por que guarda el par completo y no solo el valor
**R:** da almacenamiento dentro de una posicion de la tabla para que las claves que colisionan
(mismo resto) puedan pertenecer a la misma posicion, y dentro de ella se buscan por su
posicion al acceder a la clave del par.
**Correccion:** correcta salvo el final. Dentro del bucket se busca **comparando claves**,
recorriendo. La posicion no sirve para buscar: se obtiene *como resultado* de la busqueda y
solo se usa para sustituir o borrar.

## 5. Que hace `put` cuando la clave ya existe, y por que no puede hacer `append` a ciegas
**R:** sustituye el elemento existente por otro con el valor nuevo; con `append` se podrian
duplicar. Al usar tuplas, que son inmutables, hay que reemplazarlo por completo.
**Correccion:** correcta. La ambiguedad es el motivo de fondo: con dos pares de la misma
clave, `get` no sabe cual devolver.

## 6. Que es el factor de carga y cual es el coste de `get` en funcion de el
**R:** el cociente que determina el porcentaje de ocupacion de los buckets; si es elevado hay
muchos mas pares que buckets, hay colisiones y la busqueda se hace pesada al recorrer dobles
bucles dentro de las colisiones de un bucket. Mantenerlo bajo conserva el O(1).
**Correccion:** DOS ERRORES. (a) No es un porcentaje y puede pasar de 1: con 800 pares en 8
buckets, `alpha = 100`. Es el **numero medio de pares por bucket**. (b) `get` tiene **un solo
bucle**: calcula el indice (constante) y recorre **un** bucket. El doble bucle solo existe en
`_resize`, el unico metodo que visita todos los cajones. Bien lo ultimo: acotar `alpha` es lo
que conserva el O(1).

## 7. Por que el resize obliga a recolocar todos los pares
**R:** porque al cambiar el numero de buckets cambia el indice que calcula la funcion hash
respecto a ese tamano, y copiarlos provocaria inconsistencias.
**Correccion:** correcta. Precision: lo concreto es que los pares quedarian en cajones donde
`get` **no los va a buscar**, porque `get` calcula el indice con la `m` nueva. Se vuelven
inalcanzables aunque sigan en memoria.

## 8. Peor caso de `get` y en que situacion ocurre
**R:** cuando hay colisiones; habria que buscar por dobles bucles dentro de los buckets hasta
encontrar la deseada.
**Correccion:** INCORRECTA, arrastra el error de la 6. El peor caso es que **todas** las
claves caigan en el mismo bucket (funcion hash mala, o claves elegidas adrede contra ella).
Ese bucket tiene los `n` pares y `get` recorre `n` elementos: **O(n)**, con un solo bucle. La
tabla degenera en una lista enlazada.

---

## Huecos reales a repasar

1. Las dos condiciones del indice (pregunta 1).
2. Cuantos bucles recorre `get` — uno, no dos — y de ahi su peor caso (preguntas 6 y 8).

## Lista de espera (no ahora)

- `hash()` de Python: por que aleatoriza entre procesos.
- Direccionamiento abierto y tombstones.
- Por que se eligen primos (31, y `m` primo en vez de potencia de 2).
- Que hace a un objeto hashable y por que una lista no puede ser clave.
- `_hash` solo admite claves `str`: con un `int` revienta.
