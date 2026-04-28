"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)
    pass


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first, second, *rest = each_wagons_id
    
    # Move first two to end
    reordered = [*rest, first, second]
    
    # Find locomotive (1)
    index = reordered.index(1)
    
    # Insert missing wagons after locomotive
    return [*reordered[:index+1], *missing_wagons, *reordered[index+1:]]
    pass


def add_missing_stops(route, **kwargs):
    route["stops"] = [*kwargs.values()]
    return route
    pass


def extend_route_information(route, more_route_info):
    return {**route, **more_route_info}
    pass


def fix_wagon_depot(wagons_rows):
    # Unpack rows
    red, blue, orange = wagons_rows
    
    # Transpose using unpacking + zip
    return [list(row) for row in zip(red, blue, orange)]
    pass
