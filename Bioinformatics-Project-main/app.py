from flask import Flask, render_template, Request, Response, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template('front.html', my_function = show_sequence)





#@app.route('/', methods = ['POST'])
def show_sequence(array_seq):
    infile = request.form['sequence']
    tb=[]
    for line in infile:
        if line[0]==">":
            s=line.split("|lcl|")
        else:
            if s[3]=='non-hemolytic' or s[3]=='non-hemolytic\n':
                tb.append([line[:-1],0])
            else:
                tb.append([line[:-1],1])
    print(tb)
    
        
