from flask import Flask, render_template, request, json


app = Flask(__name__)


# The index page. In this case, the only GET request
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    form_data = request.form
    full_equation = form_data['full-equation']

    if full_equation == '':
        return 'Error! You have submitted an empty equation'
    split_equation = full_equation.split(' ')
    numbers = split_equation[::2]
    operators = split_equation[1::2]

    if len(numbers) != len(operators) + 1:
        return 'Error! You have ended the equation with an operator. Please finish with a number'

    # test data!
    # make sure they are numbers
    try:
        for num in numbers:
            int(num)
    except (KeyError, ValueError):
        return 'Error! One of the values is not a number. Please try again.'

    # make sure the operator is as expected
    for operator in operators:
        if operator not in ['+', '-', '*', '/']:
            return 'Error! Somehow the operators are not correct'

    # calculate total
    total = get_total(numbers, operators)

    # alert for division by 0
    try:
        if not total.isnumeric():
            return total
    except AttributeError:
        # numbers don't have the method isnumeric(), so we want to pass
        pass

    log_calculation('{} = {}'.format(full_equation, total))
    return 'success'


# returns the output for all users on the index page
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
def get_total(numbers, operators):
    # do operators in this order
    for operator_loop in ['*', '/', '+', '-']:
        index = 0
        while operator_loop in operators[:]:
            if operator_loop == operators[index]:
                # no division by 0 here!
                if operator_loop == '/' and numbers[index+1] == '0':
                    return 'Error! You are attempting to divide by 0.'
                # calculate new number
                new_num = eval("{}{}{}".format(numbers[index], operator_loop, numbers[index+1]))
                # condense lists, as we combined the numbers already
                del operators[index]
                del numbers[index+1]
                del numbers[index]
                # add new number to the list.
                numbers.insert(index,new_num)
            else:
                # only push index if no calculation was made, since you might do an operation on the same index
                index += 1

    return numbers[0]
