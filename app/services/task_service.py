from app.exceptions import TaskNotFoundException

def create_task(tasks, task_data):

    new_task = {
        "id": len(tasks) + 1,
        "title": task_data.title,
        "description": task_data.description,
        "completed": task_data.completed
    }

    tasks.append(new_task)

    return new_task

def get_tasks(tasks):
    return tasks

def get_task(tasks, task_id):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise TaskNotFoundException(task_id)

def update_task(tasks, task_id, task_update):

    for task in tasks:
        if task["id"] == task_id:

            task["title"] = task_update.title
            task["description"] = task_update.description
            task["completed"] = task_update.completed

            return task

    raise TaskNotFoundException(task_id)

def patch_task(tasks, task_id, task_patch):

    for task in tasks:
        if task["id"] == task_id:

            update_data = task_patch.model_dump(exclude_unset=True)

            for field, value in update_data.items():
                task[field] = value

            return task

    raise TaskNotFoundException(task_id)

def delete_task(tasks, task_id):

    for task in tasks:
        if task["id"] == task_id:

            tasks.remove(task)
            return

    raise TaskNotFoundException(task_id)