from flask import Flask, render_template
from core.vuln import TrivyInfo

app = Flask(__name__)
# app.config['SERVER_NAME'] = 'example.com'
# app.config['APPLICATION_ROOT'] = '.'
# app.config['PREFERRED_URL_SCHEME'] = 'https'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route("/")
def index():
    return render_template("home/home.html")


@app.route("/trivy_dashboard")
def trivy_dashboard():

    trivy_data = TrivyInfo().get_all_configAuditReport
    # trivy_data= [list(trivy_data[x]) for x in range(len(trivy_data)) ]
    with app.app_context():
        return render_template("trivy/trivy_dashboard.html", data=trivy_data, lenth = len(trivy_data))


if __name__ == "__main__":
    app.run(debug=True)

# trivy_dashboard()