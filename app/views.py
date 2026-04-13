"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from email import errors

from app import app
from flask import render_template, request, jsonify, send_file, send_from_directory, url_for, allowed_file
from werkzeug.utils import secure_filename
from .forms import MovieForm
from .models import Movie
from . import db, app, csrf
from flask_wtf.csrf import generate_csrf
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

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

@app.route('/api/v1/movies', methods=['POST'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        if 'poster' not in request.files:
            return jsonify({"error": "No poster file provided."}), 400
        file = request.files['poster']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(['UPLOAD_FOLDER'], filename))
        else:
            return jsonify({"error": "Invalid file type. Only jpg, jpeg, png allowed."}), 400
        
        new_movie = Movie(
            title=form.title.data,
            description=form.description.data,
            poster=filename
        )
        db.session.add(new_movie)
        db.session.commit()

        return jsonify({"message": "Movie successfully added",  "title": new_movie.title, "poster": filename,"description": new_movie.description}), 201
    return jsonify({"errors": form_errors(form)}), 400

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404