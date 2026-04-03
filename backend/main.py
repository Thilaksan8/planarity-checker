from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    vertices = set()

    for edge in data.edges:
        if len(edge) == 2:
            vertices.add(edge[0])
            vertices.add(edge[1])

    return {
        "message": "Graph received successfully",
        "vertices": sorted(list(vertices)),
        "edges": data.edges,
        "number_of_vertices": len(vertices),
        "number_of_edges": len(data.edges),
    }