from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import networkx as nx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GraphInput(BaseModel):
    edges: list[list[str]]

@app.get("/")
def read_root():
    return {"message": "Backend is running"}

@app.post("/graph")
def receive_graph(data: GraphInput):
    G = nx.Graph()
    G.add_edges_from(data.edges)

    is_planar, _ = nx.check_planarity(G)

    vertices = sorted(list(G.nodes()))
    edges = [[u, v] for u, v in G.edges()]

    return {
        "message": "Graph checked successfully",
        "vertices": vertices,
        "edges": edges,
        "number_of_vertices": G.number_of_nodes(),
        "number_of_edges": G.number_of_edges(),
        "is_planar": is_planar,
        "result_text": "Planar" if is_planar else "Non-planar",
    }