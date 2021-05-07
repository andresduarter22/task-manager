class ExecutionQueue:
    """
    Class for handling final task queueing and execution

    Tasks that are received from the scheduler are executed in a queue, following their priority

    ...

    Attributes
    ----------
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

    def get_next(self):
        """
        gets the next task for execution, following the priority of tasks queued for execution
        the next task gets removed from the queue list and stored in the actual_task variable.
        """
        count, idx = 0, None
        highest_priority = 0
        for task in self.task_queue:
            if task.priority > highest_priority:
                highest_priority = task.priority
                idx = count
            count += 1

        if idx:
            self.actual_task = self.task_queue.pop(idx)

        return False if idx is None else True

    def execute(self, prev_result=None):
        """
        executes the actual task.

        :returns res: list of task execution results
        """
        if prev_result:
            res = prev_result.append(self.actual_task.execute())
        else:
            res = [].append(self.actual_task.execute())

        incoming_task = self.get_next()
        if incoming_task:
            self.execute(res)
        return res

    def add_to_queue(self):
        """
        adds a task to the queue
        TODO
        :return:
        """
