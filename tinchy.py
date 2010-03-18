from bottle import route, run, request, redirect
import random, shelve

def generate_tinchy_id():
    return ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890', 3))

@route('/')
def index():
    return """
    <h1>Get your tinchy URL!</h1>
    <form method="post">
      <input type="text" name="url" />
      <input type="submit" value="Make it tinchy!" />
    </form>
    """

@route('/', method='POST')
def make_tinchy_url():
    fatty_url = request.POST.get('url', '')
    if fatty_url[:7] == "http://":
        storage = shelve.open("tinchy")
        tinchy_id = generate_tinchy_id()
        while tinchy_id in storage:
            tinchy_id = generate_tinchy_id()
        storage[tinchy_id] = fatty_url
        storage.close()
        tinchy_url = request.url + tinchy_id
        return 'Your tinchy url is: <a href="{0}">{0}</a>'.format(tinchy_url)
    return 'Boo, <a href="%s">enter a proper url this time</a>.' % request.url

@route('/:tinchy_id')
def redirect_to_fatty_url(tinchy_id):
    storage = shelve.open("tinchy")
    if tinchy_id not in storage:
        return "Nope, this tinchy URL wasn't found."
    fatty_url = storage[tinchy_id]
    storage.close()
    redirect(fatty_url)
    
run(host='localhost', port=8080)