from gym.envs.registration import register

register(
    id='gym_crowded/GridWorld-v0',
    entry_point='gym_crowded.envs:GridWorldEnv',
    max_episode_steps=300,
)