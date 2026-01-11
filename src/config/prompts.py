BASELINE_PROMPT = """You are a careful math assistant.

Solve the following problem.
Do NOT show your reasoning.
Return ONLY the final numeric answer.
Stop immediately after the number.

Question:
{question}

"""

SOLVER_PROMPT = """You are one of several agents solving a math problem.
Propose a solution and final numeric answer clearly.
Be concise.

Question:
{question}
"""

CRITIC_PROMPT = """You are one of several agents solving a math problem.
Review the proposed solution below.
Point out any errors or missing steps.
Do not propose a new solution yet.

Proposed solution:
{context}
"""

REFINER_PROMPT = """You are one of several agents solving a math problem.
Given the discussion so far, provide a corrected final numeric answer clearly.
Be concise.

Discussion:
{context}
"""
