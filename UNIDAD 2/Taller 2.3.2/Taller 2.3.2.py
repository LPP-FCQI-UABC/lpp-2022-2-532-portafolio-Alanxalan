# Alan E. Perez Hernandez - Lenguaje de Programación Python(532)
#Taller 2.3.2
morse = {"a":"*-","b":"-***","c":"-*-*","d":"-**","e":"*","f":"**-*","g":"--*","h":"****","i":"**","j":"*---","k":"-*-","l":"*-**","m":"--","n":"-*",
         "o":"---","p":"*--*","q":"--*-","r":"*-*","s":"***","t":"-","u":"**-","v":"***-","w":"*--","x":"-**-","y":"-*--","z":"--**",
          "1":"*----","2":"**---","3":"***--","4":"****-","5":"*****","6":"-****","7":"--***","8":"---**","9":"----*","0":"-----"," ":"/","/":" "}
caracteres = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","/")
cad  = input("Ingresa tu cadena: ")
res = ""
aux =""
cont = 0
if(cad[0]=="*" or cad[0]=="-"):
  for c in cad:
    if(c!="/"):
      aux = aux + c
    else:
      if(c == "/"):
        cont = cont +1
      for k in caracteres:
        if(cont ==2):
          res= res + " "
          cont = 0
        if(morse.get(k)== aux):
          cont = 0
          res= res + k
          aux =""
else:
  for c in cad:
    if(c != " "):
      res = res + morse.get(c) + "/"
    else:
      res = res + morse.get(c)            
print(res)