import numpy as np
import random


grid_size = (3,2)

class QlearningAgent:
    
    def __init__(self, alpha= 0.1, gamma= 0.9, epsilon= 0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.moves = np.linspace(-1, 1, 21)
        self.Q = np.zeros((grid_size[0],grid_size[1], len(self.moves) ))
        self.state = (0,0)
        self.nextAction = -1

    def choose_action(self, s):
        if self.nextAction == -1:
            if random.random() < self.epsilon:
                return (self.moves[random.randint(0,len(self.moves)-1)])
            else:
                return (self.moves[np.argmax(self.Q[s[0],s[1]])])
        else:
            return self.nextAction
        
    def get_state_from_observation(self, observation):
        position, velocity = observation[0], observation[1]
        if position > -0.35 :
            x = 0
        if position <= -0.6 :
            x = 1
        if position <= -0.35 and position> -0.6:
            x = 2
        if velocity > 0 :
            y = 0
        if velocity <= 0 :
            y = 1
        return(x,y)
    
    def fit_step(self, s, a, r, new_state):
        if random.random() < self.epsilon:
            next_action = self.moves[random.randint(0,len(self.moves)-1)]
        else:
            next_action = self.moves[np.argmax(self.Q[s[0],s[1]])]
        max_Q_next_step = np.max(self.Q[new_state[0],new_state[1]])    
        self.Q[s[0],s[1],self.get_action_index(a)] += self.alpha*(r+ self.gamma*max_Q_next_step - self.Q[s[0],s[1],self.get_action_index(a)])
        
        self.state = new_state
        self.nextAction = next_action
            
    def reset_position(self):
        self.state = (0,0)
    
    def get_action_index(self,action):
        i = 0
        for e in self.moves:
            if e == action:
                return(i)
            i+=1
            
    def choose_best_action(self, s):
        return (self.moves[np.argmax(self.Q[s[0],s[1]])])

        