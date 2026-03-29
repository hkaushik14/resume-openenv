# env.py

from tasks import tasks
import random
from grader import grade

class ResumeEnv:
    def __init__(self):
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(tasks)
        return {
            "resume": self.current_task["resume"],
            "job": self.current_task["job"]
        }

    def step(self, action):
        correct = self.current_task["answer"]

        score = grade(action, correct)

        if score == 1.0:
            reward = 1
        else:
            reward = -1

        done = True

        return {
            "observation": {
                "resume": self.current_task["resume"],
                "job": self.current_task["job"]
            },
            "reward": reward,
            "done": done,
            "info": {
                "correct_answer": correct,
                "score": score
            }
        }

    def state(self):
        return self.current_task