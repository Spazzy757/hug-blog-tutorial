import hug

@hug.get('/world')
def hello_world():
    """Returns Hello World"""
    return {"message": "Hello World"}

