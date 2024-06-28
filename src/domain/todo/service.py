
# TodoService
# path: src/domain/todo/service.py

from typing import List
from adapters.db.schema import TodoTable
from adapters.todo_adapter import TodoAdapter
from domain.todo.model import TodoModel

class TodoService:
    def __init__(self) -> None:
        self.todo_adapter = TodoAdapter()
    
    def create(self, todo: TodoModel) -> None:
        todo = TodoTable(**todo.model_dump())
        self.todo_adapter.create(todo=todo)
    
    def get_all(self) -> List[TodoModel]:
        todos = self.todo_adapter.get_all()
        return TodoModel.from_db_model(todos)

    def get_todo_by_id(self, todo_id: str) -> TodoModel:
        todo_by_id = self.todo_adapter.get_todo_by_id(todo_id=todo_id)
        return TodoModel.from_db_model(todo_by_id)
    
    def update(self, todo: TodoModel) -> None:
        self.todo_adapter.update(todo=TodoTable(**todo.model_dump()))
    
    def delete_todo_by_id(self, todo_id: str) -> None:
        self.todo_adapter.delete_todo_by_id(todo_id=todo_id)


