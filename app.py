from bottle import run, route, debug, template, request, static_file

@route('/')
def main():
    return static_file('main.html', root='.')

@route('/help')
def help():
    return static_file('help.html', root='.')

@route('/script')
def script():
    return static_file('script.js', root='.')

@route('/d3')
def d3():
    return static_file('d3.js', root='.')

if __name__ == '__main__':
    run(reloader=True)

