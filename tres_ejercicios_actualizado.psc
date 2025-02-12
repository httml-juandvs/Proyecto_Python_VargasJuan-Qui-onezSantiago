
Algoritmo tres_ejercicios
    Definir ejercicio como entero

    Escribir "�Qu� ejercicio quiere hacer? (1, 2, 3)"
    Leer ejercicio

    Si ejercicio = 1 Entonces
        mostrarDiaSemana
    Sino Si ejercicio = 2 Entonces
        numeroNegativo_positivo
    Sino Si ejercicio = 3 Entonces
        Definir valorCompra Como Real
        Definir resultado Como Texto

        Escribir "Ingrese el valor de la compra:"
        Leer valorCompra

        resultado <- CalcularDescuentoYTotal(valorCompra)
        Escribir resultado
    Sino
        Escribir "Ejercicio no implementado."
    Fin Si
Fin Algoritmo

Funcion mostrarDiaSemana
    Definir diaSemana como entero

    Escribir "�Qu� d�a de la semana quieres? (1: Lunes, 2: Martes, ..., 7: Domingo)"
    Leer diaSemana

    Segun diaSemana Hacer
        1: Escribir "Lunes"
        2: Escribir "Martes"
        3: Escribir "Mi�rcoles"
        4: Escribir "Jueves"
        5: Escribir "Viernes"
        6: Escribir "S�bado"
        7: Escribir "Domingo"
        De Otro Modo:
            Escribir "Opci�n no v�lida. Debes ingresar un n�mero entre 1 y 7."
    Fin Segun
Fin Funcion

Funcion numeroNegativo_positivo
    Escribir "Digita el n�mero:"
    Leer numer0

    Si numer0 < 0 Entonces
        Escribir "N�mero negativo"
    SiNo Si numer0 > 0 Entonces
        Escribir "N�mero positivo"
    SiNo
        Escribir "No es ni positivo ni negativo"
    Fin Si
Fin Funcion

Funcion CalcularDescuentoYTotal(valorCompra: Real): Texto
    Definir descuento, totalPagar Como Real

    // Determinar el descuento seg�n el valor de la compra
    Si valorCompra < 500000 Entonces
        descuento <- 0
    Sino Si valorCompra >= 500000 Y valorCompra <= 1000000 Entonces
        descuento <- valorCompra * 0.10
    Sino
        descuento <- valorCompra * 0.19
    Fin Si

    // Calcular el total a pagar despu�s del descuento
    totalPagar <- valorCompra - descuento

    // Retornar los resultados como un texto formateado
    Retornar "Descuento aplicado: $" + ConvertirATexto(descuento) + ", Total a pagar: $" + ConvertirATexto(totalPagar)
Fin Funcion
