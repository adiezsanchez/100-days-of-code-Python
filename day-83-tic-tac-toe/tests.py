winning_combos = []

# Generate winning combinations for rows
for row in range(1,4):
    winning_combos.append([(row, col) for col in range(3)])

# Generate winning combinations for columns
for col in range(3):
    winning_combos.append([(row, col) for row in range(1,4)])

# Add diagonal winning combinations
diagonal_1 = [(1, 0), (2, 1), (3, 2)]
diagonal_2 = [(3, 0), (2, 1), (1, 2)]
winning_combos.append(diagonal_1)
winning_combos.append(diagonal_2)

print(winning_combos)