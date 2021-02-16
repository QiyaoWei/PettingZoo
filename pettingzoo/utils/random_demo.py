import time
import random
import numpy as np


def random_demo(env, render=True, episodes=1):
    '''
    Runs an env object with random actions.
    '''

    env.reset()

    if hasattr(env, 'display_wait'):
        display_wait = env.display_wait
    else:
        display_wait = 0.0

    total_reward = 0
    done = False
    run_episodes = 0

    while True:
        for agent in env.agent_iter(len(env.agents)):
            if render:
                env.render()
                time.sleep(display_wait)

            obs, reward, done, _ = env.last()
            total_reward += reward
            if done:
                action = None
            elif isinstance(obs, dict) and 'action_mask' in obs:
                action = random.choice(np.flatnonzero(obs['action_mask']))
            else:
                action = env.action_spaces[agent].sample()
            env.step(action)

            run_episodes += 1

        if run_episodes == episodes:
            if render:
                env.close()
            break
        else:
            env.reset()

    print("Average total reward", total_reward / episodes)

    return total_reward
