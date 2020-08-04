import requests, json

# Buscar empresa
pagina = 1
nom = 'idealista'
tipus = 'empresa'

url = 'https://libreborme.net/borme/api/v1/{}/search/?q={}&page={}'.format(tipus,nom,pagina)
resultat_cerca = json.loads(requests.get(url).text)
print (json.dumps(resultat_cerca, indent=4, sort_keys=True))

# Obtenir detalls
uri = '/borme/api/v1/empresa/idealista-international/'
url = 'https://libreborme.net{}'.format(uri)
resultat_detalls = json.loads(requests.get(url).text)
print (json.dumps(resultat_detalls, indent=4, sort_keys=True))
