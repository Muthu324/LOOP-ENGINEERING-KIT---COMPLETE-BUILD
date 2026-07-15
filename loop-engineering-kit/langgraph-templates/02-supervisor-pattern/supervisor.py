"""Minimal supervisor routing template for LangGraph."""
from typing import Literal, TypedDict
from langgraph.graph import END, StateGraph
class State(TypedDict): task: str; route: str; result: str
def supervisor(state: State): return {"route": "research" if "research" in state["task"].lower() else "write"}
def research(state: State): return {"result": f"Research completed: {state['task']}"}
def write(state: State): return {"result": f"Draft completed: {state['task']}"}
g=StateGraph(State); g.add_node("supervisor",supervisor); g.add_node("research",research); g.add_node("write",write)
g.set_entry_point("supervisor"); g.add_conditional_edges("supervisor",lambda s:s["route"],{"research":"research","write":"write"})
g.add_edge("research",END); g.add_edge("write",END); app=g.compile()
