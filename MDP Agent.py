def get_state_utilities(U,epsilon,rewards):  # Function to get the utility function for the state space with a specific epsilon error
    itr=0
    while True:
        itr = itr +1
        nextU = [[0,0,0], [0,0,1]]
        error = 0
        for r in reversed(range(ROW)):
            for c in range(COL):
                if (r == 1 and c == 2) :
                    continue
                arr=[UtilCalc(U, r, c, act) for act in range(TOT_ACTIONS)]
                nextU[r][c] = max(arr) 
                error = max(error, abs(nextU[r][c]-U[r][c]))
        U = nextU
        if error < epsilon * (1-DISCOUNT) / DISCOUNT:
            break
    print(" ")    
    return U,itr


def Util(U, r, c, act):     # Utility obtained by doing a specific action in a specific state
    a, b = ACTIONS[act]
    nR, nC = r+a, c+b
    if nR < 0 or nC < 0 or nR >= ROW or nC >= COL : 
        return U[r][c]
    else:
        return U[nR][nC] 


def reward(r,c):     # Function to get the reward in a specific state
    if (r,c)==(0,2):
        return -0.05
    elif (r,c)==(1,2):
       return 1
    else:
        return -0.1
  
  
def UtilCalc(U, r, c, action):   # Function to get the Utility of a specific state by perfoming an action
    if action==4:
        u= reward(r,c)+ DISCOUNT*U[r][c]
        
    else:    
     u=reward(r,c)
     u += 0.05 *( DISCOUNT * Util(U, r, c, (action-1)%4))
     u += 0.9 * ( DISCOUNT * Util(U, r, c, action))
     u += 0.05 *( DISCOUNT * Util(U, r, c, (action+1)%4))
     
    return u


# Finding the utilities at convergence and number of iterations for convergence

rewards=  [-0.1,-0.1,1,-0.1,-0.1,-0.05]
epsilon=0.01
DISCOUNT = 0.999
TOT_ACTIONS = 5
ACTIONS = [(-1, 0),(0,1), (1,0), (0,-1)] # North, East, South, West
ROW = 2
COL = 3
U = [[0,0,0], [0,0,0]]

U,itr = get_state_utilities(U,epsilon,rewards)

print("Utilities at convergence: ", U)
print("Value iterations taken: ", itr)

