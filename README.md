
Todo App tutorial
-----------------

See: https://hemanthhari2000.medium.com/the-ports-and-adapters-pattern-unraveling-the-mystery-2efbf678ab9b

poetry:
- cli for managing an app
  - manages dependencies via a unique venv
  - manages running the app and internal tools (e.g. alembic)

alembic:
- used to creates the local SQLite database

src:
- implements the app domain and ports
  - ports are Protocol classes (e.g. define the interface)
- implements the adaptors
  - adaptors define implementation of ports
- implements the FastAPI api endpoints

