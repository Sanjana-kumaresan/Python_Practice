def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    
    for item in items_to_add:
        current_cart.setdefault(item, 0)  # ensures key exists
        current_cart[item] += 1           # increment quantity
    
    return current_cart
def read_notes(notes):
    """Create user cart from an iterable notes entry."""
    
    cart = {}
    
    for item in notes:
        cart[item] = 1   # every item gets quantity 1
    
    return cart
def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary."""
    
    for recipe, ingredients in recipe_updates:
        ideas[recipe] = ingredients   # replace or add
    
    return ideas
def sort_entries(cart):
    """Sort a users shopping cart in alphabetical order."""
    
    return dict(sorted(cart.items()))

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information."""
    
    fulfillment = {}
    
    for item in sorted(cart.keys(), reverse=True):
        quantity = cart[item]
        aisle, refrigeration = aisle_mapping[item]
        
        fulfillment[item] = [quantity, aisle, refrigeration]
    
    return fulfillment
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order."""
    
    for item in fulfillment_cart:
        ordered_qty = fulfillment_cart[item][0]
        stock_qty = store_inventory[item][0]
        
        new_stock = stock_qty - ordered_qty
        
        if new_stock == 0:
            store_inventory[item][0] = 'Out of Stock'
        else:
            store_inventory[item][0] = new_stock
    
    return store_inventory