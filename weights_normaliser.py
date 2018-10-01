def normalise_weights(weights):
    max_weight = max(v for _, v in weights.items())

    for n, v in weights.items():
        weights[n] = v / max_weight

    return weights
