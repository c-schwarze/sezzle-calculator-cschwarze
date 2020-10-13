from flask import Flask, render_template, request, json


app = Flask(__name__)


# The index page. In this case, the only GET request
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# The index page. In this case, the only GET request
@app.route('/calculate', methods=['POST'])
def calculate():
    # get data once
    form_data = request.form
    first_num = form_data['first-num']
    operator = form_data['operator']
    second_num = form_data['second-num']

    # test data!
    # make sure they are numbers
    try:
        int(first_num)
        int(second_num)
    except (KeyError, ValueError):
        return 'Error! One of the values is not a number. Please try again.'

    # make sure the operator is as expected
    if operator not in ['+', '-', '*', '/']:
        return 'Error! Somehow the operator is not sending an expected value'
    # no division by 0 here!
    elif operator == '/' and second_num == '0':
        return 'Error! You are attempting to divide by 0.'

    # calculate total
    total = do_calculate(first_num, operator, second_num)
    log_calculation('{} {} {} = {}'.format(first_num, clean_operator(operator), second_num, total))
    return 'success'


# The index page. In this case, the only GET request
@app.route('/get_output', methods=['POST'])
def get_output():
    return read_last_10_entries()


# writes entries to a log file
def log_calculation(entry):
    f = open('calculations.txt', 'a+')
    f.write('{}\n'.format(entry))
    f.close()
    return True


# returns the 10 most recent entries, last to first
def read_last_10_entries():
    try:
        file = open('calculations.txt', 'r')
    except FileNotFoundError:
        return ''
    lines = file.readlines()

    # get the most recent 10 items from a list
    entries = reversed(lines[-10:])
    entries = strip_new_lines_from_list_elements(entries)
    return render_template('output.html', entries=entries)



# strip the new lines from list elements
def strip_new_lines_from_list_elements(list):
    new_list = []
    for item in list:
        new_list.append(item.strip())
    return new_list


# do calculations
def do_calculate(first_num, operator, second_num):
    total = eval("{}{}{}".format(first_num, operator, second_num))
    return total


# converts the operator back to the better visual.
def clean_operator(operator):
    if operator == '*':
        return 'x'
    elif operator == '/':
        return '÷'
    else:
        return operator
