from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.prediction import prediction_route
from routes.history import history_route

app = FastAPI()
app.include_router(prediction_route, prefix='/prediction')
app.include_router(history_route, prefix='/history')


origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)



if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=8080, reload=True, log_level="warning")