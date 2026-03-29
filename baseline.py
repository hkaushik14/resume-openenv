# baseline.py

from env import ResumeEnv

def simple_agent(resume):
    resume = resume.lower()

    if "python" in resume and "machine learning" in resume:
        return "shortlist"
    else:
        return "reject"

def run_baseline():
    env = ResumeEnv()
    scores = []

    for _ in range(3):
        obs = env.reset()
        action = simple_agent(obs["resume"])
        result = env.step(action)

        scores.append(result["info"]["score"])

    avg_score = sum(scores) / len(scores)
    print("Baseline Score:", avg_score)

if __name__ == "__main__":
    run_baseline()