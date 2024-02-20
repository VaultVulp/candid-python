# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskActionType(str, enum.Enum):
    CLOSE_TASK = "close_task"
    CLOSE_TASK_AND_REPROCESS = "close_task_and_reprocess"

    def visit(
        self, close_task: typing.Callable[[], T_Result], close_task_and_reprocess: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TaskActionType.CLOSE_TASK:
            return close_task()
        if self is TaskActionType.CLOSE_TASK_AND_REPROCESS:
            return close_task_and_reprocess()
