from . import menu_items, orders, order_details, recipes, resources, customers, promotions, food_categories, payment_information, feedback

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    food_categories.Base.metadata.create_all(engine)
    payment_information.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
