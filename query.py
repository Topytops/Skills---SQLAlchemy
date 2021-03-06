"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""


from model import *


init_app()

# -------------------------------------------------------------------
# Start here.


# # Part 2: Write queries

# # Get the brand with the **id** of 8.
# a = Brand.query.filter_by(id=8).one()

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# b = Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# # Get all models that are older than 1960.
# c  = Model.query.filter(Model.year > 1960).all()

# # Get all brands that were founded after 1920.
# d = Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor".
# e = Model.query.filter(Model.name.like('Cor%')).all()

# # Get all brands with that were founded in 1903 and that are not yet discontinued.
# f = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# # Get all brands with that are either discontinued or founded before 1950.
# g = Brand.query.filter( db.or_(Brand.discontinued != None, Brand.founded < 1950)).all()

# # Get any model whose brand_name is not Chevrolet.
# h = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# # Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models_brands_join = db.session.query(Model, Brand).filter(Model.year == year).join(Brand)

    for model, brand in models_brands_join:
        print model.name, model.brand_name, brand.headquarters
    	
# get_model_info(1958)

   
def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # brand_names = db.session.query(Brand, Model).join(Model).all()

    # for brand, model in brand_names:
    #     print brand.name + "\n" "  " + model.name

    summary = db.session.query(Brand, Model).join(Model).order_by(Brand.name).all()

    print "BRAND" + "\t" + "MODEL"

    for brand, model in summary:ß
        print brand.name + "    " + model.name


get_brands_summary()
# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
