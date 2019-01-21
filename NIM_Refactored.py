import random

#check for win condition
def winCondition (summ, lastAction, goal, endGame):
  if summ == goal:
    print (lastAction, "wins!")
    endGame = True
  elif summ > goal:
    print (lastAction, "looses")
    endGame = True
  return endGame

def playerInputRequest (pick, step):
  try:
    print ("Pick number from 1 to", step)
    pick = int(input())
  except ValueError:
    print ("Hey! Pick the number please!")
  return pick

#Players action
def inputFromPlayer (step, summ, goal, pick, endGame):
  print ("\n___________________\nPlayers turn:")
  lastAction = "Player"
  while pick not in range(1, step+1):
    pick = playerInputRequest (pick, step)
  summ = printResult (lastAction, pick, summ)
  endGame = winCondition (summ, lastAction, goal, endGame)
  return (summ, endGame)

#print result of action
def printResult (lastAction, pick, summ):
  print (lastAction, "picked number", pick)
  summ = summ + pick
  print ("The sum of the numbers is", summ)
  return summ

#computer picks
def computerPick (step, summ, goal, lastAction):
  if (goal - 1 - summ) % step == 0:
    pick = random.randrange(1, step)
    summ = printResult (lastAction, pick, summ)
  else:
    pick = (goal - 1 - summ) % step
    summ = printResult (lastAction, pick, summ)
  return (step, summ)

#Computer action
def computerAction (step, summ, goal, firstTurn, endGame):
  print ("\n___________________\nComputers turn:")
  lastAction = "Computer"
  if firstTurn == 0:
    firstTurn = 2
    step, summ = computerPick (step, summ, goal, lastAction)
  else:
    if goal - summ <= step:
      pick = goal - summ
      endGame = True
      summ = printResult (lastAction, pick, summ)
    else:
      step, summ = computerPick (step, summ, goal, lastAction)
  endGame = winCondition (summ, lastAction, goal, endGame)
  return (summ, endGame, firstTurn)

def pickGoal (step, goal):
  while goal / step < 2:
    try:
      goal = int(input("Enter a threshold number (at least two times more than a step)\n"))
    except ValueError:
      print ("Hey! Pick the number please!")
  return goal

def pickStep (step):
  print ("_________NIM_________")
  while step < 2:
    try:
      step = int(input("Enter the maximum step (at least 2)\n"))
    except ValueError:
      print ("Hey! Pick the number please!")
  return step

def pickFirstOrSecondTurn (firstTurn):
  while (1 < firstTurn or firstTurn < 0):
    try:
      firstTurn = int(input("Do you want to make the first move?\n0 - if not, 1 - if yes.\n"))
    except ValueError:
      print ("Choose 0 or 1, please!")
  return firstTurn

#variable declaration
resultSumm, step, goal, pick, firstTurn, endGame  = 0, 0, 0, 0, 2, False

#Start of the game: player picks step and goal:
step = pickStep (step)
goal = pickGoal (step, goal)

#Player picks first or second turn:
firstTurn = pickFirstOrSecondTurn (firstTurn)

#New Gameplay:
while endGame == False:
  if firstTurn == 1:
    resultSumm, endGame = inputFromPlayer (step, resultSumm, goal, pick, endGame)
    if endGame == True:
      break
    else:
      resultSumm, endGame, firstTurn = computerAction (step, resultSumm, goal, firstTurn, endGame)
  else:
    resultSumm, endGame, firstTurn = computerAction (step, resultSumm, goal, firstTurn, endGame)
    if endGame == True:
      break
    else:
      resultSumm, endGame = inputFromPlayer (step, resultSumm, goal, pick, endGame)

