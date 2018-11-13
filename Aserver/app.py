from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route('/aaron', methods=['POST'])
def A_rasp(aaron_num, aaron_str):
    try:
        name = {'word':aaron_str, 'code_num': aaron_num}
        res = requests.post('URL', data = aaron_num)
    except:
        HaveError = {'word':'Error!!!!', 'code_num': 555}
        return render_template(우영.html, names=HaveError)

@app.route('/checking',methods=['POST'])
def Check(back):
    return render_template(우영.html, names=back)

if __name__ ==  '__main__':
    app.run()
