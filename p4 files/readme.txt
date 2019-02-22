Projeto de Aplicações Distribuidas do grupo 032

André Oliveira Peniche, Nº 44312

ficheiros incluidos:

-client.py
-server.py
-queries.py
-novadb.db
-queries.sql
-tables.sql
-certs
---------- \ \------
Comandos:
- ADD user <nome> <username> <password>
.fim client users OK

- ADD serie <nome da serie> <data de inicio> <synopse> <categoria>
.fim client serie OK

- ADD episodio <nome do episodio><descricao><id da serie>
.fim client episodes

- ADD serie_u <id_user><id da serie><classificacao>
.incomplete

- REMOVE user <name> //devia ser id
. Remove done right!
. u'OK'

- REMOVE serie <name>
. Remove done right!
. u'OK'

- REMOVE episodio <name>
. Remove done right!
. u'OK'

- SHOW user <user_id>
. show list is here [{u'username': u'peniche', u'password': u'133', u'id': 1, u'name': u'andre'}]

- SHOW serie <serie_id>
. show list is here [{u'synopse': u'ferrero', u'category_id': 12, u'start_date': 2018, u'name': u'ambrosio', u'id': 1}]

- SHOW episodio <episodio_id>
. show list is here [{u'serie_id': 1, u'description': u'grsegergqwefrwq3', u'name': u'dadaw', u'id': 1}]

- SHOW ALL user
.[{u'username': u'peniche', u'password': u'133', u'id': 1, u'name': u'andre'}]

- SHOW ALL serie
.[{u'synopse': u'ferrero', u'category_id': 12, u'start_date': 2018, u'name': u'ambrosio', u'id': 1},..]

-SHOW ALL serie_u
.[{u'classification_id': 44444, u'user_id': 1, u'serie_id': 1}, {u'classification_id': 3, u'user_id': 1, u'serie_id': 2}]

-SHOW ALL episodio
.[{u'serie_id': 1, u'description': u'grsegergqwefrwq3', u'name': u'dadaw', u'id': 1}]

-UPDATE serie_u <user_id><serie_id><classification>
. Updated, i guess!
. u'List series was updated!'

-UPDATE user <user_id><password>
. Updated, i guess!
. u'User was updated!'

-------------\\--------------

Foram feitas as seguintes alterações:

->usei  ligação requests.session() para fazer uma ligação persistente
->update user/serie_u funcional
->Implementação de metodo 'GET', projeto 3 so usava 'POST'
->Implementação de novo comando, SHOW serie_u <user id>, para mostrar as series do utilizador
->Implementação de novo comando, SHOW ALL serie_u, para mostrar as series da table list_series
->adicionei threaded=True, para aumentar a performance

--------------\\--------------

Limitações:

-> REMOVE é feito atraves do nome em vez do id
-> Não está implementado o comando ALL SERIE_C <id da categoria>
-> ADD serie_u esta parcialmente completo

---------------\\--------------

IpTables:

-> Regras do comando iptables que permitem concretizar a política:
	
	Ligações necessárias para o funcionamento das máquinas do lab:

	DCs: 10.121.53.14, 10.121.53.15, 10.101.53.16
	Storage: 10.121.72.23
	Iate/Falua: 10.101.85.6, 10.101.85.138
	Nemo: 10.101.85.18
	Gateway: 10.101.148.1
	Proxy: 10.101.85.136, 10.101.85.137

-> Regras:







- Nao filtrar trafego loopback:

	$ sudo iptables -A INPUT -i lo -j ACCEPT
	$ sudo iptables -A OUTPUT -o lo -j ACCEPT

