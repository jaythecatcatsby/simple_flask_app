from flask import render_template, redirect, url_for
from app import app, db
from app.models import videos


# category base queries
results_bigtits = videos.query.filter(db.or_(
        videos.tags.like('%big%'),
        videos.tags.like('%fake%'),
        videos.tags.like('%huge%')
        )).filter(db.or_(
        videos.tags.like('%boob%'),
        videos.tags.like('%breast%'),
        videos.tags.like('%tits%'))
        ).filter(db.not_(videos.tags.like('%small%'))).filter(db.not_(videos.tags.like('%natural%'))
        ).order_by(videos.Id.desc())

results_teen = videos.query.filter(db.or_(
        videos.tags.like('%teen%'),
        videos.tags.like('%petite%'),
        videos.tags.like('%young%')
        )).order_by(videos.Id.desc())

results_siblings = videos.query.filter(db.or_(
        videos.tags.like('%sis%'),
        videos.tags.like('%bro%'),
        videos.tags.like('%sibling%')
        )).order_by(videos.Id.desc())

results_pov = videos.query.filter(db.or_(
        videos.tags.like('%pov%'),
        videos.tags.like('%point%')
        )).order_by(videos.Id.desc())

results_mom = videos.query.filter(db.or_(
        videos.tags.like('%mom%'),
        videos.tags.like('%mother%'),
        videos.tags.like('%milf%'),
        videos.tags.like('%son%'),
        videos.tags.like('%aunt%'),
        videos.tags.like('%wife%'),
        videos.tags.like('%cougar%')
        )).order_by(videos.Id.desc())

results_masturbation = videos.query.filter(db.or_(
        videos.tags.like('%masturb%'),
        videos.tags.like('%jerk%')
        )).order_by(videos.Id.desc())

results_daughter = videos.query.filter(db.or_(
        videos.tags.like('%dad%'),
        videos.tags.like('%daughter%'),
        videos.tags.like('%filf%'),
        videos.tags.like('%father%')
        )).order_by(videos.Id.desc())

results_massage = videos.query.filter(db.or_(
        videos.tags.like('%massage%'),
        videos.tags.like('%nuru%')
        )).order_by(videos.Id.desc())

results_group = videos.query.filter(db.or_(
        videos.tags.like('%group%'),
        videos.tags.like('%some%'),
        videos.tags.like('%way%'),
        videos.tags.like('%orgy%')
        )).order_by(videos.Id.desc())

results_momsteachsex = videos.query.filter(db.or_(
        videos.tags.like('%teach%')
        )).order_by(videos.Id.desc())

results_caught = videos.query.filter(db.or_(
        videos.tags.like('%caught%')
        )).order_by(videos.Id.desc())

results_lesbian = videos.query.filter(db.or_(
        videos.tags.like('%lesbian%'),
        videos.tags.like('%on%').like('%girl%')
        )).order_by(videos.Id.desc())

results_all = videos.query.order_by(videos.Id.desc())
#popular needs changing for popularity variable
results_popular = videos.query.order_by(videos.Id.desc())


#pagination for category pages
page_bigtits = results_bigtits.paginate(1, 100, False)
page_teen = results_teen.paginate(1, 100, False)
page_siblings = results_siblings.paginate(1, 100, False)
page_pov = results_pov.paginate(1, 100, False)
page_mom = results_mom.paginate(1, 100, False)
page_masturbation = results_masturbation.paginate(1, 100, False)
page_daughter = results_daughter.paginate(1, 100, False)
page_massage = results_massage.paginate(1, 100, False)
page_group = results_group.paginate(1, 100, False)
page_momsteachsex = results_momsteachsex.paginate(1, 100, False)
page_caught = results_caught.paginate(1, 100, False)
page_lesbian = results_lesbian.paginate(1, 100, False)
page_all = results_all.paginate(1, 100, False)
page_popular = results_popular.paginate(1, 100, False)

# home category thumbnails
import random


t1 = results_bigtits.offset(int(9*random.random())).first().thumbnail
t2 = results_teen.offset(int(9*random.random())).first().thumbnail
t3 = results_siblings.offset(int(9*random.random())).first().thumbnail
t4 = results_pov.offset(int(9*random.random())).first().thumbnail
t5 = results_mom.offset(int(9*random.random())).first().thumbnail
t6 = results_masturbation.offset(int(4*random.random())).first().thumbnail
t7 = results_daughter.offset(int(4*random.random())).first().thumbnail
t8 = results_massage.offset(int(3*random.random())).first().thumbnail
t9 = results_group.offset(int(4*random.random())).first().thumbnail
t10 = results_momsteachsex.offset(int(4*random.random())).first().thumbnail
t11 = results_caught.offset(int(4*random.random())).first().thumbnail
t12 = results_lesbian.offset(int(3*random.random())).first().thumbnail

class homecat:  
        def __init__(self, thumb, path, title):  
            self.thumb = thumb  
            self.path = path
            self.title = title
cat1 = homecat(t1, '/bigtits', 'Big Tits') 
cat2 = homecat(t2, '/teen', 'Teen')
cat3 = homecat(t3, '/siblings', 'Brother-Sister')
cat4 = homecat(t4, '/pov', 'POV')
cat5 = homecat(t5, '/mom', 'Mom') 
cat6 = homecat(t6, '/masturbation', 'Masturbation')
cat7 = homecat(t7, '/daughter', 'Daughter')
cat8 = homecat(t8, '/massage', 'Massage')
cat9 = homecat(t9, '/group', 'Group') 
cat10 = homecat(t10, '/momsteachsex', 'Moms Teach Sex')
cat11 = homecat(t11, '/caught', 'Caught')
cat12 = homecat(t12, '/lesbian', 'Lesbian')

cats = [cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8, cat9, cat10, cat11, cat12]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', cats=cats)

@app.route('/rand')
def rand():
    import random
    x = int(12*random.random())
    catpath = cats[x].path
    return redirect(catpath)

@app.route('/popular')
def popular():
    posts = page_popular
    return render_template('category.html', category='Popular Posts',posts=posts.items) 

@app.route('/all')
def all():
    posts = page_all
    return render_template('category.html', category='all',posts=posts.items) 

@app.route('/bigtits')
def bigtits():
    posts = page_bigtits
    return render_template('category.html', category='Big Tits',posts=posts.items) 

@app.route('/teen')
def teen():
    posts = page_teen
    return render_template('category.html', category='Teen',posts=posts.items) 

@app.route('/siblings')
def siblings():
    posts = page_siblings
    return render_template('category.html', category='Brother-Sister',posts=posts.items) 

@app.route('/pov')
def pov():
    posts = page_pov
    return render_template('category.html', category='pov',posts=posts.items) 

@app.route('/mom')
def mom():
    posts = page_mom
    return render_template('category.html', category='Mom',posts=posts.items) 

@app.route('/masturbation')
def masturbation():
    posts = page_masturbation
    return render_template('category.html', category='Masturbation',posts=posts.items) 

@app.route('/daughter')
def daughter():
    posts = page_daughter
    return render_template('category.html', category='Daughter',posts=posts.items) 

@app.route('/massage')
def massage():
    posts = page_massage
    return render_template('category.html', category='Massage',posts=posts.items) 

@app.route('/group')
def group():
    posts = page_group
    return render_template('category.html', category='Group',posts=posts.items) 

@app.route('/momsteachsex')
def momsteachsex():
    posts = page_momsteachsex
    return render_template('category.html', category='Moms Teach Sex',posts=posts.items) 

@app.route('/caught')
def caught():
    posts = page_caught
    return render_template('category.html', category='Caught',posts=posts.items) 

@app.route('/lesbian')
def lesbian():
    posts = page_lesbian
    return render_template('category.html', category='Big Tits',posts=posts.items) 

