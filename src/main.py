
import fastapi

import model
import database

app = fastapi.FastAPI()

@app.get("/")
def root():
    return ""

@app.get("/projects")
def read_projects(project_id: int, q: str|None = None) -> list[model.Project]:
    _ = project_id
    _ = q
    return database.get_all_projects()

@app.post("/projects")
def create_projects(project: model.Project) -> int:
    return database.add_project(project)

@app.get("/projects/{project_id}")
def read_project(project_id: int, q: str|None = None) -> model.Project:
    _ = q
    project = database.get_project(project_id)
    if project is None:
        raise fastapi.HTTPException(404, 'Project with a given ID not found')
    return project
        
