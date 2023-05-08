#Angeles Belen Garcia - 1B - primer parcial - Programacion I
from os import system
import re
#Id,  Nombre,    Raza,   Poder de pelea, Poder de ataque,  Habilidades
#"1", "Goku", "Saiyan" ,  "500000",        "10000",       "Kamehameha|$%Genki Dama|$%Super Saiyan"

def traer_datos_desde_archivo(path:str)->list:
    '''
    Brief: Trae lo que se encuentra en archivo .csv y lo convierte en una lista de diccionarios
    Parameters: 
        path: nombre del archivo de donde extraeremos los datos
    Return: Retorna una lista de personajes
    '''
    DBZ = []
    archivo_dbz = open(path, "r", encoding = "utf-8")

    for line in archivo_dbz:

        lectura = re.split(r",|\n", line)
        personaje = {}
        personaje['id'] = lectura[0]
        personaje['nombre'] = lectura[1]

        raza = []
        if lectura[2] != "Three-Eyed People" and lectura[2] !=  "Shin-jin":
            buscar_guion = re.findall("-", lectura[2])
            if buscar_guion != []:
                raza = re.split("-", lectura[2])
                personaje['raza'] = raza
            else:
                personaje['raza'] = lectura[2]
        else:
            personaje['raza'] = lectura[2]

        personaje['poder de pelea'] = lectura[3]
        personaje['poder de ataque'] = lectura[4]
        habilidades = re.split(r"\|", lectura[5])
        personaje['habilidad'] = habilidades
        DBZ.append(personaje)

    archivo_dbz.close()
    return DBZ

def control_de_archivo(path:str)->list:
    '''
    Brief: controla que el tipo de dato sea el correcto para poder llamar a la funcion que extre los datos de archivo.
    Parameters: 
        path: nombre del archivo de donde extraeremos los datos
    Return: Retorna una lista de personajes
    '''
    tipo_de_dato = type(path)

    if tipo_de_dato == str:
        buscar_extencion = re.findall(".csv", path)
        if buscar_extencion != []:
            lista_DBZ = traer_datos_desde_archivo(path)
            obtencion_de_datos = lista_DBZ
        else:
            obtencion_de_datos = []
    else:
        obtencion_de_datos = []
    return obtencion_de_datos

def setear_una_lista(lista:list)->set:
    '''
    Brief: Setea una lista
    Parameters: 
        lista: lista que busca convertise en un set.
    Return: Retorna una lista seteada
    '''
    set_lista = set(lista)
    return set_lista

def listar_habilidad_raza(path:str,clave:str)->list:
    '''
    Brief: crea una lista, de lo que se le envie en el parametro 'clave'
    Parameters: 
        path: nombre del archivo desde donde se van a extraer los datos.
        Clave: key de aquello sobre lo que se quiere listar
    Return: Retorna una lista de acuerdo con lo colocado en el parametro 'clave'
    '''

    lista_personajes = control_de_archivo(path)
    lista_raza_habilidad = []

    for personaje in lista_personajes:
        raza_habilidad = personaje[clave]
        if type(raza_habilidad) == list:
            for clave_raza_habilidad in raza_habilidad:
                clave_raza_habilidad = clave_raza_habilidad.strip()
                lista_raza_habilidad.append(clave_raza_habilidad)
        else:
            raza_habilidad = raza_habilidad.strip()
            lista_raza_habilidad.append(raza_habilidad)
    
    return lista_raza_habilidad

def calcular_cantidades_raza(path:str)->list:
    '''
    Brief: crea una lista, de lo que se le envie en el parametro 'clave'
    Parameters: 
        path: nombre del archivo desde donde se van a extraer los datos.
        Clave: key de aquello sobre lo que se quiere listar
    Return: Retorna una lista de acuerdo con lo colocado en el parametro 'clave'
    '''

    lista_raza = listar_habilidad_raza(path, 'raza')
    set_raza = setear_una_lista(lista_raza)
    lista_cantidades_por_raza = []

    for raza_set in set_raza:
        contador_raza = 0

        for raza_lista in lista_raza:
            if raza_set == raza_lista:
                contador_raza += 1
        
        dic_raza = {}
        dic_raza['nombre'] = raza_set
        dic_raza['cantidad'] = contador_raza
        lista_cantidades_por_raza.append(dic_raza)
    
    return lista_cantidades_por_raza

def listar_cantidad_por_raza(path:str):
    lista_cantidades_raza = calcular_cantidades_raza(path)
    for raza in lista_cantidades_raza:
        nombre_raza = raza['nombre']
        cantidad_raza = raza['cantidad']
        print(f"Raza: {nombre_raza} Cantidad: {cantidad_raza}")

def listar_personajes_por_raza(path:str):

    lista_todas_razas = listar_habilidad_raza(path, 'raza')
    set_raza = setear_una_lista(lista_todas_razas)
    lista_personajes = control_de_archivo(path)

    for raza in set_raza:
        nombre_raza = raza.upper()
        print("*********************************************")
        print(f"{nombre_raza}")
        for personaje in lista_personajes:

            raza_personaje = personaje['raza']
            nombre_personaje = personaje['nombre']
            poder_ataque = personaje['poder de ataque']

            if type(raza_personaje) == list:
                for razas in raza_personaje:
                    if razas == raza:
                        print(f"{nombre_personaje} - {poder_ataque}")
            
            elif raza == raza_personaje:
                print(f"{nombre_personaje} - {poder_ataque}")

def solicitar_eleccion(path:str)->str:
    lista_habilidades = listar_habilidad_raza(path, 'habilidad')
    set_habilidades = setear_una_lista(lista_habilidades)
    for habilidad in set_habilidades:
        print(habilidad)
    opcion = input("Elija una opcion valida ")
    return opcion

def validar_eleccion(path:str, opcion:str)->bool:
    lista_habilidades = listar_habilidad_raza(path, 'habilidad')
    set_habilidades = setear_una_lista(lista_habilidades)
    opcion_valida = False
    for opcion_posible in set_habilidades:
        if opcion == opcion_posible:
            opcion_valida = True
    return opcion_valida


def dividir(dividendo:float, divisor:int) -> float:
    '''
    Brief: Realiza una divicion entre dos numeros. 
    Parameters: 
        dividendo: Numero que se desea dividir.
        divisor: Numero que dividira al parametro dividendo. 
    return: retorna el resultado de la divicion.
    '''
    if divisor != 0:
        divicion = dividendo / divisor 
    else:
        divicion = 0
    return divicion 


# def sacar_promedio():

def listar_habilidades_personaje(path:str):
    lista_todas_habilidades = listar_habilidad_raza(path, 'habilidad')
    set_habilidad = setear_una_lista(lista_todas_habilidades)
    lista_personajes = control_de_archivo(path)

    for habilidad in set_habilidad:
        nombre_habilidad = habilidad.upper()
        print("*********************************************")
        print(f"{nombre_habilidad}")
        for personaje in lista_personajes:
            habilidad_personaje = personaje['habilidad']
            




def listar_personajes_por_habilidad(path:str):
    print("Habilidades:")
    print("****************************************")
    validacion = False
    while validacion != True:
        opcion = solicitar_eleccion(path)
        validacion = validar_eleccion(path, opcion)
    


lista_opciones = [ "1. Traer datos desde archivo",
                "2. Listar cantidad por raza",
                "3. Listar personajes por raza",
                "4. Listar personajes por habilidad",
                "5. Jugar batalla",
                "6. Guardar Json",
                "7. Leer Json",
                "8. Salir del programa.",
]

def imprimir_menu():
    '''
    Brief: imprime el menu de opciones.  
    Parameters: no recibe parametros 
    return: no retorna, muestra el menu de opciones. 
    '''
    for opcion in lista_opciones:
        print(f"{opcion}")

def stark_menu_principal():
    '''
    Brief: le pide al usuario que seleccione una opcion del menu.   
    Parameters: no recibe parametros 
    return: retorna la opcion ingresada por el usuario. 
    '''
    imprimir_menu()
    opcion = input("Ingrese una opcion: ")
    return opcion

def DBZ_app(archivo:str):
    '''
    Brief: Llama a las funciones correspondientes de acuerdo con lo que el usuario solicita.  
    Parameters: 
            archivo: string que indica de donde se obtendran los datos. 
    return: no retorna, muestra aquello que pide el usuario. 
    '''
    datos = control_de_archivo(archivo)
    if datos != []:
        print("Datos traidos de archivo correctamente")
        seguir = True
        while seguir:
            opcion = stark_menu_principal()
            match opcion:
                    case "1":
                        datos = control_de_archivo(archivo)
                        if datos != []:
                            print("Datos traidos de archivo correctamente")
                    case "2":
                        listar_cantidad_por_raza(archivo)
                    case "3":
                        listar_personajes_por_raza(archivo)
                    case "4":
                        listar_personajes_por_habilidad(archivo)
                    case "5":
                        pass
                    case "6":
                        pass
                    case "7":
                        pass
                    case "8":
                        seguir = False
                    case _:
                        print("Opcion no valida")
        print("¡Gracias ppor utilizar Stark_marvel_app_3!")
    else:
        print("No se pudieron obtener los datos")

system("cls")
DBZ_app("DBZ.csv")

