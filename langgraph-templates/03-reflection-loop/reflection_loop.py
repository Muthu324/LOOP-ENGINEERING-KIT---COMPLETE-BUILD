"""Framework-neutral reflection-loop skeleton."""
def reflection_loop(problem, generate, critique, max_iterations=3):
    answer=generate(problem, None)
    for _ in range(max_iterations-1):
        feedback, accepted=critique(answer)
        if accepted: break
        answer=generate(problem, feedback)
    return answer
