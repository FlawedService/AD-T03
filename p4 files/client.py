#!/usr/bin/env python
# coding=utf-8

import json
import sys
import requests
import pprint
from requests_oauthlib import OAuth2Session
from requests.packages.urllib3.exceptions import SubjectAltNameWarning
requests.packages.urllib3.disable_warnings(SubjectAltNameWarning)
#removes warning Unverified HTTPS request is being made
requests.packages.urllib3.disable_warnings()

cmdlist = ["ADD", "REMOVE", "SHOW", "UPDATE"]
cmd2list = ["user", "serie", "episodio", "serie_u"]
utillist = ["NAME", "USERNAME", "PASSWORD", "ID"]
serielist = ["NAME", "START_DATE", "SYNOPSE", "CATEGORY_ID"]
episodelist = ["NAME", "DESCRIPTION", "SERIE_ID"]
serie_ulist = ["user_id", "classificacao", "serie_id"]
tablelist = {"USER": "utilizadores", "CLASSIFICACAO": "classificacao", "CATEGORIA": "categoria",
             "SERIE_U": "serie_u", "SERIE": "series", "EPISODIO": "episodios"}
classification_values = {"M": 1, "MM":2, "S":3, "B":4, "MB":5}

client_id = "hidden"
client_secret = "hidden"
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'


try:
	github = OAuth2Session(client_id)
	authorization_url, state = github.authorization_url(authorization_base_url)
	print 'Aceder ao link (via browser) para obter a autorizacao,', authorization_url

	redirect_response = raw_input(' insira o URL devolvido no browser e cole aqui:')

	github.fetch_token(token_url, client_secret=client_secret,authorization_response=redirect_response)
	r = github.get('https://api.github.com/user')
	print "oauth2 says OK"
	#print r.content #print so para verificar que esta correto

except Exception, e:
	print "oauth2 says NOK", e
	sys.exit()

#not being used
def checkmsg(data):
    if data["category"] == "user".upper():
        data["category"] = "user"
        if cmd in utillist and cmd[4].isdigit():
            return True
        else:
            return False

    elif data["category"] == "serie".upper():
        data["category"] = "serie"
        return True

    elif data["category"] == "episodio".upper():
        data["category"] = "episodio"
        return True

    else:
        print "unknown command"
        return False
    return data

while True:
    rs = requests.session()
	cmd = raw_input("Comando:")
	cmd2 = cmd.split()
	if len(cmd.split(" ")) > 6:
	print "too much parameters"
	try:
		if cmd2[0] == "ADD":
		    if cmd2[1] == "user":
			data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2], "username": cmd2[3], "password": cmd2[4]}
			r = rs.post('https://localhost:5000/' + tablelist[data["category"].upper()], json=json.dumps(data),
				verify='root.pem',
				cert=('client.crt', 'client.key'))
			msg = json.loads(r.text)
			print "fim client users", msg

		    elif cmd2[1] == "serie":
			#in case we want to add a series to an user
			data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2], "start_date": cmd2[3], "synopse": cmd2[4], "category_id": cmd2[5]}
			if int(data["category_id"]) < 15:
			    r = rs.post('https://localhost:5000/' + tablelist[data["category"].upper()], json=json.dumps(data),
					      verify='root.pem',
					      cert=('client.crt', 'client.key'))
			    msg = json.loads(r.text)
			    print "fim client serie", msg
			else:
			    print "Categoria errada"
		    elif cmd2[1] == "serie_u":#falta definir a sql e parte no servidor
			data = {"Comando": cmd2[0], "category": cmd2[1], "user_id": cmd2[2], "classificacao": cmd2[3], "serie_id": cmd2[4]}
			print data
			if int(data["classificacao"]) < 6:
				r = rs.post('https://localhost:5000/' + tablelist[data["category"].upper()], json=json.dumps(data),
					      verify='root.pem',
					      cert=('client.crt', 'client.key'))
				msg = json.loads(r.text)
				print "fim add series user", msg
			else:
				print "Wrong classification. It must be between 1 and 5." 
		    elif cmd2[1] == "episodio":
			data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2], "description": cmd2[3], "serie_id": cmd2[4]}
			r = rs.post('https://localhost:5000/' + tablelist[data["category"].upper()], json=json.dumps(data),
				          verify='root.pem', cert=('client.crt', 'client.key'))
			msg = json.loads(r.text)
			print "fim client episodes"
		    else:
			print "no etiendo!!!"
		elif cmd2[0] == "SHOW":
		    if cmd2[1] == "ALL":
			if cmd2[2] in cmd2list:
			    r = rs.get('https://localhost:5000/' + tablelist[cmd2[2].upper()],
				              verify= 'root.pem',
				              cert=('client.crt', 'client.key'))
			    msg = json.loads(r.text)
			    print msg
		    elif cmd2[1].lower() == "serie_u":
			data = {"Comando": cmd2[0], "category": cmd2[1], "user_id": cmd2[2]}	
			r = rs.post('https://localhost:5000/' + "serie_u", json = json.dumps(data),
				          verify='root.pem', cert=('client.crt', 'client.key'))
			msg = json.loads(r.text)
			print "show user serie list here", msg

		    elif cmd2[1] in cmd2list:
			data = {"Comando": cmd2[0], "category": cmd2[1], "id": cmd2[2]}
			r = rs.post('https://localhost:5000/' + tablelist[data["category"].upper()], json = json.dumps(data),
				          verify='root.pem', cert=('client.crt', 'client.key'))
			msg = json.loads(r.text)
			print "show list is here", msg

		elif cmd2[0] == "REMOVE":
			data = {"Comando": cmd2[0], "category": cmd2[1], "name": cmd2[2]}
			if cmd2[1] in cmd2list:
				r = rs.post('https://localhost:5000/' + tablelist[data["category"].upper()], json = json.dumps(data),
						  verify='root.pem', cert=('client.crt', 'client.key'))
				msg = json.loads(r.text)
				print "Remove done right!"
				pprint.pprint(msg)
			else:
				print "upsie! can't do that"

		elif cmd2[0] == "UPDATE":
			if cmd2[1] == "user":
				data = {"Comando": cmd2[0], "category": cmd2[1], "user_id": cmd2[2], "password": cmd2[3]}
			elif cmd2[1] == "serie_u":
		    	data = {"Comando": cmd2[0], "category": cmd2[1], "user_id": cmd2[2], "serie_id": cmd2[3], "classification_id": cmd2[4]}
			print "update data", data
			r = rs.post('https://localhost:5000/' + tablelist[cmd2[1].upper()], json = json.dumps(data),
				      verify='root.pem', cert=('client.crt', 'client.key'))
			msg = json.loads(r.text)
			print "Updated, i guess!"
			pprint.pprint(msg)
	except Exception, e:
		print "There was an error executing this command, " + cmd
		print "The error was the following: ", e
