from fastapi import FastAPI
from app.schemas import BillCreate

app = FastAPI(
    title="Split Bill API",
    version="1.0.0"
)

# In-memory storage
bills_db = []
bill_id_counter = 1


@app.get("/")
def home():
    return {"message": "API is running"}


# CREATE bill (POST)
@app.post("/bills")
def create_bill(bill: BillCreate):
    global bill_id_counter

    new_bill = {
        "id": bill_id_counter,
        "title": bill.title,
        "total_amount": bill.total_amount,
        "participants": bill.participants,
        "paid_by": bill.paid_by,
        "is_settled": False
    }

    bills_db.append(new_bill)
    bill_id_counter += 1

    return new_bill


# READ bills (GET)
@app.get("/bills")
def get_all_bills():
    return bills_db


# UPDATE entire bill (PUT)
@app.put("/bills/{bill_id}")
def update_bill(bill_id: int, bill: BillCreate):
    for b in bills_db:
        if b["id"] == bill_id:
            b["title"] = bill.title
            b["total_amount"] = bill.total_amount
            b["participants"] = bill.participants
            b["paid_by"] = bill.paid_by
            return b

    return {"error": "Bill not found"}


# UPDATE partial bill (PATCH)

@app.patch("/bills/{bill_id}")
def settle_bill(bill_id: int):
    for bill in bills_db:
        if bill["id"] == bill_id:
            bill["is_settled"] = True
            return bill

    return {"error": "Bill not found"}


# DELETE bill (DELETE)
@app.delete("/bills/{bill_id}")
def delete_bill(bill_id: int):
    global bills_db

    bills_db = [bill for bill in bills_db if bill["id"] != bill_id]

    return {"message": "Bill deleted successfully"}


