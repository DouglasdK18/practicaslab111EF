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

#------------incisos---------------------
vida=3
h=0
preg=[Pin1,Pin2,Pin3,Pin4,Pin5,Pin6,Pin7,Pin8,Pin9,Pin10]

def incisos():
        vida=3
        h=0
        while(vida != 0):
            h=h+1
            if(h==1):
                print(preg[0])
                jug=input()
                jug.lower()
                if(jug=="c"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) Chile")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==2):
                print(preg[1])
                jug=input()
                jug.lower()
                if(jug=="b"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) Ripeo")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==3):
                print(preg[2])
                jug=input()
                jug.lower()
                if(jug=="c"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso c) El Conde Lucanor")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==4):
                print(preg[3])
                jug=input()
                jug.lower()
                if(jug=="a"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso a) Pablo Neruda")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==5):
                print(preg[4])
                jug=input()
                jug.lower()
                if(jug=="b"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) Anduve")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==6):
                print(preg[5])
                jug=input()
                jug.lower()
                if(jug=="b"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) Arena de Verona")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==7):
                print(preg[6])
                jug=input()
                jug.lower()
                if(jug=="b"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) Astigmatismo")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==8):
                print(preg[7])
                jug=input()
                jug.lower()
                if(jug=="b"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) Niza")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==9):
                print(preg[8])
                jug=input()
                jug.lower()
                if(jug=="b"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) Verde")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==10):
                print(preg[9])
                jug=input()
                jug.lower()
                if(jug=="b"):
                    print("Correcto!")
                    print ("")
                else:
                    vida=vida-1
                    print("Incorrecto era el inciso b) 1998")
                    print("te quedan ",vida," vidas")
                    print ("")
            elif(h==10):
                print("Ganaste!... Enhorabuena")
                print ("")


#------------faciles --------------
def faciles():
        vida1=3
        h=0
        preg1=[Pfa1,Pfa2,Pfa3,Pfa4,Pfa5,Pfa6,Pfa7,Pfa8,Pfa9,Pfa10]
        while(vida1 != 0):
            h=h+1
            if(h==1):
                print(preg1[0])
                jug=input()
                jug.lower()
                if(jug=="timon"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era timon")
                    print("te quedan ",vida1," vidas")
            elif(h==2):
                print(preg1[1])
                jug=input()
                jug.lower()
                if(jug=="tijeras" or jug=="tijera"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era tijera")
                    print("te quedan ",vida1," vidas")
            elif(h==3):
                print(preg1[2])
                jug=input()
                jug.lower()
                if(jug=="cangrejo"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era cangrejo")
                    print("te quedan ",vida1," vidas")
            elif(h==4):
                print(preg1[3])
                jug=input()
                jug.lower()
                if(jug=="4" or jug=="cuatro"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era cuatro")
                    print("te quedan ",vida1," vidas")
            elif(h==5):
                print(preg1[4])
                jug=input()
                jug.lower()
                if(jug=="agujas" or jug=="aguja"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era aguja")
                    print("te quedan ",vida1," vidas")
            elif(h==6):
                print(preg1[5])
                jug=input()
                jug.lower()
                if(jug=="obtusangulo"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era obtusangulo")
                    print("te quedan ",vida1," vidas")
            elif(h==7):
                print(preg1[6])
                jug=input()
                jug.lower()
                if(jug=="genesis"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era genesis")
                    print("te quedan ",vida1," vidas")
            elif(h==8):
                print(preg1[7])
                jug=input()
                jug.lower()
                if(jug=="mejor"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era mejor")
                    print("te quedan ",vida1," vidas")
            elif(h==9):
                print(preg1[8])
                jug=input()
                jug.lower()
                if(jug=="turbulencia"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era turbulencia")
                    print("te quedan ",vida1," vidas")
            elif(h==10):
                print(preg1[9])
                jug=input()
                jug.lower()
                if(jug=="star wars"):
                    print("Correcto!")
                else:
                    vida1=vida1-1
                    print("Incorrecto era star wars")
                    print("te quedan ",vida1," vidas")
            elif(h==10):
                print("Ganaste!... Enhorabuena")
                print ("")
                
#------------normales --------------
def normales():
        vida2=3
        h=0
        preg2=[Pno1,Pno2,Pno3,Pno4,Pno5,Pno6,Pno7,Pno8,Pno9,Pno10]
        while(vida2 != 0):
            h=h+1
            if(h==1):
                print(preg2[0])
                jug=input()
                jug.lower()
                if(jug=="amnesia"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era amnesia")
                    print("te quedan ",vida2," vidas")
            elif(h==2):
                print(preg2[1])
                jug=input()
                jug.lower()
                if(jug=="cubo"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era cubo")
                    print("te quedan ",vida2," vidas")
            elif(h==3):
                print(preg2[2])
                jug=input()
                jug.lower()
                if(jug=="12"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era 12")
                    print("te quedan ",vida2," vidas")
            elif(h==4):
                print(preg2[3])
                jug=input()
                jug.lower()
                if(jug=="66"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era 66")
                    print("te quedan ",vida2," vidas")
            elif(h==5):
                print(preg2[4])
                jug=input()
                jug.lower()
                if(jug=="atlantico"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era atlantico")
                    print("te quedan ",vida2," vidas")
            elif(h==6):
                print(preg2[5])
                jug=input()
                jug.lower()
                if(jug=="hioides"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era hioides")
                    print("te quedan ",vida2," vidas")
            elif(h==7):
                print(preg2[6])
                jug=input()
                jug.lower()
                if(jug=="nueve" or jug=="9"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era nueve")
                    print("te quedan ",vida2," vidas")
            elif(h==8):
                print(preg2[7])
                jug=input()
                jug.lower()
                if(jug=="antonio lopez" or jug=="antonio lopez garcia"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era antonio lopez garcia")
                    print("te quedan ",vida2," vidas")
            elif(h==9):
                print(preg2[8])
                jug=input()
                jug.lower()
                if(jug=="14 de junio de 1940" or jug=="14/06/1940"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era 14/06/1940")
                    print("te quedan ",vida2," vidas")
            elif(h==10):
                print(preg2[9])
                jug=input()
                jug.lower()
                if(jug=="cazado"):
                    print("Correcto!")
                else:
                    vida2=vida2-1
                    print("Incorrecto era cazado")
                    print("te quedan ",vida2," vidas")
            elif(h==10):
                print("Ganaste!... Enhorabuena")
                print ("")  
#------------dificiles --------------
def dificiles():
        vida3=3
        h=0
        preg3=[Pdi1,Pdi2,Pdi3,Pdi4,Pdi5,Pdi6,Pdi7,Pdi8,Pdi9,Pdi10]
        while(vida3 != 0):
            h=h+1
            if(h==1):
                print(preg3[0])
                jug=input()
                jug.lower()
                if(jug=="centripeta"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era centripeta")
                    print("te quedan ",vida3," vidas")
            elif(h==2):
                print(preg3[1])
                jug=input()
                jug.lower()
                if(jug=="dinosaurios"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era dinosaurios")
                    print("te quedan ",vida3," vidas")
            elif(h==3):
                print(preg3[2])
                jug=input()
                jug.lower()
                if(jug=="torre eiffel"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era torre eiffel")
                    print("te quedan ",vida3," vidas")
            elif(h==4):
                print(preg3[3])
                jug=input()
                jug.lower()
                if(jug=="emulsionar"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era emulsionar")
                    print("te quedan ",vida3," vidas")
            elif(h==5):
                print(preg3[4])
                jug=input()
                jug.lower()
                if(jug=="descafeina"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era descafeina")
                    print("te quedan ",vida3," vidas")
            elif(h==6):
                print(preg3[5])
                jug=input()
                jug.lower()
                if(jug=="alejandro magno"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era alejandro magno")
                    print("te quedan ",vida3," vidas")
            elif(h==7):
                print(preg3[6])
                jug=input()
                jug.lower()
                if(jug=="guadalajara"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era guadalajara")
                    print("te quedan ",vida3," vidas")
            elif(h==8):
                print(preg3[7])
                jug=input()
                jug.lower()
                if(jug=="pi" or jug=="3.14"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era pi")
                    print("te quedan ",vida3," vidas")
            elif(h==9):
                print(preg3[8])
                jug=input()
                jug.lower()
                if(jug=="19" or jug=="xix"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era xix")
                    print("te quedan ",vida3," vidas")
            elif(h==10):
                print(preg3[9])
                jug=input()
                jug.lower()
                if(jug=="ph"):
                    print("Correcto!")
                else:
                    vida3=vida3-1
                    print("Incorrecto era ph")
                    print("te quedan ",vida3," vidas")
            elif(h==10):
                print("Ganaste!... Enhorabuena...")
                print ("")
#----------------------------------------
while True:
	menu()
	opcionMenu = input("inserta un numero valor:  ")
	if opcionMenu=="1":
		print ("")
		input("Dificulad facil...como un paseo por el parque :D (presiona cualquier tecla para continuar)")
		faciles()
	elif opcionMenu=="2":
		print ("")
		input("Dificultad normal...wow te gustan los retos :/ (presiona cualquier tecla para continuar)")
		normales()
	elif opcionMenu=="3":
		print ("")
		input("Dificultad dificil...suerte...la precisaras :'v (presiona cualquier tecla para continuar)")
		dificiles()
	elif opcionMenu=="4":
		print ("")
		input("Dificultad moderada...lo divertido acaba de empezar (presiona cualquier tecla para continuar)")
		incisos()
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


