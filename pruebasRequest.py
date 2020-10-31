# Importamos la librería
import requests

#Get, se realiza sobre una URL, esta es un endpoint
#r = requests.get('https://jsonplaceholder.typicode.com/posts')
#Puedo cambiar mi endpoint a 20, me devolvera la información del post con id 20
r = requests.get('https://jsonplaceholder.typicode.com/posts/20')
print(r)
#Verificamos el código del estado
print(r.status_code)
#Muestrame el response como texto
#print(r.text)
# Muestrame el response en formato json
#print(r.json)
#Generalmente las APIS develven las cosas en dos formatos
#json y xml

#Me va a devolver una colección de json, va a devolver un monton de post,
#verificamos en el página
my_query = r.json()
#print(my_query)

#En mi caso de prueba, lo que quiero es que mi título sea algo,
#despues lo vamos a adaptar a nuestra librería de testing unittest
print(my_query['title'])


#POST
#Ahora quiero postear algo
#tenemos que enviar:                    url                      data (formato json)    json kwargs
r = requests.post('https://jsonplaceholder.typicode.com/posts/', data={'title': 'Hola mundo', 'body': 'Ingresando data al body'})
# Ahora quiero saber que código de status responde o devuelve => 201 se ha llevado a cabo la creación del nuevo recurso
print(r.status_code)
#Me va a mostrar el response en texto, me trajo el title y body que postee, con un id 101 (le asigno este), es decir esta trayendo
#el último post que fue registrado, ya que existían 100 post
print(r.text)








