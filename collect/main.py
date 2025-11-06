def collect_to_solve(question: str):
    complete = False
    while not complete:
        actions = plan(question)
        state = question
        for act in actions:
            state = act.execute(state)
        complete = judge(state)
    return state

def plan(question: str):
    pass

def judge(question: str):
    pass