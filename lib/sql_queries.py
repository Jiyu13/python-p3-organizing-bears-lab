select_all_female_bears_return_name_and_age = """
    select bears.name, bears.age from bears where sex = "F"
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    select bears.name from bears order by name asc
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    select bears.name, bears.age from bears where alive = 1 order by age asc
"""

select_oldest_bear_and_returns_name_and_age = """
    select bears.name, max(bears.age) from bears
"""
select_youngest_bear_and_returns_name_and_age = """
    select bears.name, min(bears.age) from bears
"""