Testing Devops Prompt

## Installation
`$ sudo apt-get install sqlite3`
`$ pip install -r requirements/requirements.txt`

## To Run:
`python devops.py`

## To Test:
`python test.py`

To automatically watch the directory and run tests on file change, run:
`when-changed -r . -c "python test.py 2>&1 | xargs -0 notify-send -u critical 'Test Results'"`

## To Make a request:
` bash make_request.sh '{ "operation": "add", "values": [1, 4] }'`
Note that the quotes are very particular, if the json is not encoded w/ " the json module will not decode it.
