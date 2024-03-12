import numpy as np

def find_points(xeval, xint, idx):

  indices = np.where(np.logical_and(xeval <= xint[idx+1], xeval >= xint[idx]))[0]
  return indices

def eval_line(x0, fx0, x1, fx1, xeval):
  m = (fx1 - fx0)/(x1 - x0)
  return m*xeval - m*x0 + fx0