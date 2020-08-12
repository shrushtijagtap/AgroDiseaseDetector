import csv
from flask import Flask, render_template, request

t = 't'

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/cotton")
def cotton():
    return render_template('cotton.html')


@app.route("/sugarcane")
def sugarcane():
    return render_template('sugarcane.html')


@app.route("/wheat")
def wheat():
    return render_template('wheat.html')


@app.route("/cotton_sym", methods=['POST', 'GET', 'DELETE'])
def cotton_sym():
    return render_template('cotton_sym.html')


@app.route("/sugarcane_sym", methods=['POST', 'GET', 'DELETE'])
def sugarcane_sym():
    return render_template('sugarcane_sym.html')


@app.route("/wheat_sym", methods=['POST', 'GET', 'DELETE'])
def wheat_sym():
    return render_template('wheat_sym.html')


@app.route("/sugarcane_final", methods=['POST', 'GET', 'DELETE'])
def sugarcane_final():
    if request.method == "POST":
        s1 = request.form.get("mycheckbox1")
        s2 = request.form.get("mycheckbox2")
        s3 = request.form.get("mycheckbox3")
        s4 = request.form.get("mycheckbox4")
        if (s1 == None and s2==None and s3==None and s4==None ):
            return render_template('sugarcane_sym.html')
        if s1 == None:
            s1 = 0
        if s2 == None:
            s2 = 0
        if s3 == None:
            s3 = 0
        if s4 == None:
            s4 = 0
    s = t + str(s1) + str(s2) + str(s3) + str(s4)
    with open('sugarcane_sym.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            if s == line[5]:  # if the username shall be on column 3 (-> index 2)
                disease = line[0]
                cure = line[6]
                symptoms = line[7]
                s_name = line[8]
                return render_template('sugarcane_final.html', disease=disease, cure=cure, symptoms=symptoms, s_name=s_name)
        err = 'Disease not found!!'
        return render_template('sugarcane_final1.html', err=err)


@app.route("/wheat_final", methods=['POST', 'GET', 'DELETE'])
def wheat_final():
    if request.method == "POST":
        s1 = request.form.get("mycheckbox1")
        s2 = request.form.get("mycheckbox2")
        s3 = request.form.get("mycheckbox3")
        s4 = request.form.get("mycheckbox4")
        s5 = request.form.get("mycheckbox5")
    if (s1 == None and s2 == None and s3 == None and s4 == None and s5 == None):
        return render_template('wheat_sym.html')
    if s1 == None:
        s1 = 0
    if s2 == None:
        s2 = 0
    if s3 == None:
        s3 = 0
    if s4 == None:
        s4 = 0
    if s5 == None:
        s5 = 0
    s = t + str(s1) + str(s2) + str(s3) + str(s4) + str(s5)
    with open('wheat_sym.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            if s == line[6]:  # if the username shall be on column 3 (-> index 2)
                disease = line[0]
                cure = line[7]
                symptoms = line[8]
                s_name = line[9]
                return render_template('wheat_final.html', disease=disease, cure=cure, symptoms=symptoms, s_name=s_name)
        err = 'Disease not found!!'
        return render_template('wheat_final1.html', err=err)


@app.route("/cotton_final", methods=['POST', 'GET', 'DELETE'])
def cotton_final():
    if request.method == "POST":
        s1 = request.form.get("mycheckbox1")
        s2 = request.form.get("mycheckbox2")
        s3 = request.form.get("mycheckbox3")
        s4 = request.form.get("mycheckbox4")
        s5 = request.form.get("mycheckbox5")
        s6 = request.form.get("mycheckbox6")
        s7 = request.form.get("mycheckbox7")
    if (s1 == None and s2 == None and s3 == None and s4 == None and s5 == None and s6== None and s7 == None):
        return render_template('cotton_sym.html')
    if s1 == None:
        s1 = 0
    if s2 == None:
        s2 = 0
    if s3 == None:
        s3 = 0
    if s4 == None:
        s4 = 0
    if s5 == None:
        s5 = 0
    if s6 == None:
        s6 = 0
    if s7 == None:
        s7 = 0
    s = t + str(s1) + str(s2) + str(s3) + str(s4) + str(s5) + str(s6) + str(s7)
    with open('cotton_sym.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for line in reader:
            if s == line[8]:  # if the username shall be on column 3 (-> index 2)
                disease = line[0]
                cure = line[9]
                symptoms = line[10]
                s_name = line[11]
                return render_template('cotton_final.html', disease=disease, cure=cure, symptoms=symptoms, s_name=s_name)
        err = 'Disease not found!!'
        return render_template('cotton_final1.html', err=err)


app.run(debug=True)