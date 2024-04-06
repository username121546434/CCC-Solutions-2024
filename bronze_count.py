try:
    scores = {i: 0 for i in range(76)}
    participants = int(input())

    for _ in range(participants):
        score = int(input())
        scores[score] += 1

    scores = {k: v for k, v in scores.items() if v != 0}

    for _ in range(2):
        m = max(scores.keys())
        scores.pop(m)

    bronze_score = max(scores.keys())
    num_awards = scores[bronze_score]
    print(f'{bronze_score} {num_awards}')
except Exception as e:
    print(e)
