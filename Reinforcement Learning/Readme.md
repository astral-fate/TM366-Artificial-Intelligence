
##Study Notes 

Reinforcement learning is a type of machine learning that focuses on how an agent (a software program or physical device) should act and behave in a given environment in order to maximize a numerical reward signal. This is done by giving the agent rewards or punishments based on the actions it has taken in different scenarios. The goal of reinforcement learning is to learn through experience and improve the agent's ability to behave optimally in order to achieve a goal.

One of the key features of reinforcement learning is the idea of trial-and-error search, where the agent must discover which actions yield the most reward by trying them out. Another key feature is the concept of delayed reward, where actions may affect not only the immediate reward but also the next situation and all subsequent rewards.

One of the challenges in reinforcement learning is the exploration vs. exploitation dilemma, where the agent must balance the need to exploit its current knowledge in order to obtain reward with the need to explore in order to make better action selections in the future.

There are four main subelements of a reinforcement learning system:

1. Policy <br>


2. Reward function <br>
          The policy defines the learning agent's way of behaving at a given time, the reward function maps states or state-action pairs to a single number indicating             the desirability of that state.
          
3. Value function <br>

       the value function specifies what is good in the long run by mapping states to the total amount of reward an agent can expect to accumulate over the future,

 
4. Model of the environment <br> 
      the model of the environment allows the agent to predict the consequences of its actions.




Reinforcement learning has numerous applications in robotics, including:
* control of autonomous vehicles
* manipulation tasks
* humanoid robots.

It can be used to train robots to perform complex tasks through trial-and-error learning and to adapt to changing environments.

One of the main challenges in reinforcement learning is the exploration vs. exploitation dilemma, where the agent must balance the need to exploit its current knowledge in order to obtain reward with the need to explore in order to make better action selections in the future. This is important because the agent must try new actions in order to discover which ones yield the most reward, but it also needs to rely on its existing knowledge in order to maximize reward in the short term.

One way to address this challenge is through the use of exploration policies, which encourage the agent to try new actions and explore its environment. These policies can be random, where the agent takes random actions with a certain probability, or they can be more structured, such as using information about the uncertainty of the environment or the value of different actions to guide exploration.

Another approach to addressing the exploration vs. exploitation dilemma is through the use of multi-armed bandits, which are a type of reinforcement learning problem that involves choosing between a set of actions with unknown rewards. In this type of problem, the agent must balance the need to explore in order to learn about the rewards of different actions with the need to exploit its current knowledge in order to maximize reward.

Overall, reinforcement learning is a powerful tool for training robots to perform complex tasks and adapt to changing environments. It allows robots to learn through trial-and-error and improve their performance over time, making it a key component of many modern robotics systems.
