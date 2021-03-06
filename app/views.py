from flask import render_template, flash, redirect, request, session, url_for, jsonify, make_response
from app import app, db, models



#----------------------------------------------    

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

#----------------------------------------------

@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>', methods=['GET'])
def return_descpt(section_slug,subsection_slug):
    if subsection_slug == "main":
        target = models.Section.query.filter(models.Section.slug == section_slug).first()
    else:
        target = models.Subsection.query.filter(models.Subsection.slug == subsection_slug).first()
    return jsonify({"description": target.description})

@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles/', methods=['GET'], defaults={'article_slug': None}) 
@app.route('/sections/<string:section_slug>/subsection/<string:subsection_slug>/articles/<string:article_slug>', methods=['GET']) 
def articles_within(section_slug,subsection_slug,article_slug):
    if article_slug != None and article_slug != "None":
        articles = models.Article.query.filter(models.Article.slug == article_slug).first().__dict__
        del articles['_sa_instance_state']
    elif subsection_slug == "main":
        section =  models.Section.query.filter(models.Section.slug == section_slug).first()
        articles = models.Article.query.filter(models.Article.section == section).all()
        articles = [u.__dict__ for u in articles]
        for i in articles:
            del i['_sa_instance_state']
    else:
        subsection =  models.Subsection.query.filter(models.Subsection.slug == subsection_slug).first()
        articles = models.Article.query.filter(models.Article.subsection == subsection).all()
        articles = [u.__dict__ for u in articles]
        for i in articles:
            del i['_sa_instance_state']
    return jsonify({"articles": articles})


#----------------------------------------------    
