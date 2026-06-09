
from fastapi import FastAPI, HTTPException,status
app=FastAPI()
expenses={}
@app.post("/expenses",status_code=status.HTTP_201_CREATED)
def create_expense(expense:dict):
    if "description" not in expense:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="description is required")
    if "amount" not in expense:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="amount is required")
    if not isinstance (expense["amount"],(int,float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="amount must be a number")
    new_id=len(expenses)+1
    expenses[new_id]={"id":new_id,"description":expense["description"],"amount":expense["amount"]}
    return expenses[new_id]


@app.get("/expenses", status_code=status.HTTP_200_OK)
def get_expenses():
    return expenses



@app.get("/expenses/{expense_id}",status_code=status.HTTP_200_OK)
def get_expense(expense_id:int):
    if expense_id not in expenses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="expense not found")
    return expenses[expense_id]




@app.delete("/expenses/{expense_id}", status_code=status.HTTP_200_OK)
def delete_expense(expense_id:int):
    if expense_id not in expenses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="expense not found")
    deleted=expenses.pop(expense_id)
    return {"message":"deleted successfully","data":deleted}


@app.put("/expenses/{expense_id}", status_code=status.HTTP_200_OK)
def update(expense_id:int,expense:dict):
    if expense_id not in expenses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="expense not found")
    if "discription" not in expense:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="description is required")
    if "amount" not in expense:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="amount is required") 
    if not isinstance(expense["amount"],(int,float)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="amount must be a number") 
    expenses[expense_id]={"id":expense_id, "description":expense["description"], "amount":expense["amount"]}
    return expenses[expense_id]  
