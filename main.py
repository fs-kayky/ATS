from fastapi import FastAPI

from routes.ATS.routes import router as router_ATS

app = FastAPI()

app.include_router(router_ATS)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5693)