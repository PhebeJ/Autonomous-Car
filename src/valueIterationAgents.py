# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Car AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/car.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is action dict with default 0
     
    "*** YOUR CODE HERE ***"
    
    for i in range(iterations):
        self.prevBatch = self.values.copy() 
        for state in mdp.getStates():
            qValues = util.Counter()
            for action in mdp.getPossibleActions(state):
                for (statePrime, tValue) in mdp.getTransitionStatesAndProbs(state, action):
                    qValues[action] += tValue * (mdp.getReward(state, action, statePrime) + self.discount * self.prevBatch[statePrime])
            self.values[state] = qValues[qValues.argMax()]

  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    qValue = 0 
    for (sp, tValue) in  self.mdp.getTransitionStatesAndProbs(state, action):  
        qValue += tValue * (self.mdp.getReward(state, action, sp) + self.discount * self.values[sp] )
    return qValue;

    #util.raiseNotDefined()

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    if self.mdp.isTerminal(state) :
        return None 
    else:
        qValues = util.Counter()
        actions = self.mdp.getPossibleActions(state)
        for action in actions:
            qValues[actions.index(action)] = self.getQValue(state, action) 
        return actions[qValues.argMax()];      
    #util.raiseNotDefined()

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  
