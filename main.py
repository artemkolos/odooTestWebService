import xmlrpc.client
HOST = 'localhost'
PORT = 8569
DB = 'o15-learn'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
models = xmlrpc.client.ServerProxy(ROOT + 'object')
sessions = models.execute_kw(DB, uid, PASS, 'open_academy.sessions', 'search_read', [],{'limit': 5})

for session in sessions:
    print("Session %s (%s seats)" % (session['name'], session['seatsNumber']))

session_id = models.execute_kw(DB, uid, PASS, 'open_academy.sessions', 'create', [{
    'name' : 'Session 4',
    'course' : 2,
    'seatsNumber' : 10,
    'create_uid': uid,
}])

