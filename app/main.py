from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    except Exception as e:
        print(str(e))
