import http.server
import socketserver

# 定义服务器端口
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('./game/olh8ls3uenr16w8pr4ei3jlf20awopxu/ind ex.html')

if __name__ == '__main__':
    app.run()

#http://localhost:8000/