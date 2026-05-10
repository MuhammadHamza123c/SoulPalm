from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from api.solo_router import router_sol
from api.friend_router import router_fri
from api.relation_router import router_real
from fastapi.staticfiles import StaticFiles
import os

app=FastAPI()

# Create public dir if it doesn't exist (safety for deployment)
if not os.path.exists("public"):
    os.makedirs("public")

app.mount("/public", StaticFiles(directory="public"), name="public")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def serve_home():
    return FileResponse('index.html')

@app.get('/SoulPalm')
def home():
    return{
        'SoulPalm':'Welcome to SoulPalm'
    }

app.include_router(router_sol)
app.include_router(router_fri)
app.include_router(router_real)