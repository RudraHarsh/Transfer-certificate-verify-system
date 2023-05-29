from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)




#Home page
@app.route("/")
def main():
    return render_template("index.html")


#TC page
@app.route("/TC")
def TC():
    return render_template("TC.html")



@app.route("/rtc", methods=['GET', 'POST'])
def rtc():
    if request.method == 'POST':
        IDp = request.form.get('ID')

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="TC"
        )

        mycusr = mydb.cursor()
        mycusr.execute("SELECT ID, Name, Tc FROM TC WHERE IDp = %s", (IDp,))
        r = mycusr.fetchone()
        mycusr.close()
        mydb.close()

        return render_template("rtc.html", r=r)

    return render_template("rtc.html")

if __name__ == '__main__':
    app.run(debug=True)
