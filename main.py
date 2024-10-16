from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import replicate
from loguru import logger
from typing import Dict

app = FastAPI()

logger.add("app.log", rotation="500 MB")


class ImageInput(BaseModel):
    prompt: str
    prompt_upsampling: bool = True


@app.post("/generate")
async def generate_image(input_data: ImageInput) -> Dict[str, str]:
    input_prompt = {
        "prompt": input_data.prompt,
        "prompt_upsampling": input_data.prompt_upsampling
    }

    output = replicate.run(
        "black-forest-labs/flux-1.1-pro",
        input=input_prompt
    )
    if isinstance(output, replicate.helpers.FileOutput):
        url = str(output)
    else:
        url = output
    return {"message": "Image generated", "url": url}


@app.get("/")
async def root() -> Dict[str, str]:
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Flux image generation API"}

if __name__ == "__main__":
    logger.info("Starting the application")
    uvicorn.run(app, host="127.0.0.1", port=8000)
