def prune_context(products, max_chars=500):
    pruned = []
    total = 0

    for p in products:
        text = str(p)
        if total + len(text) > max_chars:
            break
        pruned.append(p)
        total += len(text)

    return pruned