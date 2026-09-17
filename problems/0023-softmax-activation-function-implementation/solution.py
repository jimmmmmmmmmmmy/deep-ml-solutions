import math

scores = [1, 2, 3]
def softmax(scores: list[float]) -> list[float]:
    sf_list = []
    max_z = max(scores)
    for z in scores:
        sf_list.append(math.exp(z - max_z))
    sf_sum = sum(sf_list)
    for i in range(len(sf_list)):
        sf_list[i] = round((sf_list[i] / sf_sum), 4)
    return sf_list