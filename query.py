"""

This file is the place to write solutions for the
practice part of skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes by just their
class name (and not model.ClassName).

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id="ram").all()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter(Model.name=="Corvette", Brand.brand_id=="che").all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != "for").all()



# -------------------------------------------------------------------
# Part 3: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    brands_by_year = Brand.query.filter_by(founded=year).all()
    for brand in brands_by_year:
        for model in brands.models:
            print model.name, brand.name, brand.headquarters


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brand_objs = Brand.query.all()
    for brand in brand_objs:
        print brand.name
        for model in brand.models:
            print model.name, model.year
        print "\n"


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_objs = []
    query = Brand.query.all()
    for brand_obj in query:
        if mystr in brand_obj.name:
            brand_objs.append(brand_obj)
    return brand_objs


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    model_objs = []
    query = Model.query.all()
    for model in query:
        if model.year >= start_year and model.year < end_year:
            model_objs.append(model)
    return model_objs

