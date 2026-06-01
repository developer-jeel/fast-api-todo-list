from fastapi import FastAPI
from database import engine
from models import Base
from crud import router as crud_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(crud_router,prefix='/todo',tags=["Crud Router"])

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1" ,port="8000")