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
    return render_template('dp.html')

@app.route("/convert")
def convert():
    global chatbot
    mes = request.args.get("query")
    fr = request.args.get("from")
    to = request.args.get("to")
    response = chatbot.get_chat_response(f"""convert this {fr} query into the {to} query :{mes}""", output="text")
    s= response["message"][::-1]
    st = s.find("""```""")
    en = s[st+3:].find("""```""")
    print(s[st+4:st+en+2][::-1])
    return f"<h1>{s[st+4:st+en+2][::-1]}</h1>"

if __name__=="__main__":
    app.run(debug=True)