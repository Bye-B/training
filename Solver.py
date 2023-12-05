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
    x_4 = LpVariable(name=f"x_4", cat="Float")
    x_5 = LpVariable(name=f"x_5", cat="Float")
    x_6 = LpVariable(name=f"x_6", cat="Float")
    x_7 = LpVariable(name=f"x_7", cat="Float")
    x_8 = LpVariable(name=f"x_8", cat="Float")
    #renamed former y_ constraints
    x_11 = LpVariable(name=f"x_11", cat="Binary")
    x_12 = LpVariable(name=f"x_12", cat="Binary")
    x_13 = LpVariable(name=f"x_13", cat="Binary")
    # profit function
    expression = 90*x_1 + 130*x_2 + 150*x_3 + 150*x_4 + 100*x_5 + 80*x_6 + 70*x_7 + 100*x_8 - x_11*facility_costs - x_12*facility_costs - x_13*fine

    # constraints
    constraint_1 = x_1 <= 1450
    constraint_2 = x_2 <= 550
    constraint_3 = x_3 <= 650
    constraint_4 = x_4 <= 150
    constraint_5 = x_5 <= 750
    constraint_6 = x_6 <= 1450
    constraint_7 = x_7 <= 1550
    constraint_8 = x_8 <= 1350

    #non-negative
    constraint_15 = x_1 >=0
    constraint_16 = x_2 >=0
    constraint_17 = x_3 >=0
    constraint_18 = x_4 >=0
    constraint_19 = x_5 >=0
    constraint_20 = x_6 >=0
    constraint_21 = x_7 >=0
    constraint_22 = x_8 >=0
    
    # at least 1000 Ammonia
    constraint_9 = x_1 >= 1000

    # available gas
    constraint_10 = 8*x_1 + 10*x_2 + 12*x_3 + 12*x_4 + 7*x_5 + 18*x_6 + 20*x_7 + 14*x_8 <= available_gas

    # production faciliy 1
    #               sum products          <= y1*M
    constraint_11 = x_1 + x_2 + x_3 + x_4 <= x_11* 100000

    # production faciliy 2
    #               sum products          <= y2*M
    constraint_12 = x_5 + x_6 + x_7 + x_8 <= x_12* 100000

    # constraints for fine
    constraint_13 = x_5 - m <= m*(1-x_13)
    constraint_14 = x_5-499 <= m*x_13

    # more or equal caustic soda (x_7) than ammonia (x_1) 
    constraint_23 = x_7 >= x_1


    # construct model
    model += expression
    model += (constraint_1, "constraint_1")
    model += (constraint_2, "constraint_2")
    model += (constraint_3, "constraint_3")
    model += (constraint_4, "constraint_4")
    model += (constraint_5, "constraint_5")
    model += (constraint_6, "constraint_6")
    model += (constraint_7, "constraint_7")
    model += (constraint_8, "constraint_8")
    model += (constraint_9, "constraint_9")
    model += (constraint_10, "constraint_10")
    model += (constraint_11, "constraint_11")
    model += (constraint_12, "constraint_12")
    model += (constraint_13, "constraint_13")
    model += (constraint_14, "constraint_14")
    model += (constraint_15, "constraint_15")
    model += (constraint_16, "constraint_16")
    model += (constraint_17, "constraint_17")
    model += (constraint_18, "constraint_18")
    model += (constraint_19, "constraint_19")
    model += (constraint_20, "constraint_20")
    model += (constraint_21, "constraint_21")
    model += (constraint_22, "constraint_22")
    model += (constraint_23, "constraint_23")

    model.solve()
    
    return model.variables()

def fine():
    
    step_size = 1
    fine = 10000

    while True:
        print(fine)
        
        fine += step_size
        variables = lp_solver(fine)
        optimal_temp = []

        for var in variables:
            optimal_temp.append(var.value())
        if fine > 38000:
            print("not found")
            break
        if optimal_temp[3] != 1.0:
            break
        

    print(f"fine: {fine}")
    
    for var in variables:
        print(f"{var.name}: {var.value()}")


if __name__ == "__main__":
    fine()