file = open('data', 'r')
data = file.read().splitlines()

width = len(data[0])
height = len(data)

inner_index_start = 1


def check_left_visibility(x, y):
  tree = data[y][x]
  
  for idx in range(x):
    if tree <= data[y][idx]:
      return False
  
  return True


def check_right_visibility(x, y):
  tree = data[y][x]
  
  for idx in range(x+1, width):
    if tree <= data[y][idx]:
      return False
  
  return True


def check_up_visibility(x, y):
  tree = data[y][x]
  
  for idy in range(y):
    if tree <= data[idy][x]:
      return False
  
  return True


def check_down_visibility(x, y):
  tree = data[y][x]
  
  for idy in range(y+1, height):
    if tree <= data[idy][x]:
      return False
  
  return True


def count_left(x, y):
  tree = data[y][x]
  counter = 0

  for idx in range(x):
    if tree <= data[y][idx]:
      counter += 1
  
  return counter


def count_right(x, y):
  tree = data[y][x]
  counter = 0
  
  for idx in range(x+1, width):
    if tree <= data[y][idx]:
      counter += 1
  
  return counter


def count_up(x, y):
  tree = data[y][x]
  counter = 0
  
  for idy in range(y):
    if tree <= data[idy][x]:
      counter += 1
  
  return counter


def count_down(x, y):
  tree = data[y][x]
  counter = 0
  
  for idy in range(y+1, height):
    if tree <= data[idy][x]:
      counter += 1
  
  return counter

visible = 0
for y in range(height):
  for x in range(width):
     if check_left_visibility(x, y) or check_up_visibility(x, y) or check_right_visibility(x, y) or check_down_visibility(x, y):
        visible += 1

max_scenic_score = 0
for y in range(height):
  for x in range(width):
    scenic_score = count_left(x,y) * count_up(x,y) * count_right(x,y) * count_down(x,y)
    if max_scenic_score < scenic_score:
      max_scenic_score = scenic_score

print(max_scenic_score)

# 2371446 too high
