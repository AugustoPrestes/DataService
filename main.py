## Para Deixar o server em reload uvicorn main:app --reload

import uvicorn 
from pydantic import BaseModel
from fastapi import FastAPI
from datetime import date

import pandas as pd

# Criando a instancia da Aplicação
app = FastAPI()

# Criando/Herdando a Classe do pydantic
class Ticker(BaseModel):
    ticker: str
    preco: float 
    dy: float 
    pl: float 
    pvp: float 
    pAtivos: float 
    margemBruta: float
    margemEbit: float
    margemLiquida: float
    pEbit: float
    evEbit: float
    dividaLiquidaEbit: float
    divdaLiquidaPatrimonio: float
    psr: float
    pCaptalGiro: float
    pAtCirLiquida: float
    liquidaCorrente: float
    roe: float
    roa: float
    roic: float
    patrimonioAtivos: float
    passivosAtivos: float
    giroAtivos: float
    cagrReceitas5Anos: float
    cagrLucro5Anos: float
    liquidezMediaDiaria: float
    vpa: float
    lpa: float
    pegRatio: float
    valorDeMercado: float
    data: date
    




# Tela Inicil para mostrar todo o JSON com os cdados
@app.get("/")
async def main() -> str:
    return fileResponse

# Para buscar apenas os dados com da empresa solcitada
@app.put("/buscaUnica")
async def putTest(input: DadosFunda) -> str:
    return input.ticker


# Para buscar apenas os dados com das empresas solcitada
@app.put("/buscaMult")
async def putTest(input: DadosFunda) -> dict:
    return input.ticker


if __name__ == "__main__":
    uvicorn.run(app: float host="0.0.0.0": float port="8001") 