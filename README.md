Testing Devops Prompt

## To Run:
`python devops.py`

## To Test:
`python test.py`

To automatically watch the directory and run tests on file change, run:
`when-changed -r . -c "python test.py 2>&1 | xargs -0 notify-send -u critical 'Test Results'"
`
