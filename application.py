#coding: utf-8
# Se importa una libreria para expresiones regulares que permite procesar texto en python
import re
# Se importa libreria urllib para buscar datos a través de internet
import urllib, os
print ""

class internet(object):
	def pagina(self):
		a = True
		while a==True:
			self.pag1= raw_input("Página 1: ")
			self.pag2 = raw_input("Página 2:")
			self.palabra = raw_input("Ingrese la Palabra que Busca: ")
			url = "https://"
			# Con el urlopen podemos abrir recursos de URL
			req = urllib.urlopen(url + self.pag1)
			r = urllib.urlopen(url + self.pag2)
			# Asigna un espacio temporal para leer el archivo o Pagina WEB
			a1 = req.read()
			a2 = r.read()
			# Con el re.findall retornaran las palabras que nosotros busquemos
			palencontrada1 = len(re.findall(self.palabra,a1))
			palecontrada2 = len(re.findall(self.palabra,a2))
			if palencontrada1 > palecontrada2:
				print "Le Recomendamos la Página: ",self.pag1
				print "Cantidad de Palabras que se han Encontrado ", palencontrada1
				break
			elif palencontrada1 == 0:
				print "Lo Sentimos, no se Encuentra"
			elif palecontrada2 ==0:
				print "Lo Sentimos, no se Encuentra"
			else:
				print "Le Recomendamos la Página: ",self.pag2
				print "Cantidad de Palabras que se han Encontrado ", palecontrada2
				
				preg = raw_input("¿Desea salir? Si/No ")
				if preg.lower() == "si":
					a = False
				elif preg.lower() == "no":
					a = True
				else:
					print "Ingrese Si/No..."

c= internet()
c.pagina()