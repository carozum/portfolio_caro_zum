from flask import (render_template, url_for, request)
from models import db, Pet, app


# **************** MAIN PAGE **************

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pets')
def pets():
    return render_template('p1-index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


# **************** PROJECT 1 - PET APP ****************


@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    print(request.form)
    print(request.form['name'])
    return render_template('p1-addpet.html')


@app.route('/single-pet')
def single_pet():
    return render_template('p1-singlepet.html')


# ******************  CODING BLOG ***************

# *************** B0.FLASK  **********************


@app.route('/set-environment')
def set_environment():
    return render_template('b1-set-environment.html')


@app.route('/flask-quickstart')
def flask_quickstart():
    return render_template('b2-quickstart.html')


@app.route('/add-templates')
def add_templates():
    return render_template('b3-add-templates.html')


@app.route('/static-files')
def static_files():
    return render_template('b4-static-files.html')


@app.route('/template-inheritance')
def template_inheritance():
    return render_template('b5-template-inheritance.html')


@app.route('/form')
def form():
    return render_template('b6-form.html')


# *************** b10. DATABASE SQLAlchemy *************************
@app.route('/flask-sqlalchemy')
def flask_sqlalchemy():
    return render_template('b10-flask-sqlalchemy.html')

# ****************b20. SQL ********************


@app.route('/basic-sql')
def basic_sql():
    return render_template('b20-basic-sql.html')

# *************** b30.PYTHON *************************


@app.route('/pep-8')
def pep_8():
    return render_template('b20-pep8-guidelines.html')


# ****************** b90. Other subjects

@app.route('/markdown')
def markdown():
    return render_template('b90-markdown.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
