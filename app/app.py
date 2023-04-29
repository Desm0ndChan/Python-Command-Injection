from flask import Flask,request
import os,subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return "Send a post request to /ping with the parameter 'host' to ping a host"

@app.route("/ping", methods=["GET","POST"])
def ping():
    if request.method == "POST":
        host = request.form.get("host")
        if not host:
            return "host name is required", 400
        command = "ping -c 1 "+ host
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output, 200
    else:
        return """
            <form method="post">
                <label for="host">Enter your host:</label>
                <input type="text" id="host" name="host">
                <button type="submit">Submit</button>
            </form>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8080)