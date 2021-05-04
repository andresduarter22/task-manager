from datetime import datetime



class Scheduler:
    """
    Class for scheduling and executing tasks, the main functionality of the system revolves around this class

    ...

    Attributes
    ----------
    task_queue : list
        stores all tasks to be executed
    update_interval: int
        interval at which the scheduler updates, in seconds.
    last_update_timestamp: float
        last time updated in timestamp format

    Methods
    -------
    add_schedule():
        adds a task to the queue
    edit_schedule():
        edits a scheduler entry
    delete_schedule()
        deletes a scheduler entry
    update()
        reviews which tasks are ready to be sent to the execution queue

    """
    def __init__(self, update_interval: int = 1):
        self.task_queue = []
        self.update_interval = update_interval
        self.last_update_timestamp = datetime.now().timestamp()

    def add_schedule(self, task):
        """
        adds a task to the queue

        :parameter task: Task object to be inserted into the scheduler
        """
        self.task_queue.append(task)

    def edit_schedule(self, id, new_exec):
        """
        adds a task to the queue

        :parameter id: Task id to find the corresponding task
        :parameter new_exec: ExecutionType object to define a new schedule

        :returns True if the task was updated, False if not.
        """
        found = False
        for task in self.task_queue:
            if task.id == id:
                found = True
                task.exec_type = new_exec
                break
        return found

    def delete_schedule(self, id):
        """
        deletes a task from the queue

        :parameter id: Task id to find the corresponding task

        :returns True if the task was deleted, False if not.
        """
        found = False
        temp_task = None
        for task in self.task_queue:
            if task.id == id:
                found = True
                temp_task = task
                break
        if found:
            self.task_queue.remove(temp_task)
        return found

    def check_for_update(self):
        """
        checks if it is time to update the scheduler
        """
        if self.update_interval >= (datetime.now().timestamp() - self.last_update_timestamp):
            self.last_update_timestamp = datetime.now().timestamp()
            self.update()




    def update(self):
        """
        moves tasks to the execution queue
        """
        for task in self.task_queue:
            if task.exec_type.exec_time <= datetime.now():
                # TODO move to execution queue
                pass
