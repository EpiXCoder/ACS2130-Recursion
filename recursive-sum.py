def sum(n):

  if n == 1: #base
    return 1
  return n + sum(n-1) #recursive