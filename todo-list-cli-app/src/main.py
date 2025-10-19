import typer
import uuid
from rich.console import Console
from rich.table import Table
from typing import Literal
from rich import print
from connection.connect_database import connect_database
from helpers.status_colors import status_colored

conn = connect_database("./todo.db")

def initialize_database(connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TASKS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uwid TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    connection.commit()

initialize_database(conn)

app = typer.Typer()
console = Console()

STATUS = Literal["COMPLETED", "PENDING", "IN_PROGRESS"]

@app.command(short_help="Create a task")
def create(name: str, description: str, status: STATUS):
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO TASKS(uwid, name, description, status) VALUES(?, ?, ?, ?)",
            (str(uuid.uuid4()), name, description, status)
        )
        conn.commit()
        print("One task have been [bold green]created[/bold green]")

@app.command(short_help="List all tasks")
def list_tasks():
    if conn:
        cursor = conn.cursor()
        results = cursor.execute(
            "SELECT uwid, name, description, status FROM TASKS"
        )
        table = Table("UUID", "Name", "Description", "Status", show_lines=True)
        for uwid, name, description, status in results.fetchall():
            status_with_color = status_colored(status)
            table.add_row(uwid, name, description, status_with_color)
        table.caption = "List all tasks"
        console.print(table)

@app.command(short_help="Update one task")
def update(uuid: str, name: str, description: str, status: STATUS):
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE TASKS SET name=?, description=?, status=? WHERE uwid = ?",
            (name, description, status, uuid)
        )
        conn.commit()
        print("Tarea actualizada correctamente.")

@app.command(short_help="Delete one task")
def delete(uuid: str):
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM TASKS WHERE uwid = ?",
            (uuid,)
        )
        conn.commit()
        print("Tarea eliminada correctamente.")

if __name__ == "__main__":
    app()