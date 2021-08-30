# Import routines
import numpy as np
import math
import random


# Defining hyperparameters
#Number of Cities
m = 5
#Number of hours
t = 24
#Number of days
d = 7
#Cost per kilometer
C = 5
#Revenue per kilometer
R = 9


class CabDriver():

    def __init__(self):
        "Initialization of state and definition of action and state space and "
        self.state_init = [np.random.randint(0,m), np.random.randint(0,t),np.random.randint(0,d)]
        self.state_space = [[i,j,k] for i in range(m) for j in range(t) for k in range(d)]
        self.action_space = [[i,j] for i in range(m) for j in range(m) if i!=j or i==0]
             

        # First round
        self.reset()
        self.total_time = 0
        self.max_time = 24*30
        self.action_size = m*(m-1) + 1


    ## Encoding state (or state-action) for NN input
    def state_encod_arch1(self, state):
        state_encod = np.zeros((m+t+d))
        state_encod[state[0]] = 1
        state_encod[m + np.int(state[1])] = 1
        state_encod[m + t + np.int(state[2])] = 1

        
        return state_encod


    def state_encod_arch2(self, state, action):
        state_encod = np.zeros(m+t+d+m+m)
        state_encod.reshape(1,m+t+d+m+m)
        state_encod[state[0]] = 1
        state_encod[m+np.int(state[1])] = 1
        state_encod[m+np.int(t+state[2])] = 1
        state_encod[m+t+d+action[0]] = 1
        state_encod[m+t+d+m+action[1]] = 1
        return state_encod  



    def requests(self, state):
        location = state[0]
        if location == 0:
            requests = np.random.poisson(2)
            
        elif location == 1:
            requests = np.random.poisson(12)
                        
        elif location == 2:
            requests = np.random.poisson(4)
            
        elif location == 3:
            requests = np.random.poisson(7)
            
        else:
            requests = np.random.poisson(8)    
            

        if requests >15:
            requests =15

        possible_actions_index = random.sample(range(1, self.action_size), requests)
        actions = [self.action_space[i] for i in possible_actions_index]

       # [0, 0] is not a 'request', but it is one of the possible actions
        actions.append([0,0])
        possible_actions_index.append(0)
        return possible_actions_index, actions   



    def reward_func(self, state, action, Time_matrix):
        "Takes state, action and Time-matrix and returns reward"
        start_loc, time, day = state
        pickup, drop = action


        if pickup == 0 and drop == 0:
            return -5
        else:
            "Calculate the reward for actionts"
            time_elapsed_till_pickup = Time_matrix[start_loc, pickup, int(time), int(day)]

            # when pickup is not same as current location, current time and day could change

            time_next = (time +  time_elapsed_till_pickup) % t
            day_next = (day + (time +  time_elapsed_till_pickup)//t) % d

            return (R*Time_matrix[pickup, drop, int(time_next),int(day_next)] - C*(Time_matrix[pickup, drop, int(time_next), int(day_next)] + Time_matrix[start_loc, pickup, int(time), int(day)]))




    def next_state_func(self, state, action, Time_matrix):
        "Takes state and action as input and returns next state"
        start_loc, time, day = state
        pickup, drop = action
        
        
        if pickup == 0 and drop == 0:
            # when action is (0,0)
            time_elapsed = 1
            
            self.total_time = self.total_time + time_elapsed
        else:

            # when pickup is not same as current location, current time and day could change

            time_elapsed_till_pickup = Time_matrix[start_loc, pickup, int(time), int(day)]
            time_next_temp = (time +  time_elapsed_till_pickup) % t
            day_next_temp = (day + (time +  time_elapsed_till_pickup)//t) % d

            time = time_next_temp
            day = day_next_temp

            time_elapsed = Time_matrix[pickup, drop,  int(time), int(day)]
            
            self.total_time = self.total_time +  time_elapsed + time_elapsed_till_pickup

        time_next = (time + time_elapsed)%t
        day_next = (day + (time + time_elapsed)//t) % d
        
        time_next = np.int(time_next)
        day_next = np.int(day_next)
        
        # check whether it is a terminal state
        if (self.total_time >= self.max_time):
        	terminal_state = 1
        	self.total_time = 0
        else:
        	terminal_state =0

        terminal_state = bool(terminal_state) # returns terminal state as True or False

        next_state = [drop, time_next, day_next]
        
        return next_state, terminal_state
    

    def reset(self):
        return self.state_init
