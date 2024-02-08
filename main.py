from fastapi import FastAPI

app = FastAPI()

@app.get('/api/hello')
def helloWorld():
    return {'Message' : 'Hello World'}
