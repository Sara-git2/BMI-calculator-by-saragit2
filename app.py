from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None
    if request.method == "POST":
        height = float(request.form["height"])
        weight = float(request.form["weight"])
        height_m = height / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
