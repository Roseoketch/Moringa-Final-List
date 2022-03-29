from flask import Flask, render_template, request, url_for, redirect, Response, flash
import io
from io import TextIOWrapper
import csv
# Converting Python Dictionary to
# XML and saving to a file
from dicttoxml import dicttoxml

from xml.dom.minidom import parseString
from ..models import Grade
from .. import db
from . import main


@main.route('/')
def index():
    grades = Grade.query.order_by('grades_id').all()
    return render_template('index.html', grades = grades)

@main.route('/create', methods=['GET','POST'])
def create():
    if request.method == "POST":
        id =  request.form['id']
        name =  request.form['name']
        cohort =  request.form['cohort']
        ip_scores =  request.form['ip_scores']
 
        grades_data = Grade(id, name, cohort, ip_scores)
        db.session.add(grades_data)
        db.session.commit()


        flash("New students has been successfully added")

        return redirect(url_for('main.index'))

@main.route('/update/<id>', methods=['GET','POST'])
def update(id):
    if request.method == "POST":
        grades_data = Grade.query.filter_by(id=id).first()

        grades_data.id =  request.form['id']
        grades_data.name =  request.form['name']
        grades_data.cohort =  request.form['cohort']
        grades_data.ip_scores =  request.form['ip_scores']

        db.session.commit()
        
        flash("Student Updated successfully")

        return redirect(url_for('main.index'))
 
@main.route('/delete/<id>', methods = ['GET', 'POST'])
def delete(id):
    grades_data = Grade.query.get(id)
    db.session.delete(grades_data)
    db.session.commit()

    flash("You have successfully deleted the student")

    return redirect(url_for('main.index'))

@main.route("/upload", methods=['POST'])
def uploadFiles():
    if request.method == 'POST':
        db.session.execute("DELETE FROM grades")
        db.session.commit()
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            grades = Grade(id=row[0], name=row[1], cohort=row[2], ip_scores=row[3])
            db.session.add()
            db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/csv_report')
def download_csv():
    result = db.session.execute("SELECT id,name,cohort,ip_scores FROM grades")

    output = io.StringIO()
    writer = csv.writer(output)
    
    for row in result:
        line = [row[0] ,row[1], row[2],row[3]]
        writer.writerow(line)

    output.seek(0)
    db.session.commit()
    return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=Final_List.csv"})

@main.route('/xml_report')
def xml_report():
    data = db.session.execute("SELECT id,name,cohort,ip_scores FROM grades")
finallistmoringa.herokuapp.com/

    # Variable name of Dictionary is data
    xml = dicttoxml(data)
    # Obtain decode string by decode()
    # function
    xml_decode = xml.decode()
    xmlfile = open("dict.xml", "w")
    xmlfile.write(xml_decode)
    xmlfile.close()
    return Response(xml_decode, mimetype="text/xml", headers={"Content-Disposition":"attachment;filename=dict.xml"})
