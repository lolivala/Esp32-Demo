import uasyncio
from microdot_asyncio import Microdot, Response

#from microdot import Response
from microdot_utemplate import render_template

# setup webserver
app = Microdot()
current_task = None
Response.default_content_type = 'text/html'

@app.route('/')
async def hello(request):
	return 'Hello world'

@app.before_request
async def pre_request_handler(request):
    if current_task:
        current_task.cancel()

@app.route('/MonitorSettings')
async def Monitor(request):
    return '<html><body><h1>Hola Mundo</h1></body></html>'

@app.route('/niagara')
async def niagara(request):
    args_dict = {}
    for key in request.args.keys():
        args_dict[key] = int(request.args[key])
    
    global current_task
    current_task = uasyncio.create_task(setNiagara())

    await uasyncio.sleep_ms(delay_ms)
    return 'OK'

@app.route('/orders', methods=['GET'])
async def index(req):
    name = "donsky"
    orders = ["soap", "shampoo", "powder"]

    return render_template('orders.html', name=name, orders=orders)

async def MonitorEnvironment():
    delay_ms=5000
    print("Inside Monitor method")
    i = 0
    while True:
        print("tick: {}", str(i))
        i = i+1
        await uasyncio.sleep_ms(delay_ms)
        
def start_server():
    print('Starting microdot app')
    try:
        print("Step 1")
        uasyncio.create_task(MonitorEnvironment())
        print("Step 2")
        app.run(debug=True,port=80)
    except:
        app.shutdown()

start_server()