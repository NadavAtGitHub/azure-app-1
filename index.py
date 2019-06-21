from bottle import run, template, request, static_file, Bottle

app: Bottle = Bottle()


@app.get('/')
@app.get('/hello/<name>')
def hello(name='world'):
    return template("Hello, {{name}}!", name=name)


@app.post('/hello')
def do_hello():
    default = "default"
    name = request.forms.get("name", default=default)

    return template("Hello, {{name}}", name=name)


@app.get('/files/<filename:path>')
def get_file(filename):
    return static_file(filename, root='E:\\Pycharm Comunity Edition\\test\\html')


run(app, host='localhost', port=8080, debug=True)
