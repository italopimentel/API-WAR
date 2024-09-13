import uvicorn
import api

app = api.app

uvicorn.run(app=app, port=8000)