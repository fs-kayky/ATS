from fastapi import FastAPI
from routes.ATS.routes import router as router_ats

app = FastAPI()

app.include_router(router_ats)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5693)
