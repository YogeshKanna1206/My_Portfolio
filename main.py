from flask import Flask,render_template,request
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

password = os.environ.get("EMAIL_PASS")
@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        try:
            print("Trying to login to SMTP...")
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("yogesh.test1206@gmail.com", password)
            rec_name = request.form["r_name"]
            rec_mail = request.form["r_mail"]
            message = request.form["message"]
            email_body = f"""
            New contact message received:
                
            Receiver name : {rec_name}
            Receiver mail : {rec_mail}
            message:
            {message}
            """
            print("successfull")
            s.sendmail("yogesh.test1206@gmail.com", "yogeshkanna1206@gmail.com", email_body)
            s.quit()
            print("successfull")
        except Exception as e:
            print("Error sending email:", e)
        return render_template("port.html")
    return render_template("port.html")
if __name__ == "__main__" :
    app.run()