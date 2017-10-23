# directive_example.py
import hug


# Header Directive
@hug.directive()
def foobar_header(**kwargs):
    header = {
        'Content-Type': 'application/json'
    }
    return header


# The Endpoint that uses the directive
@hug.get("/data")
def get_data(name, hug_foobar_header):
    return {"header": hug_foobar_header, "data": {"name": name}}
