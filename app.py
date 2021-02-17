from flask import Flask
import os
app = Flask(__name__)            

@app.route("/")                  
def hello():
    myhost = os.uname()[0]+" - "+os.uname()[1]+" - "+os.uname()[2]+" - "+os.uname()[3]+" - "+os.uname()[4]                    
    return "I am running on server 🙂 : --> ["+myhost+"]"

if __name__ == "__main__":              
    app.run(host='0.0.0.0', debug=True) 