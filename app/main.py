from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:

    application = FastAPI(title="Carplit", version="1.0.0")  # Can be changed to use a settings file

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["localhost"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app = get_application()

@app.get("/")
async def read_root():
    return {"Welcome": "This is the main root."}
