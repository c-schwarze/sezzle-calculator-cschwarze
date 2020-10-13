from flask import Flask, render_template, request


app = Flask(__name__)


# The index page. In this case, the only GET request
@app.route('/', methods=['GET'])
def index():
    log_calculation('3+4=10')
    entries = read_last_10_entries()
    return render_template('index.html', **locals())


# The index page. In this case, the only GET request
@app.route('/calculate', methods=['POST'])
def calculate():
    # get data
    form_data = request.form
    first_num = form_data['first-num']
    operator = form_data['operator']
    second_num = form_data['second-num']

    total = do_calculate(first_num, operator, second_num)
    log_calculation('{} {} {} = {}'.format(first_num, operator, second_num, total))
    return 'success'


# writes entries to a log file
def log_calculation(entry):
    f = open('calculations.txt', 'a+')
    f.write('{}\n'.format(entry))
    f.close()
    return True


# returns the 10 most recent entries, last to first
def read_last_10_entries():
    file = open('calculations.txt', 'r')
    lines = file.readlines()

    # get the most recent 10 items from a list
    entries = lines[-10:]
    entries = strip_new_lines_from_list_elements(entries)
    return entries


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
