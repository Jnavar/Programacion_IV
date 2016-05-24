# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg interrogar="sala_interrogatorio.jpg"
image bg interrogar2 ="sala_interrogatorio3.jpg"
image bg afueras= "fuera_del_pueblo3.png"

image detective = "Grupo7/DetectivePensarr.png"
image detective2= "Grupo7/DetectivePensarr2.png"
image detective3 ="Grupo7/detectivee2.png"
image detective4= "Grupo7/DetectiveConfronn.png"
image testigo ="Grupo1/133.png"
image burt= "Grupo5/hablando3.2.png"
image burt2= "Grupo5/hablando3.1.png"
image art= "Grupo2/Hablandoo 2.png"
image art2= "Grupo2/Peensando.png"
image carl= "Grupo3/carl.png"
image carl2= "Grupo3/hablandoo2.png"


image bg Culpable="cadeia5.jpg"

# Declare characters used by this game.
define e = Character('TvNOticias', color="#c8ffc8")
define a = Character('Detective', color="#c8ffc8")
define b = Character('Testigo', color="#c8ffc8" )
define burt= Character('Burt', color="#c8ffc8")
define art= Character('Art', color="#c8ffc8")
define carl= Character('Carl', color="#c8ffc8")

# The game starts here.
label start:
        
    scene bg afueras
    e "Ultimas noticias se cometio un asesinato en las afueras de la ciudad"
    
    show detective at right
    a "Al parecer la victima fue abandonada aqui"
    hide detective
    show detective2 at left
    a "Preguntemosle al testigo"

    scene bg interrogar
    show detective3 at left
    a "Por favor que pase el testigo"
    hide detective3

    show testigo at right 
    b "Buenas tardes oficial"
    hide testigo
    
    show detective3 at left
    a "Buenas tardes señorita"
    a "Todo lo que sepa nos puede ser de gran ayuda"  
    hide detective3

    show testigo at right 
    b "no tengo mucha informacion, pero si logre ver a la victima acompañada de 3 hombres"  
    b "en un auto en las afueras de la ciudad"

    scene bg interrogar2
    show detective4 at right
    a "Buenas tardes señor Burt"
    hide detective4

    show burt at left
    burt "Buenas tardes oficial"
    hide burt
 
    show detective4 at right
    a "Como sabe fue acusado, ya que fue visto con la victima"
    a "Cuentenos sobre usted y la victima"
    hide detective4
    show burt at left
    burt "Yo me encontraba fuera del pueblo "
    burt "Yo no conoci a la victima" 
    hide burt
    show burt2 at left
    burt "."
    hide burt2
    show detective4 at right
    a "Bueno esto seria todo por ahora se puede retirar"  
    hide detective4

    show detective4 at right
    a "ahora que pase art"
    a "buenas tardes art " 
    hide detective4
    show art at right
    art "Buenas tardes oficial " 
    art "digame en que lo puedo ayudar"  
    hide art
    show detective4 at right
    a "usted fue visto junto a la victima"
    hide detective4
    show  art2 at right
    art "Se que burt era amigo de la victima"
    art "art y la victima eran enemigos"
    hide art2
    show art at right
    art "No tengo mas que decir"
    hide art
    show detective4 
    a "eso seria todo, gracias"
    a "que pase carl"
    hide detective4 
    show carl at left
    carl "Buenas tardes"
    hide carl
    show detective4 at right
    a "Fue visto con la victima que me puede decir sobre eso"
    hide detective4
    show carl2
    carl "Yo me econtraba dentro del pueblo "
    carl "tambien estuvo dentro del pueblo art y burt"
    carl "Yo y Burt eramos amigos de la victima" 
    

    
    scene bg Culpable
    show detective at right
    show art2 at left
    python:
          from pyswip import Prolog
          prolog=Prolog()
          prolog.consult("/home/maze/Escritorio/Adriandetective.pl")
          asesino=list(prolog.query("murderer(X)"))
          a ("Segun las prubas y declaraciones obtenidas el culpable es %s"%asesino[0]["X"])
          a ("Segun las prubas y declaraciones obtenidas el culpable es %s"%asesino[1]["X"])
          
    
     

    return
