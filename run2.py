from flask import Flask
import requests


app = Flask(__name__)

@app.route("/<string:birth>/<string:dob>/<string:num>")
def vata(birth, dob, num):
    link = 'https://mis.bhata.gov.bd/beneficiary/verifynidinfo'

    data = {
        "nid": birth,
	    "dob": dob
    }

    r = requests.post(link, json=data)
    print(r.status_code)
    if r.status_code == 200:
        return r.text
    else:
        return "something wrong"


if __name__ == '__main__':
    app.run(debug=True)
