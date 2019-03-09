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
  if depthLeft == 0 or  not len(state.applicableActions(player))  :
    return state.value()
  next_player = max(0,1-player)
  #print(f"current player:{player} and next player: {next_player}")
  if player == 1: #Maximizing Player 
    best = -float("inf")
    for action in state.applicableActions(player):
      next_state = state.successor(player,action)
      v = minimax(next_player,next_state,depthLeft-1)
      best = max(best,v)
  
  else: #minimizing player 
    best = float("inf")
    for action in state.applicableActions(player):
      next_state = state.successor(player,action)
      v = minimax(next_player,next_state,depthLeft-1)
      best = min(best,v)
  # print(f"best : {best} at depth: {depthLeft} for player: {player}") 
  return best

### INSERT YOUR IMPLEMENTATION OF MINIMAX HERE
### It should be recursively calling 'minimax'.

def alphabeta(player,state,depthLeft,alpha,beta):
  global calls
  calls += 1
  if depthLeft == 0 or  not len(state.applicableActions(player))  :
    return state.value()
  next_player = max(0,1-player)
  #print(f"current player:{player} and next player: {next_player}")
  if player == 1: #Maximizing Player 
    best = -float("inf")
    for action in state.applicableActions(player):
      next_state = state.successor(player,action)
      v = alphabeta(next_player,next_state,depthLeft-1,alpha,beta)
      if (v is None):
        print("V is none ")
      best = max(best,v)
      alpha = max(alpha,v)
      if alpha >= beta :
        break
  else: #minimizing player 
    best = float("inf")
    for action in state.applicableActions(player):
      next_state = state.successor(player,action)
      v = alphabeta(next_player,next_state,depthLeft-1,alpha,beta)
      best = min(best,v)
      beta = min(beta,v)
      if alpha >= beta :
        break
  # print(f"best : {best} at depth: {depthLeft} for player: {player}") 
  return best
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


