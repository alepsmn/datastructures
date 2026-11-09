# Plantilla de notas por estructura

Las mismas 8 preguntas para toda estructura. Son lo minimo para decir que la controlas:
si las ocho tienen respuesta, puedes reimplementarla y defenderla.

Formato de cada seccion:

    ## N. <pregunta>
    **R:** lo que contestaste de memoria.
    **Correccion:** lo que estaba mal, o "correcta".

Reglas:
- Contestar de memoria, sin mirar el codigo ni la conversacion. Si no sale, `??` y seguir.
- Un hueco marcado es informacion. Un hueco tapado es deuda.
- No apuntar lo que se puede re-derivar o consultar (constantes, formulas). Apuntar el mecanismo.

## Las 8 preguntas

1. **Que problema resuelve** y cual es la operacion que la justifica frente a la alternativa
   mas simple (normalmente un array o una lista de Python).
2. **Representacion:** que atributos tiene el objeto y que invariantes se cumplen siempre
   entre ellos.
3. **Mecanismo central:** la idea que la hace funcionar, en dos o tres frases. Es la pregunta
   que mas pesa.
4. **Operaciones:** pasos de cada una y su coste. Decir cuantos bucles recorre cada una.
5. **Casos frontera:** la lista de ramas del codigo (vacio, un solo elemento, extremos,
   duplicados). Aqui viven los bugs.
6. **Contrato de errores:** que lanza y cuando, y por que esa excepcion y no otra.
7. **Peor caso** de la operacion principal y en que situacion concreta ocurre.
8. **Decisiones de diseno:** que elegiste pudiendo elegir otra cosa, y el argumento.
