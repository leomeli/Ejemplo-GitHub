import json

def cargar_datos(ruta):
	with open(ruta) as contenido:
	    a=json.load(contenido)
	    print(a.get('user_id'))
	    print(a.get('antiguedad'))

if __name__ == '__main__':	
	ruta='file_userss.json'
	cargar_datos(ruta)

