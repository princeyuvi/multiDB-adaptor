from flask import Flask,request,render_template
from revChatGPT.revChatGPT import Chatbot

config={
        "email":"kuvvamh@gmail.com",
        "password":"#arshitH"
}
chatbot = Chatbot(config,conversation_id=None)

app = Flask(__name__)
chatbot
@app.route("/")
def home():
    return render_template('index2.html')

@app.route("/convert")
def convert():
    global chatbot
    mes = request.args.get("query")
    response = chatbot.get_chat_response(f"""{mes} \n is this a hive databse query? or postgres? or mongodb?  just reply with database name and nothing else.""", output="text")
    s= response["message"]
    s= s.split(".")[0]
    print(s)
    if 'Hive' in s:
        return """<h1>the query is in hive</h1>"""
    elif 'Postgres' in s:
        return """<h1>the query is in Postgres/h1>"""
    elif 'MongoDB' in s:
        return """<h1>the query is in MongoDB</h1>"""
    else:
        return """Nothing"""

if __name__=="__main__":
    app.run(debug=True)