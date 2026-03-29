from env import ResumeEnv

env = ResumeEnv()

obs = env.reset()
print("Observation:", obs)

result = env.step("shortlist")
print("Result:", result)