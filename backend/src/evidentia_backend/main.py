from fastapi import FastAPI


def create_app()->FastAPI:
    app = FastAPI(
         title="Evidentia API",
        version="0.1.0",
    )
    @app.get("/api/v1/health")
    def health_check() -> dict[str, str]:
        return {"status": "ok"}
    return app


app = create_app()
