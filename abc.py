# Read the input grid as a list of strings
grid = [input() for _ in range(3)]

# Define a function to check if a cell is valid
def is_valid(row, col):
  return 0 <= row < 3 and 0 <= col < 3

# Define a function to find the adjacent cells of a given cell
def get_adjacent(row, col):
  # Use a list of offsets to represent the eight directions
  offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  # Initialize an empty list to store the adjacent cells
  adjacent = []
  # Loop through the offsets and add the valid cells to the list
  for dr, dc in offsets:
    nr = row + dr
    nc = col + dc
    if is_valid(nr, nc):
      adjacent.append((nr, nc))
  # Return the list of adjacent cells
  return adjacent

# Define a function to find the lexicographically smallest word of length 3
def find_smallest_word():
  # Initialize the smallest word as an empty string
  smallest = ""
  # Loop through all the cells in the grid
  for r in range(3):
    for c in range(3):
      # Get the first letter from the current cell
      first = grid[r][c]
      # Loop through all the adjacent cells of the current cell
      for nr, nc in get_adjacent(r, c):
        # Get the second letter from the adjacent cell
        second = grid[nr][nc]
        # Loop through all the adjacent cells of the adjacent cell
        for nnr, nnc in get_adjacent(nr, nc):
          # Get the third letter from the adjacent cell
          third = grid[nnr][nnc]
          # Skip if the third cell is the same as the first cell
          if (nnr, nnc) == (r, c):
            continue
          # Form a word from the three letters
          word = first + second + third
          # Compare the word with the smallest word so far
          # If the word is lexicographically smaller or the smallest word is empty, update the smallest word
          if smallest == "" or word < smallest:
            smallest = word
  # Return the smallest word
  return smallest

# Print the smallest word
print(find_smallest_word())