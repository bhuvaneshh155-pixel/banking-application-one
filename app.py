from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple Banking API")


account = {"balance": 0.0}

class Transaction(BaseModel):
    amount: float

@app.get("/balance")
def get_balance():
    return {"balance": account["balance"]}

@app.post("/deposit")
def deposit(tx: Transaction):
    if tx.amount <= 0:
        raise HTTPException(status_code=400, detail="Deposit must be greater than zero.")
    account["balance"] += tx.amount
    return {"message": "Success", "balance": account["balance"]}

@app.post("/withdraw")
def withdraw(tx: Transaction):
    if tx.amount <= 0:
        raise HTTPException(status_code=400, detail="Withdrawal must be greater than zero.")
    if tx.amount > account["balance"]:
        raise HTTPException(status_code=400, detail="Insufficient funds.")
    account["balance"] -= tx.amount
    return {"message": "Success", "balance": account["balance"]}
