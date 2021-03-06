import random


class QLearn:
    def __init__(self, actions, epsilon=0.1, alpha=0.2, gamma=0.9):
        self.q = {}

        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.actions = actions

    def getQ(self, state, action):
        # if (state,action) in self.q:
        #     print "Best Action Present"
        #randomized_action_in_case_none=random.choice(self.actions)
        #return self.q.get((state, action), randomized_action_in_case_none)
        return self.q.get((state, action), 1.0)

    def learnQ(self, state, action, reward, value):
        oldv = self.q.get((state, action), None)
        if oldv is None:
            self.q[(state, action)] = reward
        else:
            self.q[(state, action)] = oldv + self.alpha * (value - oldv)

    def chooseAction(self, state):
        #print "State: "+state
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
            #print "Eps: Random choice"
        else:
            q = [self.getQ(state, a) for a in self.actions]
            #print "options  :: "+str(q)
            maxQ = max(q)
            count = q.count(maxQ)  
            if count > 1:
                best = [i for i in range(len(self.actions)) if q[i] == maxQ]
                i = random.choice(best)
            else:
                i = q.index(maxQ)
            action = self.actions[i]
        return action

    def learn(self, state1, action1, reward, state2):
        maxqnew = max([self.getQ(state2, a) for a in self.actions])
        #print "Learning with reward "+str(reward)
        self.learnQ(state1, action1, reward, reward + self.gamma*maxqnew)

import math
def ff(f,n):
    fs = "{:f}".format(f)
    if len(fs) < n:
        return ("{:"+n+"s}").format(fs)
    else:
        return fs[:n]