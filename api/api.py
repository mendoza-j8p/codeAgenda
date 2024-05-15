from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from models import *

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Monta un nuevo "sistema de archivos" en la ruta /static
# y sirve los archivos estáticos desde el directorio ./static
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})





"""

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

"""