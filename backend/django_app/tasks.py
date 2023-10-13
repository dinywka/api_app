from celery import shared_task

@shared_task
def add(x, y):
    print(f"Adding: {x} + {y} = {x + y}")
    return x + y

@shared_task
def multiply(x, y):
    print(f"Multiplying: {x} * {y} = {x * y}")
    return x * y

@shared_task
def concatenate(str1, str2):
    result = str1 + str2
    print(f"Concatenating: '{str1}' + '{str2}' = '{result}'")
    return result

