# DRAW_BEAM
Dibujo automático de secciones transversales de vigas, hasta 3 filas de aceros superiores e inferiores

#PEQUEÑO EJEMPLO

Buen dia con todos.
-Esta versión de prueba esta limitado, como se observa
solo esta disponible para dibujar una fila, en la parte superior
e inferior.

USO : 
- PASOS:
 Paso 1: Abrir el AutoCad o Civil 3D en el formato CAD
 Paso 2 : Colocar el nombre de la viga
 Paso 3: Cargas los estilos de texto y cota disponibles en su documento
 Paso 4: Colocar datos de la geometria en "metros" ejemplo :
			Base = 0.25m 
			Altura = 0.50m
			Recubrimiento = 0.04m
			Longitud de gancho = 0.10m
	Recuerden que estos valores se pueden modificar, de acuerdo
	a su uso.
Paso 5 : Colocar los aceros.
	La cantidad mínima de aceros en las filas son de 2 barras
		En la primera fila SUPERIOR:

			El primer recuadro (N° Barras), colocan la cantidad de barras
			en total.

			El segundo recuadro es para indicar la cantidad parcial de
			barras a usar del total antes colocado.

			El tercer recuadro es para colocar el diametro de las barras 
			colocadas en el recuadro anterior (Cantidad parcial)

			Seguidamente aparecera los botones "ADD" y "REMOVE"
			que sirven para agregar los datos de barra y diámetros
			
			Recordar que si coloca dos aceros en la primera fila superior,
			los dos deben ser del mismo diámetro, ya si son de 3 barras a más
			se debe colocar los mismos diametros de barra a los costados
			y en el centro las barra de menor o mayor diámetro. Revisar 
			EJEMPLO N°01.

		En la primera fila INFERIOR:
			El primer recuadro (N° Barras), colocan la cantidad de barras
			en total.

			El segundo recuadro es para indicar la cantidad parcial de
			barras a usar del total antes colocado.

			El tercer recuadro es para colocar el diametro de las barras 
			colocadas en el recuadro anterior (Cantidad parcial)

			Seguidamente aparecera los botones "ADD" y "REMOVE"
			que sirven para agregar los datos de barra y diámetros.

			Recordar que si coloca dos aceros en la primera fila inferior, 
			los dos deben ser del mismo diámetro, ya si son de 3 barras a más
			se debe colocar los mismos diametros de barra a los costados
			y en el centro las barra de menor o mayor diámetro. Revisar 
			EJEMPLO N°01.

EJEMPLO N° 01:

Dibujar una sección de viga de 0.40m x 0.70m con 4 aceros en la parte superior 2 de 3/4" y
2 de 1/2" y en la parte inferior 5 aceros 2 de 1" y 3 de 5/8"


PASOS EN LA APPLICACIÓN:

DENOMINACIÓN Y ESTILOS
	Nombre de viga : VIGA 101
	ETexto : texto25
	ECota : viga
GEOMETRÍA
	Base = 0.40m
	Altura = 0.70m
	Recubri = 0.04m
	L gancho = 0.10m

ACEROS

	SUPERIOR :
		N°Barras = 4
		Parciales = 1 de 3/4"ADD;
				2  de1/2" ADD; 
				1 de 3/4" ADD.

	INFERIOR :
		N°Barras = 5
		Parciales = 1 de 1"ADD;
				3  de 5/8" ADD; 
				1 de 1" ADD.
Clic en "DIBUJAR", luego dar clic en el punto que quieren que se dibuje la sección.
