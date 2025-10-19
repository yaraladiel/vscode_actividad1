# Todo list app with Typer
Esta es una app de consola de comando / terminal creada con [Typer](https://typer.tiangolo.com/), una librería de Python para crear aplicaciones CLI.

## Recreación del entorno virtual
Para instalar las librerías que estoy usando en este proyecto te dejo el archivo `requirements.txt` donde se lista todo las librerías que necesita esta app. Para instalarlas, luego de tener activo tu entorno virtual, ejecuta el siguiente comando:

```sh
pip install -r requirements.txt
```

## Listado de comandos
Ejecutando el siguiente comando podrás ver una lista de los subcomandos que puedes ejecutar en este proyecto:
#### 1. Mostrar todos los comandos y opcions
```sh
python src/main.py --help
```
#### 2. Listar todas las tareas
```sh
python src/main.py list
```
#### 3. Crear una tarea
```sh
python src/main.py create "Estudiar para el examen" "El examen será el próximo Jueves" IN_PROGRESS
```
#### 4. Actualizar una tarea
```sh
python src/main.py update 026936b1-a131-4cc6-9abd-812089383af6 "Estudiar para el examen" "El examen será el próximo Jueves" IN_PROGRESS
```
#### 5. Eliminar una tarea
```sh
python src/main.py delete 026936b1-a131-4cc6-9abd-812089383af6
```

## Consultas SQL
La base de datos que estamos usando es [SQLite3](https://sqlite.org/). Ingresa desde la terminal / consola de comandos y ejecuta las siguientes consultas:

#### 1. Crear tabla `tasks`
```sql
CREATE TABLE tasks(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	uuid TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	status TEXT NOT NULL CHECK(status IN ('COMPLETED', 'PENDING', 'IN_PROGRESS'))
);
```

#### 2. Insertar registros
```sql
INSERT INTO 
	tasks(uuid, name, description, status) 
VALUES(
	'770f1a0e-d370-4a12-b89e-b3c994acaecd', 
	'Leer un libro', 'Leer es importante para el crecimiento profesional',
	'PENDING'
	);
```

