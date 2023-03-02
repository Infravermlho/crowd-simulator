from gymnasium.envs.registration import register

register(
     id="CrowdSim-v0",
     entry_point="gym_crowdsim.envs:GridWorldEnv",
     max_episode_steps=300,
)