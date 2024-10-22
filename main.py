from fastapi import FastAPI
from pydantic import BaseModel
from outlines import models, generate
from user import User

class Prompt(BaseModel):
    text: str

app = FastAPI()

llm_model = models.transformers("microsoft/Phi-3-mini-4k-instruct")
generator = generate.json(llm_model, User)

@app.post("/AskLLM")
async def ask_llm(prompt: Prompt):
    result = generator(prompt.text)
    return result
