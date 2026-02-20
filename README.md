# Laberinto Minimax con Gato, Ratón y Queso

Proyecto práctico para demostrar la implementación en Python del **Algoritmo Minimax con Poda Alfa-Beta** en un entorno de teoría de juegos (juego de suma cero modificado).

## Descripción del Proyecto

El entorno de simulación consiste en un tablero de 5x5 casillas donde interactúan tres entidades principales:
- **Gato (G):** Busca cazar al Ratón. Actúa como el *Maximizador* en el algoritmo Minimax.
- **Ratón (R):** Busca sobrevivir y comer el Queso. Actúa como el *Minimizador* (simulado) en el árbol de decisiones del Gato.
- **Queso (Q):** Es el objetivo estático del Ratón.

### Condiciones de Victoria
1. **Gana el Gato:** Si logra moverse a la misma casilla que el Ratón antes de que éste coma el queso.
2. **Gana el Ratón:** Si logra llegar a la casilla del Queso sin ser atrapado.

## Características Técnicas y Algoritmos

Este código demuestra conceptos fundamentales de Inteligencia Artificial para juegos:

- **Algoritmo Minimax:** El Gato evalúa un árbol completo de posibles futuros (hasta 8 niveles de profundidad) considerando "Si yo me muevo aquí, el ratón se moverá allá...".
- **Poda Alfa-Beta:** Optimización crucial del Minimax. El algoritmo "poda" (ignora) ramas del árbol de decisiones matemático que ya sabe que son peores que una opción previamente calculada, permitiendo al Gato calcular *muchas más jugadas a futuro* en milisegundos.
- **Función de Evaluación Heurística:** Cuando el juego no ha terminado pero se alcanza el límite de visión (profundidad 0), la IA evalúa la conveniencia del tablero restando la distancia entre el Gato y el Ratón, y sumando la distancia entre el Ratón y el Queso.
- **Desempate Físico y Recompensa por Velocidad:** El algoritmo fue refinado para penalizar simulaciones donde el triunfo tarda más turnos, forzando al Gato a atrapar al Ratón en la menor cantidad de pasos posibles.

## Cómo Ejecutarlo

El proyecto no requiere dependencias externas, utiliza exclusivamente la biblioteca estándar de Python:

```bash
python minimax_lab.py
```