import json
import constantes as CONST

class ValidadorJSON:
	def carga_JSON(self,entrada):
		data_JSON = {}
		try:
			with open(entrada+'.json') as json_file:
				data_JSON = json.load(json_file)
				respuesta = self.valida_JSON(data_JSON)
				return respuesta
		except:
			return "ERROR AL ABRIR ARCHIVO JSON"
			
	def exporta_JSON(self,entrada,data_out):
		with open(entrada+'_out.json', 'w') as file:
			json.dump(data_out, file, indent=4)

	def valida_JSON(self,data_JSON):
		CAMPOS_REQUERIDOS = ["nombre","nivel","goles","sueldo","bono","sueldo_completo","equipo"]
		data = []
		for it in data_JSON:
			if self.valida_tipos(it) and self.contine_propiedades(it):
				data.append(it)
			else:
				return "ERROR AL VALIDAR JSON"

		return data

	def valida_tipos(self,data_JSON):
		respuesta = True
		respuesta = respuesta and self.es_numero(data_JSON["goles"])
		respuesta = respuesta and self.es_numero(data_JSON["sueldo"])
		respuesta = respuesta and self.es_numero(data_JSON["bono"])
		respuesta = respuesta and self.existe_nivel(data_JSON["nivel"])
		return respuesta

	def es_numero(self,cadena):
		if type(cadena) == int or type(cadena) == float:
			return True
		else:
			return False
	
	def existe_nivel(self,nivel):
		if nivel not in CONST.CATALOGO_NIVEL:
			return False
		return True

	def contine_propiedades(self,data_JSON):
		CAMPOS_REQUERIDOS = ["nombre","nivel","goles","sueldo","bono","sueldo_completo","equipo"]
		for propiedad in CAMPOS_REQUERIDOS:
			if propiedad not in data_JSON:
				return False
		return True