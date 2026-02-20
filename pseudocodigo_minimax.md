# Pseudocódigo del Laberinto Minimax

A continuación, se presenta la lógica del programa explicada en español simple, ideal para comprender la arquitectura del código durante una presentación.

---

## 1. Módulos y Reglas Generales

```text
IMPORTAR MÓDULO "Aleatoriedad" (Para posicionar el queso)
IMPORTAR MÓDULO "Matemáticas"  (Para usar números infinitos en Minimax)
IMPORTAR MÓDULO "Tiempo"       (Para pausar la animación)
IMPORTAR MÓDULO "Sistema"      (Para limpiar la consola)

CONSTANTE Tamaño_Tablero = 5
CONSTANTE Profundidad_Vision_Futura = 8

FUNCIÓN Cuales_Son_Los_Movimientos_Posibles( Posición_Actual ):
    Crear una lista vacía de posibles_rutas
    
    SI puedo ir Arriba sin salirme del tablero ENTONCES añadir a posibles_rutas
    SI puedo ir Abajo sin salirme del tablero ENTONCES añadir a posibles_rutas
    SI puedo ir Izquierda sin salirme del tablero ENTONCES añadir a posibles_rutas
    SI puedo ir Derecha sin salirme del tablero ENTONCES añadir a posibles_rutas
    
    DEVOLVER posibles_rutas

FUNCIÓN Distancia_Física( Casilla_A, Casilla_B ):
    Medir los pasos en línea recta horizontal y vertical entre la Casilla A y Casilla B
    DEVOLVER pasos
```

---

## 2. La Inteligencia del Gato (Minimax)

```text
FUNCIÓN Evaluar_Tablero_Imaginario( Gato, Ratón, Queso, Nivel_De_Profundidad ):
    SI el Gato atrapó al Ratón:
        # Gran victoria. Entre más rápido lo atrapes (mayor nivel), mejor.
        DEVOLVER 100 puntos + Nivel_De_Profundidad
    
    SI el Ratón comió el Queso:
        # Pésimo para el Gato.
        DEVOLVER -100 puntos - Nivel_De_Profundidad
        
    # Si nadie ha ganado todavía en este futuro imaginario:
    # Al Gato le conviene que el Ratón esté cerca de él, y lejos del queso.
    Puntuación = -Distancia(Gato, Ratón) + Distancia(Ratón, Queso)
    DEVOLVER Puntuación


FUNCIÓN Algoritmo_Minimax( Gato, Ratón, Queso, Turnos_Al_Futuro, Es_Turno_Gato, Alfa, Beta ):
    
    SI alguien ya ganó O Ya no puedo ver más al futuro (Turnos = 0):
        DEVOLVER Evaluar_Tablero_Imaginario(...)

    SI Es_Turno_Gato (Buscamos la Puntuación Máxima):
        Mejor_Puntos_Gato = Peor Puntuación Posible (-Infinito)
        PARA CADA Movimiento_Posible DEL Gato:
            Puntos = Algoritmo_Minimax( Simular_Tablero, Turnos - 1, Turno_Raton )
            Mejor_Puntos_Gato = Elegir_El_Mayor( Mejor_Puntos_Gato, Puntos )
            # PODA ALFA-BETA: Si esta rama ya demostró ser peor que otra que calculé antes, dejo de buscar aquí.
        
        DEVOLVER Mejor_Puntos_Gato

    SI Es_Turno_Raton (Buscamos la Puntuación Mínima):
        Peor_Puntos_Para_Gato = Mejor Puntuación Posible (+Infinito)
        PARA CADA Movimiento_Posible DEL Ratón:
            Puntos = Algoritmo_Minimax( Simular_Tablero, Turnos - 1, Turno_Gato )
            Peor_Puntos_Para_Gato = Elegir_El_Menor( Peor_Puntos_Para_Gato, Puntos )
            # PODA ALFA-BETA
            
        DEVOLVER Peor_Puntos_Para_Gato


FUNCIÓN Decidir_Siguiente_Paso_Gato( Gato, Ratón, Queso ):
    Revisar_Todas_Mis_Opciones = Cuales_Son_Los_Movimientos_Posibles(Gato)
    Mejor_Paso = Mi_Posicion
    Meilleur_Futuro = -Infinito
    
    PARA CADA Opcion EN Revisar_Todas_Mis_Opciones:
        # Miro 8 turnos al futuro para esta opción
        Puntuación_Del_Futuro = Algoritmo_Minimax( Opcion, Ratón, Queso, 8 turnos... )
        
        SI Puntuación_Del_Futuro es mayor a mi Meilleur_Futuro:
            Meilleur_Futuro = Puntuación_Del_Futuro
            Mejor_Paso = Opcion
            
    # Me muevo hacia donde el algoritmo calculó que está mi mejor futuro
    DEVOLVER Mejor_Paso
```

---

## 3. Lógica Principal (El Bucle del Juego)

```text
REPETIR INFINITAMENTE (Para Modo Espectador Animado):

    Limpiar_Pantalla_De_Consola()
    
    Configurar Posición_Gato en esquina superior izquierda
    Configurar Posición_Ratón en esquina inferior derecha
    Colocar_Queso_Al_Azar()
    
    Dibujar_Tablero_En_Pantalla()
    Esperar( 1 Segundo )

    REPETIR POR 50 TURNOS MÁXIMO (Una Partida Normal):
        
        Limpiar_Pantalla_De_Consola()
        
        # --- TURNO DEL RATÓN ---
        # El ratón usa heurística simple para acercarse al queso y alejarse del gato
        Mejor_Plan = Quedarse_Quieto
        Mejor_Puntuacion = -Infinito
        
        PARA CADA Movimiento_Posible DEL Ratón:
            Puntuacion = (Acercarme_Al_Queso * 2) - (Acercarme_Al_Gato * 1)
            SI Gato_Me_Come_En_Ese_Movimiento:
                Puntuacion = Puntuacion - 1000
                
            SI Puntuacion es mayor a Mejor_Puntuacion:
                Mejor_Puntuacion = Puntuacion
                Mejor_Plan = Ese_Movimiento
                
        Posición_Ratón = Mejor_Plan
        
        SI Ratón_Llegó_Al_Queso O Gato_Atrapó_Al_Ratón:
            Dibujar_Tablero()
            Anunciar_Ganador()
            Terminar_Partida() # Rompe este bucle de 50 turnos
        
        # --- TURNO DEL GATO ---
        # El gato invoca todo el cerebro de la inteligencia artificial (Minimax)
        Posición_Gato = Decidir_Siguiente_Paso_Gato( Posición_Gato, Posición_Ratón, Queso )
        
        Dibujar_Tablero_En_Pantalla()
        
        SI Gato_Atrapó_Al_Ratón:
            Anunciar_Ganador()
            Terminar_Partida() # Rompe este bucle de 50 turnos
            
        Esperar( 0.5 Segundos ) # Da efecto de animación fluida

    # Cuando alguien gana, se acaba la partida...
    Mensaje("Reiniciando en 3 segundos...")
    Esperar( 3 Segundos )
    # ...y el bucle infinito vuelve a empezar una nueva partida arriba.
```
