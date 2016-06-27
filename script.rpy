# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.

image bg escena="fuera_del_pueblo3.png"
image bg interro="sala_interrogatorio.jpg"
image detective = "Grupo7/DetectivePensarr.png"
image art="Grupo5/hablando3.2.png"
image burt="Grupo3/burt1.png"
image carl="Grupo2/Hablando.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el
#   ejemplo.
define e = Character('detective', color="#c8ffc8")
define a = Character('art', color="#c8ffc8")
define b = Character('burt',color="#c8ffc8")
define c = Character('carl',color="#c8ffc8")

# The game starts here.
# - El juego comienza aquí.
label start:
    
    scene bg escena
    show detective at right
    e "Hay que resolver este caso"
    e "preguntemos a los acusados"

    scene bg interro
    show art at left
    a "buenas tardes detective"
    hide art 

    show detective at right
    e"Buenas tardes art " 
    e "por favor respondeme algunas preguntas sobre el caso"

    python:
       nueva_lista = []
    menu:
        "Soy inocente, Burt conocia a la victima al igual que carl":    
            python:
                   nueva_lista.append("claims(art,[[innocent,art],[knewVic,burt],[knewVic,carl]]).""\n")
        


    e "creo que eso es todo puedes retirarte" 
    e "que pase el siguiente por favor"   

    hide detective
    show burt at left
    b "Buenas tardes oficial"
    hide burt
    show detective at left
    e "Buenas tardes burt "
    e "Cuentame sobre lo que sabes "
    
    menu:
        "Bueno yo estuve fuera del pueblo. No conocia a la victima":    
            python:
                   nueva_lista.append("claims(burt,[[inOfTown,burt],[didNotKnowVic,burt]]).""\n")
        
    
    e "creo que eso es todo puedes retirarte"   
    e "que pase el siguiente por favor" 
 
    hide detective
    show carl at left
    c "Buenas tardes oficial"
    hide carl
    show detective at left
    e "Buenas tardes carl "
    e "Cuentame respecto al caso "
    
    menu:
        "soy inocente, yo estuve dentro del pueblo y a Burt fuera del pueblo ":    
            python:
                   nueva_lista.append("claims(carl,[[innocent,carl],[outOfTown,burt],[inTown,carl]]).""\n")
       


    python:
        archivo = open('/home/yaimcj/Documentos/Proyecto/murderer.pl','r')
        archivo2 =open('/home/yaimcj/Documentos/Proyecto/murderer2.pl','r')
        lista1 = list(archivo)
        lista2 = list(archivo2)
        lista3 = list(set(nueva_lista))
        nuevo_doc = open('/home/yaimcj/Escritorio/murder.pl','w')
        for x in lista1:
            nuevo_doc.write(x)
        for x in lista3:
            nuevo_doc.write(x)
        for x in lista2:
            nuevo_doc.write(x)
        nuevo_doc.close()
   
    return
