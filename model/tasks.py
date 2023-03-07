class TasksTODO(object):
    def __init__(self):
        self.counter = 0
        self.todos_tasks = []

    def get(self, id):
        for todo in self.todos_tasks:
            if todo['id'] == id:
                return todo
        # api.abort(404, "Todo {} doesn't exist".format(id))

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos_tasks.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos_tasks.remove(todo)


domain = 'yourdomainname.pythonanywhere.com'
DAO = TasksTODO()
DAO.create({'task': {'register': f'https://{domain}/login/register'}})
DAO.create({'task': {'login': f'https://{domain}/login/'}})
DAO.create({'task': {'open_home': f'https://{domain}/home'}})
DAO.create({'task': {'validate_profile_info': f'https://{domain}/home/profile'}})
