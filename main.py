## Para Deixar o server em reload uvicorn main:app --reload

import uvicorn 
from pydantic import BaseModel
from fastapi import FastAPI

# Criando a instancia da Aplicação
app = FastAPI()

# Criando/Herdando a Classe do pydantic
class DadosFunda(BaseModel):
    ticker: str
    



# Tela Inicil para mostrar todo o JSON com os cdados
@app.get("/")
async def hello() -> dict:
    return {}

# Para buscar apenas os dados com da empresa solcitada
@app.put("/buscaUnica")
async def putTest(input: DadosFunda) -> dict:
    return input.ticker


# Para buscar apenas os dados com das empresas solcitada
@app.put("/buscaMult")
async def putTest(input: DadosFunda) -> dict:
    return input.ticker


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8001") 