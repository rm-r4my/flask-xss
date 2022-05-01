from flask import Flask, send_file
from flask_cors import CORS

win = Flask(__name__)
CORS(app)




@app.route('/xss.js', methods=['GET'])
def xss():
  return send_file('./xss.js', download_name='xss.js')



if __name__ == '__main__':
  win.run(host='127.0.0.1', port=443, ssl_context=('cert.pem', 'key.pem'))
