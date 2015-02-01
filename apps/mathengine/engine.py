SUPPORTED_OPERATIONS = {
    'add': lambda a,b: a+b,
    'subtract': lambda a,b: a-b,
    'multiply': lambda a,b: a*b,
    'divide': lambda a,b: a/b,
}

def handleRequest(req):
    operation = req['operation']
    print "\n\n\n\n\n"
    print type(operation)
    values = req['values']

    assert isinstance(values, list)
    operation_to_execute = SUPPORTED_OPERATIONS[operation]
    result = reduce(operation_to_execute, values)
    return {'result': result}



