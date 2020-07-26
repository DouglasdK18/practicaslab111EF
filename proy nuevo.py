# Brian Douglas Velarde Menacho
# c.i: 10931722
import os
#-----------Preguntas Faciles-----------
Pfa1= """¿Como se llama el suricata que acompaña a Simba en la pelicula El Rey Leon?"""
Pfa2= """¿Instrumento de corte con dos brazos movibles utilizado por los sastres?"""
Pfa3= """¿Que animal representa el signo zodiacal Cancer?"""
Pfa4= """¿Cuantas silabas contiene la palabra HISTRIONICO ?"""
Pfa5= """¿Herramienta principal de la acupuntura?"""
Pfa6= """¿Como se llama el triangulo cuyo angulo es mayor de 90° ?"""
Pfa7= """¿En que libro de la biblia se cuenta la historia de Adan y Eva?"""
Pfa8= """¿Cual es el adjetivo comparativo de Bueno?"""
Pfa9= """¿Movimiento desordenado del aire que provoca que un avion se agite durante su vuelo?"""
Pfa10="""¿A que saga cinematografica pertenece el Film La venganza de los Sith?"""

#-----------Preguntas Normales----------
Pno1= """¿Perdida total o parcial de la memoria?"""
Pno2= """¿Con que otro nombre se conoce al hexaedro regular?"""
Pno3= """¿Cual es la raiz de 144?"""
Pno4= """¿Cuantas flores hay en 5 docenas y media?"""
Pno5= """¿En que oceano se encuentra las islas Malvinas?"""
Pno6= """¿Nombre del hueso situado en la base de la lengua y encima de la laringe?"""
Pno7= """¿Cuantas canastas son 18 puntos en Baloncesto?"""
Pno8= """¿Que pintor tardo 20 años en terminar el retrato La familia de Carlos Primero?"""
Pno9= """¿En que fecha se rindio Paris ante los alemanes en la segunda guerra mundial?"""
Pno10="""¿Participio del verbo CAZAR?"""

#-----------Preguntas Dificiles----------
Pdi1="""¿Fuerza contraria a la centrifuga que se mueve hacia el centro o el interior?"""
Pdi2="""¿Cual es el tema principal del museo Dinópolis de Teruel?"""
Pdi3="""¿Monumento frances que se levanto con motivo de exposicion internacional en 1889?"""
Pdi4="""¿EN COCINA, como se dice el batir 2 liquidos, no mezclar entre si con el fin de ligarlos?"""
Pdi5="""¿Tercera persona singular presente del indicativo del verbo Descafeinar?"""
Pdi6="""¿A que rey macedonio representa el rey de treboles de la baraja francesa?"""
Pdi7="""¿Provincia a la que pertenece el parque arqueologico Visigodo de Recópolis?"""
Pdi8="""¿Numero que se obtiene al dividir la longitud de una circunferenia por su diametro?"""
Pdi9="""¿A que siglo pertenece el año 1870?"""
Pdi10="""¿Con que dos letra se expresa el grado de acidez o basicidadde una solucion?"""

#-------Preguntas de incisos------------
Pin1= """¿A que pais pertencen la isla de pascuas?
a) Argentina     b) Chile             c) EEUU"""
Pin2= """¿Proceso a travez del cual se transfiere un contenido multimedia a otro soporte?
a) Trolleo       b) Ripeo             c) Formateo """
Pin3= """¿Cual de estas obras NO es un libro de caballeria?
a) Amadís de Gaula     b) Las sergas de Esplandian     c) El conde Lucanor """
Pin4= """¿Seudomimo con que se concoce al poeta chileno Ricardo Eliécer Neftalí Reyes Basoalto?
a) Pablo Neruda      b) Vicente Huidobro      c) Nicanor Parra """
Pin5= """¿Primera persona singular del preterito perfecto simple del indicativo del verbo andar?
a) Andé          b) Anduve          c) Anduvo """
Pin6= """¿Teatro de Ópera al aire libre ubicado en el anfiteatro romano de Verona?
a) Liceo de Verona        b) Arena de Verona          c) Teatro nacional de Verona """
Pin7= """¿Que transtorno ocular se debe a la curvatura no uniforme de la cornea?
a) Presbicia        b) Astigmatismo         c) Miopía """
Pin8= """¿En que ciudad francesa se encuentra el museo de Marc Chagall?
a) Cannes        b) Niza        c) Marsella """
Pin9= """¿Cual de estos colores no corresponde a una época pictórica de Picasso?
a) Azul        b) Verde         c) Rosa """
Pin10= """¿El 9 de noviembre de que año fue derribado el muro de Berlin?
a) 1987        b) 1989       c) 1992 """

#--------------------Menu----------------
def menu():
	os.system('cls')
	print("")
	print("Te doy la bienvenida al JUEGO DE PREGUNTAS de conocimiento general ")
	print("Reglas sencillas...responde correctamente....solo tienes 3 vidas...")
	print("las vidas son tus oportunidades, piensa bien antes de responder, si llega a cero...fin del juego")
	print("A JUGAR....¿que dificultad quieres probar?")
	print ("Selecciona la dificultad y empecemos :v ")
	print ("\t1 - Dificultad facil...(tienes que escribir la respuesta)")
	print ("\t2 - Dificultad normal...(tienes que escribir la respuesta)")
	print ("\t3 - Dificultad dificil...(tienes que escribir la respuesta)")
	print ("\t4 - Dificultad moderada...(Hay incisos :v) ")
	print ("\t0 - salir (A estado divertido ¿verdad?)")

#------------faciles---------------------
def pregunta1():
    vida=3
    preg=[Pfa1,Pfa2,Pfa3,Pfa4,Pfa5,Pfa6,Pfa7,Pfa8,Pfa9,Pfa10]   
    res=["timon","tijeras","cangrejo","genesis","4","agujas","obtusangulo","mejor","turbulencia","star wars"]
    for i in range(0,10,1):
        print(preg[i])
        jug=input()
        jug.lower()
        if(jug==res[i]):
            print("correcto")
            print ("")
        else:
            vida=vida-1
            print("Incorrecto ")
            print("te quedan ",vida," vidas")
            print ("")
        if(vida==0):
            break
#------------normales---------------------
def pregunta2():
    vida1=3           
    preg1=[Pno1,Pno2,Pno3,Pno4,Pno5,Pno6,Pno7,Pno8,Pno9,Pno10]  
    res1=["amnesia","cubo","12","66","atlantico","hioides","9","antonio lopez garcia","14/06/1940","cazado"]

    for i in range(0,10,1):
        print(preg1[i])
        jug=input()
        jug.lower()
        if(jug==res1[i]):
            print("correcto")
            print ("")
        else:
            vida1=vida1-1
            print("Incorrecto ")
            print("te quedan ",vida1," vidas")
            print ("")
        if(vida1==0):
            break

#------------dificiles---------------------
def pregunta3():
    vida2=3
    preg2=[Pdi1,Pdi2,Pdi3,Pdi4,Pdi5,Pdi6,Pdi7,Pdi8,Pdi9,Pdi10]
    res2=["centripeta","dinosaurios","terro eiffel","emulsionar","descafeina","alejandro magno","gualadajara","pi","19","ph"]
    for i in range(0,10,1):
        print(preg2[i])
        jug=input()
        jug.lower()
        if(jug==res2[i]):
            print("correcto")
            print ("")
        else:
            vida2=vida2-1
            print("Incorrecto ")
            print("te quedan ",vida2," vidas")
            print ("")
        if(vida2==0):
            break
#------------incisos---------------------
def pregunta4():
    vida3=3
    preg3=[Pin1,Pin2,Pin3,Pin4,Pin5,Pin6,Pin7,Pin8,Pin9,Pin10]
    res3=["b","b","c","a","b","b","b","b","b","b"]
    for i in range(0,10,1):
        print(preg3[i])
        jug=input()
        jug.lower()
        if(jug==res3[i]):
            print("correcto")
            print ("")
        else:
            vida3=vida3-1
            print("Incorrecto ")
            print("te quedan ",vida3," vidas")
            print ("")
        if(vida3==0):
            break
#---------------------------------------
while True:
	menu()
	opcionMenu = input("inserta un numero valor:  ")
	if opcionMenu=="1":
		print ("")
		input("Dificulad facil...como un paseo por el parque :D (presiona cualquier tecla para continuar)")
		pregunta1()
	elif opcionMenu=="2":
		print ("")
		input("Dificultad normal...wow te gustan los retos :/ (presiona cualquier tecla para continuar)")
		pregunta2()
	elif opcionMenu=="3":
		print ("")
		input("Dificultad dificil...suerte...la precisaras :'v (presiona cualquier tecla para continuar)")
		pregunta3()
	elif opcionMenu=="4":
		print ("")
		input("Dificultad moderada...lo divertido acaba de empezar (presiona cualquier tecla para continuar)")
		pregunta4()
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



