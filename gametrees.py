#!/usr/bin/python3

# Both the Minimax and the Alpha-beta algorithm represent the players
# as integers 0 and 1. The moves by the two players alternate 0, 1, 0, 1, ...,
# so in the recursive calls you can compute the next player as the subtraction
# 1-player.
# The number of recursive calls to the algorithms is kept track with
# the variable 'calls'. Let your implementation increase this variable
# by one in the beginning of each recursive call. This variable is
# also used as part of the evaluation of the implementations.

calls = 0

def minimax(player,state,depthLeft):
  global calls
  calls += 1
  if depthLeft == 0:
    return state.value()
### INSERT YOUR IMPLEMENTATION OF MINIMAX HERE
### It should be recursively calling 'minimax'.

def alphabeta(player,state,depthLeft,alpha,beta):
  global calls
  calls += 1
  if depthLeft == 0:
    return state.value()
### INSERT YOUR IMPLEMENTATION OF ALPHABETA HERE
### It should be recursively calling 'alphabeta'.

def gamevalue(startingstate,depth):
  global calls
  calls = 0
  v = minimax(0,startingstate,depth)
  print(str(v) + " value with " + str(calls) + " calls with minimax to depth " + str(depth))
  calls = 0
  v = alphabeta(0,startingstate,depth,0-float("inf"),float("inf"))
  print(str(v) + " value with " + str(calls) + " calls with alphabeta to depth " + str(depth))
  calls = 0
