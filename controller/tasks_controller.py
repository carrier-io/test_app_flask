from flask_restx import Resource

from util.dto import TasksDto
from model.tasks import DAO

api = TasksDto.tasks_api
tasks = TasksDto.todos


@api.route('/')
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @api.doc('list_todos')
    @api.marshal_list_with(tasks)
    def get(self):
        """List all tasks"""
        return DAO.todos_tasks

    @api.doc('create_todo')
    @api.expect(tasks)
    @api.marshal_with(tasks, code=201)
    def post(self):
        """Create a new task"""
        return DAO.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'Todo not found')
@api.param('id', 'The task identifier')
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @api.doc('get_todo')
    @api.marshal_with(tasks)
    def get(self, id):
        """Fetch a given resource"""
        return DAO.get(id)

    @api.doc('delete_todo')
    @api.response(204, 'Todo deleted')
    def delete(self, id):
        """Delete a task given its identifier"""
        print('whatefuck')
        DAO.delete(id)
        return '', 204

    @api.expect(tasks)
    @api.marshal_with(tasks)
    def put(self, id):
        """Update a task given its identifier"""
        return DAO.update(id, api.payload)
