from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/bye")
def read_root():
    return {"message": "Good bye I am Deepa}
