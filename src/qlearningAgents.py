# qlearningAgents.py
# ------------------
from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent

    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discount (discount rate)

    Functions you should use
      - self.getLegalActions(state)
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)

    "*** YOUR CODE HERE ***"
    
    self.qValues = util.Counter()

  def getQValue(self, state, action):
    """
      Returns Q(state,action)
      Should return 0.0 if we never seen
      a state or (state,action) tuple
    """
    "*** YOUR CODE HERE ***"
    
    if (state, action) not in self.qValues:
        self.qValues[(state, action)] = 0

    return self.qValues[(state, action)]
    
    #util.raiseNotDefined()


  def getValue(self, state):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    "*** YOUR CODE HERE ***"
    
    actions = self.getLegalActions(state)
    if len(actions) == 0:
        return 0.0
    else:
        qvalues = util.Counter()
        for action in actions:
            qvalues[action] = self.getQValue(state, action)
        return qvalues[qvalues.argMax()];
            
    #util.raiseNotDefined()

  def getPolicy(self, state):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    "*** YOUR CODE HERE ***"
    
    actions = self.getLegalActions(state)
    if len(actions) == 0:
        return None
    else:
        qvalues = util.Counter()
        for action in actions:
            qvalues[actions.index(action)] = self.getQValue(state, action)
        return actions[qvalues.argMax()];
    
    #util.raiseNotDefined()

  def getAction(self, state):
    """
      Compute the action to take in the current state.  With
      probability self.epsilon, we should take a random action and
      take the best policy action otherwise.  Note that if there are
      no legal actions, which is the case at the terminal state, you
      should choose None as the action.

      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)
    """
    # Pick Action
    legalActions = self.getLegalActions(state)

    "*** YOUR CODE HERE ***"
    
    if len(legalActions) == 0:
        return None
    elif util.flipCoin(self.epsilon):
        return random.choice(legalActions)
    else:
        return self.getPolicy(state)
    
    #util.raiseNotDefined()

  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a
      state = action => nextState and reward transition.
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf
    """
    "*** YOUR CODE HERE ***"
    self.qValues[(state, action)] = (1 - self.alpha) * self.qValues[(state, action)] + self.alpha * (reward + self.discount * self.getValue(nextState))
    
    #util.raiseNotDefined()

class CarQAgent(QLearningAgent):
  "Exactly the same as QLearningAgent, but with different default parameters"

  def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
    """
    These default parameters can be changed from the car.py command line.
    For example, to change the exploration rate, try:
        python car.py -p CarQLearningAgent -a epsilon=0.1

    alpha    - learning rate
    epsilon  - exploration rate
    gamma    - discount factor
    numTraining - number of training episodes, i.e. no learning after these many episodes
    """
    args['epsilon'] = epsilon
    args['gamma'] = gamma
    args['alpha'] = alpha
    args['numTraining'] = numTraining
    self.index = 0  # This is always Car
    QLearningAgent.__init__(self, **args)

  def getAction(self, state):
    """
    Simply calls the getAction method of QLearningAgent and then
    informs parent of action for Car.  Do not change or remove this
    method.
    """
    action = QLearningAgent.getAction(self,state)
    self.doAction(state,action)
    return action


class ApproximateQAgent(CarQAgent):
  """
     ApproximateQLearningAgent

     You should only have to overwrite getQValue
     and update.  All other QLearningAgent functions
     should work as is.
  """
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    CarQAgent.__init__(self, **args)

    # You might want to initialize weights here.
    "*** YOUR CODE HERE ***"
    self.weights = util.Counter()
    
  def getQValue(self, state, action):
    """
      Should return Q(state,action) = w * featureVector
      where * is the dotProduct operator
    """
    "*** YOUR CODE HERE ***"
    
    features = self.featExtractor.getFeatures(state, action)
    qValue = 0.0
    for feature, value in features.iteritems():
        qValue += self.weights[feature] * value
    
    return qValue
    #util.raiseNotDefined()

  def update(self, state, action, nextState, reward):
    """
       Should update your weights based on transition
    """
    "*** YOUR CODE HERE ***"
    
    correction = (reward + self.discount * self.getValue(nextState)) - self.getQValue(state, action) 
    
    features = self.featExtractor.getFeatures(state, action)
    for feature, value in features.iteritems():
        self.weights[feature] = self.weights[feature] + self.alpha * correction * value
    
    #util.raiseNotDefined()

  def final(self, state):
    "Called at the end of each game."
    # call the super-class final method
    CarQAgent.final(self, state)

    # did we finish training?
    if self.episodesSoFar == self.numTraining:
      # you might want to print your weights here for debugging
      "*** YOUR CODE HERE ***"
      for feature, value in self.weights.iteritems():
          print "Weight of ", feature, " is ", value
      pass
