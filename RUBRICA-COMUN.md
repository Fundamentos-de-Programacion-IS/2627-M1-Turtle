# Rúbrica común de calidad de los hitos

Los hitos **no puntúan por separado**. El **M2** y el **M3** dan **derecho a asiento** en su
control —entrega en plazo *y* que el proyecto se ejecute sin errores—; el **M1 es una práctica
de calentamiento y no condiciona el asiento**. El conjunto de los tres puede aportar hasta
**+0,5** a la nota de teoría. Sólo se valora calidad después de
comprobar que cada entrega está en plazo y se ejecuta; esa comprobación es la misma que
concede el asiento y la hace `scripts/verificar-entregas.sh`.

| Criterio | Evidencia |
|---|---|
| Funcionamiento | supera los casos de `PRUEBAS.md` sin romper la plantilla |
| Comprensión | el grupo puede explicar y modificar las decisiones principales |
| Pruebas | documenta casos normales, límites y errores comprobados |
| Legibilidad | nombres claros, funciones manejables y README actualizado |
| Extensión | mejora útil que conserva el contrato y está probada |

El bonus se asigna globalmente tras M3; no se suman tres bonus de +0,5. Una extensión
que el grupo no pueda explicar o probar no se valora. Se desaconseja la IA generativa;
si se usa puntualmente debe declararse en el README de la entrega.
