
from bottle import route,run, request, jinja2_template as template
import random
from beaker.middleware import SessionMiddleware


@route('/')
def iniciar(environ, start_response):
	 # Get the session object from the environ
    session = environ['beaker.session']

    # Check to see if a value is in the session
    mivariable = random.randint(1,5) in session

    # Set some other session variable
    session['mivariable'] = random.randint(1,5)

    start_response('200 OK', [('Content-type', 'text/plain')])
	
	return template('base',mivariable=session['mivariable'])
	
	
@route('/numero',method='GET')	
def comprobarNumero():
	numero = int(request.GET.get('num'))
	if  numero != 33:		
		return template('distinto',mivariable=numero)
	else:
		return template('igual',mivariable=numero)
run(host='localhost', port=8080) 
