from fastapi import FastAPI
from pydantic import BaseModel
from env import ResumeEnv
from tasks import tasks
from grader import grade

app = FastAPI()
env = ResumeEnv()

class Action(BaseModel):
    action: str

@app.get("/")
def home():
    return {"message": "Resume OpenEnv running"}

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/reset")
def reset_post():
    return env.reset()

@app.get("/state")
def state():
    return env.state()

@app.post("/step")
def step(data: Action):
    return env.step(data.action)

@app.post("/grader")
def grader_endpoint(data: Action):
    correct = env.current_task["answer"]
    score = grade(data.action, correct)
    return {"score": score}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/baseline")
def baseline():
    from baseline import simple_agent
    scores = []

    for _ in range(3):
        obs = env.reset()
        action = simple_agent(obs["resume"])
        result = env.step(action)
        scores.append(result["info"]["score"])

    avg_score = sum(scores) / len(scores)
    return {"baseline_score": avg_score}


# ✅ IMPORTANT: OpenEnv entrypoint
def main():
    return app


# ✅ Optional: for local running with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860, reload=True)
