tasks = []


def create_task(task):

    tasks.append(task)

    return task


def get_tasks():

    return tasks


def get_task(task_id):

    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def update_task(task_id, task_data):

    task = get_task(task_id)

    if task is None:
        return None

    task["title"] = task_data.title
    task["description"] = task_data.description
    task["completed"] = task_data.completed

    return task


def patch_task(task_id, update_data):

    task = get_task(task_id)

    if task is None:
        return None

    for field, value in update_data.items():
        task[field] = value

    return task


def delete_task(task_id):

    task = get_task(task_id)

    if task is None:
        return False

    tasks.remove(task)

    return True