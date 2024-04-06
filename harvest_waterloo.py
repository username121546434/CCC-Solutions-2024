from collections import deque
rows = int(input())
cols = int(input())

grid = [input() for _ in range(rows)]
start_row = int(input())
start_col = int(input())

prices = {
    'S': 1,
    'M': 5,
    'L': 10
}

checked = set()
price = 0
q = deque()
q.append((start_row, start_col))

while q:
    row, col = q[0]
    q.popleft()
    if (row, col) in checked:
        continue
    checked.add((row, col))
    price += prices[grid[row][col]]

    around = [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1)
    ]
    for row, col in around:
        try:
            x = grid[row][col]
        except IndexError:
            continue
        else:
            if row < 0 or col < 0:
                continue
        if x == '*':
            continue
        q.append((row, col))

print(price)
