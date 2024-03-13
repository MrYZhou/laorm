from fastapi import FastAPI
from util.system import Env
from util.response import AppResult

app = FastAPI()
Env.init(app)


@app.get("/")
def root():
    return AppResult.success("laorm-test")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8001, reload=False, workers=1)
