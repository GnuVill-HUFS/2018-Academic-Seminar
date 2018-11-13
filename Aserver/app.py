from flask import Flask,render_template,request

app = Flask(__name__)

class CodeError(Exception):
    def __init__(self, a):
        self.a = int(555)

    value = voice_assist(STATUS)

    if value != 303 or 309 or 306 or 321:
        raise CodeError(555)

#예외처리
def if_it_doesnt_work(direction_code):
    try:
        if direction_code == 303 or 309 or 306 or 321:
            return direction_code
    except: CodeError


code_list=[]

@app.route('/direction/<int: direction_code> ',methods=['GET, POST'])
def A_rasp(direction_code):
    if request.method =='POST':
        code_list[0] = direction_code
        return code_list, render_template(우영.html, name=direction_code)

def B_rasp():
    if request.method =='POST':
        a = int (code_list[0])
        return a
