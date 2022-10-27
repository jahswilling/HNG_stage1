from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { "slackUsername": "Javi", "backend": True, "age": 26, "bio": "I good die" }