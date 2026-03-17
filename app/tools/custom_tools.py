def simple_calculator(query: str):
    try:
        return str(eval(query))
    except:
        return "Error in calculation"