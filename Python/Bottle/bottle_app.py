from bottle import route, run, template, error, default_app, post, request

# index page
@route('/')
def index():
    return template( 'index' )

# 404 page
@error(404)
def error404(error):
    return template( '404' )
        
import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

application = default_app()