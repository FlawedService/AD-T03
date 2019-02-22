#!/usr/bin/env python
# coding=utf-8

import sqlite3
import json
import queries
import ssl
from flask import Flask, request
from flask import jsonify
from flask import render_template_string
from requests_oauthlib import OAuth2Session
import os.path as pa

ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.load_cert_chain('server.crt', 'server.key')
ctx.load_verify_locations(cafile='root.pem')


DATABASE = "novadb"
#DATABASE = "testDb"
app = Flask(__name__)

def dict_factory(cursor, row):

    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db(dbname):
    # Existe ficheiro da base de dados?
    db_is_created = pa.isfile(dbname)
    connection = sqlite3.connect(dbname, check_same_thread=False)
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    if not db_is_created:
        cursor.executescript(open("tables.sql").read())
        connection.commit()

    return connection, cursor

@app.route('/utilizadores', methods=["POST", "GET"])
def users():
	if request.method == 'POST':
		data = json.loads(request.json)
		query = str(data["Comando"] + " " + data["category"])
		
		if data["Comando"] == "ADD":
		    args = [str(data["name"][0:]), str(data["username"][0:]), str(data["password"][0:])]

		    db.execute(queries.add['ADD USERS'], args)
		    print db.fetchone()

		    conndb.commit()
		    return json.dumps("OK")

		elif data["Comando"] == "REMOVE":
		    args = [str(data["name"][0:])]
		    db.execute(queries.remove['REMOVE USERS'], args)
		    print db.fetchone()
		    conndb.commit()
		    return json.dumps("OK")

		elif data["Comando"] == "SHOW":
		    if "user" == data["category"]:
			c = db.execute(queries.show["SHOW USERS"], (data["id"],))
			requery = c.fetchall()
			conndb.commit()
			print requery
			return json.dumps(requery)

		elif data["Comando"] == "UPDATE":
		    db.execute(queries.update['UPDATE USER'], (data["user_id"], data["password"],))
		    conndb.commit()
		    return json.dumps("User was updated!")

	elif request.method == "GET":
		c = db.execute(queries.show_all['SHOW ALL USERS'])
		requery = c.fetchall()
		conndb.commit()
		print requery
		return json.dumps(requery)
	
@app.route('/serie_u', methods=["POST", "GET"])
def user_series():
	if request.method == 'POST':
		data = json.loads(request.json)
		if data["Comando"] == "SHOW":
			c = db.execute(queries.show["SHOW SERIES USER"], (data["user_id"],))
			requery = c.fetchall()
			conndb.commit()
			print requery
			return json.dumps(requery)
		elif data["Comando"] == "UPDATE":
			db.execute(queries.update['UPDATE SERIE_U'], (data["classification_id"], data["serie_id"], data["user_id"],))
			conndb.commit()
			return json.dumps("List series was updated!")
		elif data["Comando"] == "REMOVE":
			db.execute(queries.update['REMOVE SERIE_U'], (data["classification_id"], data["serie_id"], data["user_id"],))
			conndb.commit()
			return json.dumps("List series was updated!")
		else:
			return json.dumps("Invalid command")
	elif request.method == "GET":
		c = db.execute(queries.show_all['SHOW ALL SERIE_U'])
		requery = c.fetchall()
		conndb.commit()
		print requery
		return json.dumps(requery)

@app.route('/series', methods = ["POST", "GET"])
def series():
	if request.method == 'POST':
		data = json.loads(request.json)
		if data["Comando"] == "ADD":
		    print data.keys()
		    if "subCategory" in data.keys():
			args = [int(data["user_id"]), int(data["classification_id"]), int(data["serie_id"])]
			db.execute(queries.add['ADD serie_u'], args)
			print db.fetchone()
			conndb.commit()
			return json.dumps("OK")
		    else:
			args = [str(data["name"][0:]), int(data["start_date"][0:]), str(data["synopse"][0:]), int(data["category_id"[0:]])]
			db.execute(queries.add['ADD SERIES'], args)
			print db.fetchone()
			conndb.commit()
			return json.dumps("OK")

		elif data["Comando"] == "REMOVE":
		    args = [str(data["name"][0:])]
		    db.execute(queries.remove['REMOVE SERIE'], args)
		    print db.fetchone()
		    conndb.commit()
		    return json.dumps("OK")

		elif data["Comando"] == "SHOW":
			print data
			c = db.execute(queries.show['SHOW SERIES'], (data["id"],))
			requery = c.fetchall()
			conndb.commit()
			print requery
			return json.dumps(requery)

		else:
		    return jsonify("Invalid Command")
	
	elif request.method =="GET":
		c = db.execute(queries.show_all['SHOW ALL SERIES'])
		requery = c.fetchall()
		conndb.commit()
		print requery
		return json.dumps(requery)

@app.route('/episodios', methods=["GET", "POST"])
def episodes():
	if request.method == 'POST':
		data = json.loads(request.json)

		if data["Comando"] == "ADD":
		    args = [str(data["name"][0:]), str(data["description"][0:]), int(data["serie_id"][0:])]
		    db.execute(queries.add['ADD EPISODE'], args)
		    print db.fetchone()
		    conndb.commit()
		    return json.dumps("OK")

		elif data["Comando"] == "REMOVE":
		    args = [str(data["name"][0:])]
		    db.execute(queries.remove['REMOVE EPISODE'], args)
		    print db.fetchone()
		    conndb.commit()
		    return json.dumps("OK")

		elif data["Comando"] == "SHOW":
			c = db.execute(queries.show['SHOW EPISODIOS'], (data["id"],))
			requery = c.fetchall()
			conndb.commit()
			print requery
			return json.dumps(requery)
		else:
		    return jsonify("Invalid command!")
	elif request.method == 'GET':
		c = db.execute(queries.show_all['SHOW ALL EPISODES'])
		requery = c.fetchall()
		conndb.commit()
		print requery
		return json.dumps(requery)


if __name__ == '__main__':

    conndb, db = connect_db(DATABASE)
    app.run(threaded=True, ssl_context=ctx, use_reloader=False, debug=True)
    #app.run(threaded=True, ssl_context = ctx, debug = True)