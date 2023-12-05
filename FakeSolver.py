from pulp import *

def lp_solver(fine):
    facility_costs = 200000
    available_gas = 57277.5
    m = 800
    model = LpProblem(name= "lp_problem", sense= LpMaximize)
    # Float variables for each product
    x_1 = LpVariable(name=f"x_1", cat="Float")
    x_2 = LpVariable(name=f"x_2", cat="Float")
    x_3 = LpVariable(name=f"x_3", cat="Float")
    ...

    # constraints
    constraint_1 = x_1 <= 1450
    constraint_2 = x_2 <= 550
    constraint_3 = x_3 <= 650
    ...


    # construct model
    model += expression
    model += (constraint_1, "constraint_1")
    model += (constraint_2, "constraint_2")
    model += (constraint_3, "constraint_3")
    ...

    model.solve()
    
    return model.variables()

def fine():
    
    step_size = 1
    fine = 10000

    while True:
        fine += step_size
        variables = lp_solver(fine)
        optimal_temp = []

        for var in variables:
            optimal_temp.append(var.value())
        if optimal_temp[3] != 1.0:
            break
        

    print(f"fine: {fine}")  
    for var in variables:
        print(f"{var.name}: {var.value()}")
