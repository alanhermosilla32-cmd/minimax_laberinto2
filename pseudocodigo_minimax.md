# Pseudocódigo del Laberinto Minimax

A continuación, se presenta la lógica del programa explicada en español simple, ideal para comprender la arquitectura del código durante una presentación.

---

## 1. Módulos y Reglas Generales

```text
IMPORT MODULE "Aleatoriedad" (Para posicionar el queso)
IMPORT MODULE "Matemáticas"  (Para usar números infinitos en Minimax)
IMPORT MODULE "Tiempo"       (Para pausar la animación)
IMPORT MODULE "Sistema"      (Para limpiar la consola)

CONSTANT Tamaño_Tablero = 5
CONSTANT Profundidad_Vision_Futura = 8

FUNCTION Cuales_Son_Los_Movimientos_Posibles( Posición_Actual ):
    Crear una lista vacía de posibles_rutas
    
    IF puedo ir Arriba sin salirme del tablero THEN añadir a posibles_rutas
    IF puedo ir Abajo sin salirme del tablero THEN añadir a posibles_rutas
    IF puedo ir Izquierda sin salirme del tablero THEN añadir a posibles_rutas
    IF puedo ir Derecha sin salirme del tablero THEN añadir a posibles_rutas
    
    RETURN posibles_rutas

FUNCTION Distancia_Física( Casilla_A, Casilla_B ):
    Medir los pasos en línea recta horizontal y vertical entre la Casilla A y Casilla B
    RETURN pasos
```

---

## 2. La Inteligencia del Gato (Minimax)

```text
FUNCTION Evaluar_Tablero_Imaginario( Gato, Ratón, Queso, Nivel_De_Profundidad ):
    IF el Gato atrapó al Ratón:
        # Gran victoria. Entre más rápido lo atrapes (mayor nivel), mejor.
        RETURN 100 puntos + Nivel_De_Profundidad
    
    IF el Ratón comió el Queso:
        # Pésimo para el Gato.
        RETURN -100 puntos - Nivel_De_Profundidad
        
    # Si nadie ha ganado todavía en este futuro imaginario:
    # Al Gato le conviene que el Ratón esté cerca de él, y lejos del queso.
    Puntuación = -Distancia(Gato, Ratón) + Distancia(Ratón, Queso)
    RETURN Puntuación


FUNCTION Algoritmo_Minimax( Gato, Ratón, Queso, Turnos_Al_Futuro, Es_Turno_Gato, Alfa, Beta ):
    
    IF alguien ya ganó OR Ya no puedo ver más al futuro (Turnos = 0):
        RETURN Evaluar_Tablero_Imaginario(...)

    IF Es_Turno_Gato (Buscamos la Puntuación Máxima):
        Mejor_Puntos_Gato = Peor Puntuación Posible (-Infinito)
        FOR EACH Movimiento_Posible IN Movimientos_Gato:
            Puntos = Algoritmo_Minimax( Simular_Tablero, Turnos - 1, Turno_Raton )
            Mejor_Puntos_Gato = Elegir_El_Mayor( Mejor_Puntos_Gato, Puntos )
            # PODA ALFA-BETA: Si esta rama ya demostró ser peor que otra que calculé antes, dejo de buscar aquí.
            IF Poda_Alfa_Beta_Activa THEN BREAK
        
        RETURN Mejor_Puntos_Gato

    ELSE (Es_Turno_Raton, Buscamos la Puntuación Mínima):
        Peor_Puntos_Para_Gato = Mejor Puntuación Posible (+Infinito)
        FOR EACH Movimiento_Posible IN Movimientos_Ratón:
            Puntos = Algoritmo_Minimax( Simular_Tablero, Turnos - 1, Turno_Gato )
            Peor_Puntos_Para_Gato = Elegir_El_Menor( Peor_Puntos_Para_Gato, Puntos )
            # PODA ALFA-BETA
            IF Poda_Alfa_Beta_Activa THEN BREAK
            
        RETURN Peor_Puntos_Para_Gato


FUNCTION Decidir_Siguiente_Paso_Gato( Gato, Ratón, Queso ):
    Revisar_Todas_Mis_Opciones = Cuales_Son_Los_Movimientos_Posibles(Gato)
    Mejor_Paso = Mi_Posicion
    Meilleur_Futuro = -Infinito
    
    FOR EACH Opcion IN Revisar_Todas_Mis_Opciones:
        # Miro 8 turnos al futuro para esta opción
        Puntuación_Del_Futuro = Algoritmo_Minimax( Opcion, Ratón, Queso, 8 turnos... )
        
        IF Puntuación_Del_Futuro es mayor a mi Meilleur_Futuro:
            Meilleur_Futuro = Puntuación_Del_Futuro
            Mejor_Paso = Opcion
            
    # Me muevo hacia donde el algoritmo calculó que está mi mejor futuro
    RETURN Mejor_Paso
```

---

## 3. Lógica Principal (El Bucle del Juego)

```text
WHILE True (Para Modo Espectador Animado):

    Limpiar_Pantalla_De_Consola()
    
    Configurar Posición_Gato en esquina superior izquierda
    Configurar Posición_Ratón en esquina inferior derecha
    Colocar_Queso_Al_Azar()
    
    Dibujar_Tablero_En_Pantalla()
    Esperar( 1 Segundo )

    FOR Turno = 1 TO 50 (Una Partida Normal MÁXIMO):
        
        Limpiar_Pantalla_De_Consola()
        
        # --- TURNO DEL RATÓN ---
        # El ratón usa heurística simple para acercarse al queso y alejarse del gato
        Mejor_Plan = Quedarse_Quieto
        Mejor_Puntuacion = -Infinito
        
        FOR EACH Movimiento_Posible IN Opciones_Ratón:
            Puntuacion = (Acercarme_Al_Queso * 2) - (Acercarme_Al_Gato * 1)
            IF Gato_Me_Come_En_Ese_Movimiento:
                Puntuacion = Puntuacion - 1000
                
            IF Puntuacion es mayor a Mejor_Puntuacion:
                Mejor_Puntuacion = Puntuacion
                Mejor_Plan = Ese_Movimiento
                
        Posición_Ratón = Mejor_Plan
        
        IF Ratón_Llegó_Al_Queso OR Gato_Atrapó_Al_Ratón:
            Dibujar_Tablero()
            Anunciar_Ganador()
            BREAK # Terminar_Partida, rompe este bucle de 50 turnos
        
        # --- TURNO DEL GATO ---
        # El gato invoca todo el cerebro de la inteligencia artificial (Minimax)
        Posición_Gato = Decidir_Siguiente_Paso_Gato( Posición_Gato, Posición_Ratón, Queso )
        
        Dibujar_Tablero_En_Pantalla()
        
        IF Gato_Atrapó_Al_Ratón:
            Anunciar_Ganador()
            BREAK # Terminar_Partida, rompe este bucle de 50 turnos
            
        Esperar( 0.5 Segundos ) # Da efecto de animación fluida

    # Cuando alguien gana, se acaba la partida...
    Mensaje("Reiniciando en 3 segundos...")
    Esperar( 3 Segundos )
    # ...y el bucle infinito vuelve a empezar una nueva partida arriba.
```
