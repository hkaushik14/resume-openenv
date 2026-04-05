#  Resume Screening OpenEnv

##  Description
This project simulates a real-world **resume screening task** where an AI agent decides whether to **shortlist** or **reject** a candidate based on their resume and job description.

---

##  Objective
- Analyze resume text  
- Compare with job requirements  
- Take decision: `shortlist` or `reject`  

---

##  Action Space
- `shortlist`
- `reject`

---

##  Observation Space
Each step returns:
- `resume` → candidate profile  
- `job` → job description  

---

##  Tasks
- **Easy** → clear match → shortlist  
- **Medium** → weak match → reject  
- **Hard** → irrelevant profile → reject  

---

##  Reward Function
- +1 → correct decision  
- -1 → incorrect decision  

---

##  Grader
- Returns score between **0.0 and 1.0**  
- Deterministic and reproducible  

---

##  Baseline
A simple rule-based agent:
- If resume contains *Python + Machine Learning* → shortlist  
- Otherwise → reject  

**Baseline Score:** `1.0`


---

##  API Endpoints

| Endpoint | Method | Description |
|----------|--------|------------|
| `/` | GET | Health check |
| `/reset` | GET | Reset environment |
| `/state` | GET | Get current state |
| `/step` | POST | Take action |
| `/grader` | POST | Evaluate action |
| `/tasks` | GET | List tasks |
| `/baseline` | GET | Run baseline |

---

##  Deployment
Deployed on Hugging Face Spaces using Docker.

 Live Demo:  
https://harsh494-resume-openenv.hf.space

---

##  Run Locally

```bash
pip install fastapi uvicorn
py -m uvicorn app:app --reload

---
title: Resume OpenEnv
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
app_file: server/app.py
pinned: false
---
