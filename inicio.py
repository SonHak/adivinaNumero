
from bottle import route,run, request, jinja2_template as template
import random
from beaker.middleware import SessionMiddleware

#codigo hardcoded
@route('/')
def iniciar():
	mivariable = 33
	return template('base',mivariable=mivariable)
	
	
@route('/numero',method='GET')	
def comprobarNumero():
	numero = int(request.GET.get('num'))
	if  numero != 33:		
		return template('distinto',mivariable=numero)
	else:
		return template('igual',mivariable=numero)
run(host='localhost', port=8080) 
