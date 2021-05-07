
from datetime import datetime


class ExecutionType:
    """
    Class that defines the temporal properties for a Task's execution

    ...

    Attributes
    ----------
    exec_type : str
        whether the task is executed 'asap', 'single_schedule' or 'repeating_schedule'
    exec_time : Datetime
        the programmed execution time
    interval : int
        the interval in seconds at which the task is executed. (Only for 'repeating_schedule')

    Methods
    -------
    get_exec_time():
        Gets the next time of execution for a task.
    get_time_string():
        Returns the time, in string format, of when the task is going to be executed.
    set_time_from_string():
        sets the exec_time variable from a string input.
    """
    def __init__(self, exec_type: str, exec_time: str = None, interval: int = None):
        self.exec_type = exec_type
        if exec_time:
            self.exec_time = exec_time
        else:
            self.get_exec_time()
        self.interval = interval

    def get_exec_time(self):
        """
        gets the next exec_time
        """
        if self.exec_type == 'asap':
            self.exec_time = datetime.now()
        elif self.exec_type == 'repeating_schedule':
            now = datetime.now()
            if self.exec_time <= now:
                ts = int(self.exec_time.timestamp()) + self.interval
                self.exec_time = datetime.fromtimestamp(ts)
        else:
            pass

    def set_time_from_string(self, str: str):
        """
        sets the exec_time from a string

        :parameter str: str
            string formatted datetime

        """
        self.exec_time = datetime.strptime(str, '%d/%m/%Y %H:%M:%S')

    def get_time_string(self):
        """
        gets the exec_time in string format

        :returns exec_time in string format d/m/Y H:M:S.
        """
        return self.exec_time.strftime("%d/%m/%Y %H:%M:%S")
