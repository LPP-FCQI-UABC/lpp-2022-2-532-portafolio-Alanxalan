# Alan E. Perez Hernandez - Lenguaje de Programación Python(532)

#Creacion de listas con calles,numero y codigo postal
#Los codigos y calles repetidas se omitiran
calle = ["C.Pedregal",
         "P.º Ensenada",
         "P.º Playas de Tijuana",
         "P.º Playas de Tijuana",
         "Paseo Playas",
         "Prolongacion",
         "P.º Ensenada",
         "Av Del Pacifico",
         "Paseo Playas",
         "C.Pedregal",
         "Av del Agua",
         "C.Pedregal",
         "P.º Estrella del Mar",
         "Avenida Del Pacifico",
         "P.º Playas de Tijuana",
         "P.º Ensenada",
         "C. Oaxaca ",
         "C. Tláloc",
         "Cerro Azul",
         "Tecate - Rumorosa Libre",
         "Carretera Libre Mexicali -Tij "]
numExterior = [2234,
               1455,
               2234,
               2685,
               2685,
               3595,
               1356,
               1396,
               479,
               "S/N",
               "S/N",
               20,
               "S/N",
               "S/N",
               10,
               687,
               798,
               "S/N",
               126,
               400,
               "S/N",
               109,
               103,
               98,
               71]
codigoPostal = [22505,
                22500,
                22500,
                22506,
                22500,
                22506,
                22500,
                21440,
                21507,
                21420,
                21510]

#Tuplas de oxxos
Oxxo1 = (calle[0],numExterior[0],codigoPostal[0],32.5624351780737,-116.603732866706)
Oxxo2 = (calle[1],numExterior[1],codigoPostal[1],32.5661618045088,-116.585348818556)
Oxxo3 = (calle[2],numExterior[2],codigoPostal[1],32.5673645992957,-116.585348818556)
Oxxo4 = (calle[3],numExterior[3],codigoPostal[2],32.5716141561419,-116.611778712728)
Oxxo5 = (calle[4],numExterior[4],codigoPostal[2],32.5752088261282,-116.610178542352)
Oxxo6 = (calle[5],numExterior[5],codigoPostal[0],32.5740402175201,-116.624399600024)
Oxxo7 = (calle[6],numExterior[6],codigoPostal[3],32.5588660798213,-116.621384911664)
Oxxo8 = (calle[7],numExterior[7],codigoPostal[2],32.568946125631,116.625244342352)
Oxxo9 = (calle[6],numExterior[8],codigoPostal[4],32.564812910355,-116.626165400024)
Oxxo10 = (calle[8],numExterior[9],codigoPostal[0],32.5741765344836,-116.627363357696)
Oxxo11 = (calle[9],numExterior[10],codigoPostal[1],32.5706647358217,-116.60403948468)
Oxxo12 = (calle[10],numExterior[11],codigoPostal[5],32.5660668729055,-116.631501711664)
Oxxo13 = (calle[11],numExterior[12],codigoPostal[4],32.5704611555462,-116.628433264568)
Oxxo14 = (calle[12],numExterior[13],codigoPostal[6],32.5584801522821,-116.630751942352)
Oxxo15 = (calle[13],numExterior[14],codigoPostal[0],32.5669499525421,-116.585292342352)
Oxxo16 = (calle[14],numExterior[15],codigoPostal[0],32.5735962146707,-116.631327300024)
Oxxo17 = (calle[11],numExterior[16],codigoPostal[7],32.5658099741225,-116.647784227008)
Oxxo18 = (calle[15],numExterior[17],codigoPostal[0],32.5758255907345,-116.627228246056)
Oxxo19 = (calle[16],numExterior[18],codigoPostal[6],32.5616962936089,-116.634289057696)
Oxxo20 = (calle[17],numExterior[19],codigoPostal[2],32.5713606648984,-116.620024915368)
Oxxo21 = (calle[18],numExterior[20],codigoPostal[8],32.5011383612881,-116.570866015502)
Oxxo22 = (calle[19],numExterior[21],codigoPostal[9],32.5575919044134,-116.417352036363)
Oxxo23 = (calle[19],numExterior[22],codigoPostal[8],32.5507092255879,-116.344677865387)
Oxxo24 = (calle[19],numExterior[23],codigoPostal[10],32.5321233566162,-116.308749061758)
Oxxo25 = (calle[20],numExterior[24],codigoPostal[10],32.5369422846267,-116.06377994611)

#creacion de una lista de tuplas
OxxosList = [Oxxo1]
OxxosList.append(Oxxo2)
OxxosList.append(Oxxo3)
OxxosList.append(Oxxo4)
OxxosList.append(Oxxo5)
OxxosList.append(Oxxo6)
OxxosList.append(Oxxo7)
OxxosList.append(Oxxo8)
OxxosList.append(Oxxo9)
OxxosList.append(Oxxo10)
OxxosList.append(Oxxo11)
OxxosList.append(Oxxo12)
OxxosList.append(Oxxo13)
OxxosList.append(Oxxo14)
OxxosList.append(Oxxo15)
OxxosList.append(Oxxo16)
OxxosList.append(Oxxo17)
OxxosList.append(Oxxo18)
OxxosList.append(Oxxo19)
OxxosList.append(Oxxo20)
OxxosList.append(Oxxo21)
OxxosList.append(Oxxo22)
OxxosList.append(Oxxo23)
OxxosList.append(Oxxo24)
OxxosList.append(Oxxo25)

print(OxxosList) 