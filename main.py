import uasyncio
from microdot_asyncio import Microdot, Response
from microdot_utemplate import render_template
import mainTask

app = Microdot()
current_task = None
Response.default_content_type = 'text/html'

@app.before_request
async def pre_request_handler(request):
    if current_task:
        current_task.cancel()

@app.route('/')
async def root_html(request):
    return '<html><body><h1>Hola Root</h1></body></html>'

@app.route('/index')
async def index_html(request):
    return '<html><body><h1>Hola Mundo</h1></body></html>'

@app.route('/orders', methods=['GET'])
async def orders_html(request):
    name = "donsky"
    orders = ["soap", "shampoo", "powder"]
    return render_template('orders.html', name=name, orders=orders)

async def ExecMainTask():
    delay_ms=5000
    print("Inside Monitor method")
    i = 0
    while True:
        mainTask.execute()
        await uasyncio.sleep_ms(delay_ms)
        
def start_server():
    print('Starting microdot app')
    try:
        print("Step Exec Main Task")
        uasyncio.create_task(ExecMainTask())
        print("Step Run Server")
        app.run(debug=True,port=80)
    except:
        app.shutdown()

start_server()
