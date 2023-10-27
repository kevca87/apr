# Escribe aquí tu código
# Recuerda que todas las preguntas son independientes, no necesitas copiar y pegar código
# Puedes avanzar o retroceder entre las preguntas sin compromiso
import juegos_de_mesa
def encontrar_elemento_mas_repetido(lista_fav):
    contador = 0
    contador_mayor= 0
    for e in lista_fav:
        for x in lista_fav:
            if e == x:
                contador+= 1
        if contador > contador_mayor:
            elemento_buscado= e
            contador_mayor= contador
        contador= 0

    return elemento_buscado

        

def eliminar_elementos(lista_fav,eliminar):
    lista_nueva= []
    for i in lista_fav:
        if i != eliminar:
            lista_nueva.append(i)
    return lista_nueva


if __name__ == "__main__":
    x= input()
    amigos_pre= x.split(";")
    y= input()
    juegos_dis= y.split(";")
    lista_fav = []
    i= 0
    while i <= len(amigos_pre)-1:
        nombre= amigos_pre[i]
        juego_fav= juegos_de_mesa.encontrar_juego_favorito(nombre)
        lista_fav.append(juego_fav)
        i+=1
    print('Personas invitadas:',amigos_pre)
    print('Juegos disponibles:',juegos_dis)
    print('Juegos favoritos de los invitados:', lista_fav)
    print('Eligiendo juego de mesa para jugar:')
    sisi= True
    while sisi == True:
        juego= encontrar_elemento_mas_repetido(lista_fav)
        if juego not in juegos_dis:
            lista_fav = eliminar_elementos(lista_fav, juego)
            print('Ibamos a jugar', juego, 'pero no estaba disponible')
        else:
            juego_elegido= juego+'!'
            sisi = False
    print('Decidimos jugar',juego_elegido,'Que emocion!')


