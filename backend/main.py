from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from ai_engine import recommend_product
from context_pruning import prune_context

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load products
with open("backend/products.json") as f:
    products = json.load(f)

@app.get("/products")
def get_products():
    return products

@app.post("/recommend")
def recommend(data: dict):
    budget = data.get("budget", 10000000)
    priority = data.get("priority", "")

    pruned = prune_context(products)

    result = recommend_product(pruned, budget, priority)

    return result