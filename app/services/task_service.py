from app.exceptions import TaskNotFoundException
from app.repositories import task_repository


def create_task(task_data):

    new_task = {
        "id": len(task_repository.tasks) + 1,
        "title": task_data.title,
        "description": task_data.description,
        "completed": task_data.completed
    }

    return task_repository.create_task(new_task)


def get_tasks():

    return task_repository.get_tasks()


def get_task(task_id):

    task = task_repository.get_task(task_id)

    if task is None:
        raise TaskNotFoundException(task_id)

    return task


def update_task(task_id, task_data):

    task = task_repository.update_task(task_id, task_data)

    if task is None:
        raise TaskNotFoundException(task_id)

    return task


def patch_task(task_id, task_patch):

    update_data = task_patch.model_dump(exclude_unset=True)

    task = task_repository.patch_task(
        task_id,
        update_data
    )

    if task is None:
        raise TaskNotFoundException(task_id)

    return task


def delete_task(task_id):

    deleted = task_repository.delete_task(task_id)

    if not deleted:
        raise TaskNotFoundException(task_id)