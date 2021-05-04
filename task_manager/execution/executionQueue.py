class ExecutionQueue:
    """
    Class for handling final task queueing and execution

    ...

    Attributes
    ----------
    task_is_exec : bool
        stores if a task is under execution
    task_queue: list
        stores the tasks for execution
    actual_task: object
        the Task being performed now

    Methods
    -------
    get_next():
        gets the next task for execution
    execute():
        executes the actual task.

    """
    def __init__(self):
        self.task_queue = []
        self.actual_task = None
        self.task_is_exec = False

    def get_next(self):
        """
        gets the next task for execution

        TODO
        """

    def execute(self):
        """
        executes the actual task.

        TODO
        """
        found = False
        for task in self.task_queue:
            if task.id == id:
                found = True
                task.exec_type = new_exec
                break
        return found
