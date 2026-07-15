"""Optional LangGraph example. Install with: pip install -e '.[langgraph]'"""
from typing import TypedDict
from langgraph.graph import END, StateGraph

class State(TypedDict):
    value: str
    valid: bool
    iterations: int

def generate(state: State): return {"value": state["value"].strip(), "iterations": state.get("iterations", 0)+1}
def validate(state: State): return {"valid": bool(state["value"])}
def route(state: State): return "end" if state["valid"] or state["iterations"] >= 3 else "retry"

graph=StateGraph(State); graph.add_node("generate", generate); graph.add_node("validate", validate)
graph.set_entry_point("generate"); graph.add_edge("generate", "validate")
graph.add_conditional_edges("validate", route, {"retry":"generate", "end":END})
app=graph.compile()
