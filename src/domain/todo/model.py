
from typing import List
from pydantic import BaseModel, ConfigDict
from adapters.db.schema import TodoTable

class TodoModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str = ""
    title: str
    description: str = ""
    priority: int
    is_complete: bool

    @staticmethod
    def from_db_model(todo: TodoTable | List[TodoTable]):
        if isinstance(todo, TodoTable):
            return TodoModel.model_validate(todo)
        return [TodoModel.model_validate(t) for t in todo]

