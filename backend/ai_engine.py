def recommend_product(products, budget, priority):
    best = None
    best_score = 0

    for p in products:
        score = 0

        # Budget check
        if p["price"] <= budget:
            score += 5

        # Feature scoring
        score += len(p["features"])

        if priority.lower() in " ".join(p["features"]).lower():
            score += 3

        if score > best_score:
            best_score = score
            best = p

    return {
        "recommended": best,
        "score": best_score
    }