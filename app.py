from flask import Flask, render_template


app = Flask(__name__)


# The index page. In this case, the only GET request
@app.route('/', methods=['GET'])
def index():
    log_calculation("3+4=10")
    entries = read_last_10_entries()
    return render_template('index.html', **locals())


# writes entries to a log file
def log_calculation(entry):
    f = open("calculations.txt", "a+")
    f.write("{}\n".format(entry))
    f.close()
    f.close()
    return True


# returns the 10 most recent entries, last to first
def read_last_10_entries():
    file = open("calculations.txt", "r")
    lines = file.readlines()

    # get the most recent 10 items from a list
    entries = lines[-10:]
    entries = strip_new_lines_from_list_elements(entries)
    return entries


def strip_new_lines_from_list_elements(list):
    new_list = []
    for item in list:
        new_list.append(item.strip())
    return new_list
