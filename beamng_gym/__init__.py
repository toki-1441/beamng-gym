from gymnasium.envs.registration import register

register(
    id="BeamNG-v0",
    entry_point="beamng_gym.envs.env:BeamNGEnv",
)
