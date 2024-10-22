from fastapi import FastAPI
from pydantic import BaseModel
from outlines import models, generate
from ted_contract_award_notice import TedContractAwardNotice

class Prompt(BaseModel):
    text: str

app = FastAPI()

llm_model = models.transformers("microsoft/Phi-3-mini-4k-instruct")
generator = generate.json(llm_model, TedContractAwardNotice)

@app.post("/AskLLM")
async def ask_llm(prompt: Prompt):
    result = generator(prompt.text)
    return result
