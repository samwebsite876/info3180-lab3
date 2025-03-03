from app import app
from flask import render_template, request, redirect, url_for, flash
from app import mail
from app.forms import ContactForm
from flask_mail import Message


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()  

    if form.validate_on_submit():  
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        msg = Message(
            subject=subject,
            sender=(name, email), 
            recipients=["ssamuels327@gmail.com"],  
            body=f"From: {name} <{email}>\n\n{message}"
        )

        try:
            mail.send(msg)  
            flash("Your message has been sent successfully!", "success")
            return redirect(url_for("home"))  
        except Exception as e:
            flash(f"Error sending email: {str(e)}", "danger")

    return render_template("contact.html",form=form)


###
# The functions below should be applicable to all Flask apps.
###


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
