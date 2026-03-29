from env import ResumeEnv
from baseline import simple_agent

def run():
    env = ResumeEnv()
    scores = []

    for _ in range(3):
        obs = env.reset()
        action = simple_agent(obs["resume"])
        result = env.step(action)
        scores.append(result["info"]["score"])

    avg_score = sum(scores) / len(scores)
    print("Final Score:", avg_score)

if __name__ == "__main__":
    run()
