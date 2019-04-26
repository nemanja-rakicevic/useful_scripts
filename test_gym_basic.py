

import argparse
import gym


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-s', '--show', default=False, type=bool,
                    help="Render the environment.")
parser.add_argument('-p', '--print', default=False, type=bool,
                    help="Print some output")
parser.add_argument('-m', '--mujoco', default=False, type=bool,
                    help="Check if MuJoCo works.")
args = parser.parse_args()


if args.mujoco:
    env = gym.make('Reacher-v2')
else:
    env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    if args.show: env.render()
    action = env.action_space.sample()
    if args.print: action
    env.step(action) # take a random action
env.close()