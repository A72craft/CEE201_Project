import pulp

# Step 1: Uncomment the code for Step 1 and then modify it
my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)
x1 =  pulp.LpVariable('x1', lowBound=0, cat='Continuous')
x2 =  pulp.LpVariable('x2', lowBound=0, cat='Continuous')
my_lp_problem +=  0.8 * x1 -2.2* x2, "Z"
my_lp_problem +=  -6*x1 + 3*x2 <=12
my_lp_problem += 4*x1 - 2*x2 <=24
my_lp_problem += 1 * x1 -1*x2 <=5
my_lp_problem += x2<=6


# Step 2: When you finished the "Step 1", modify the code bellow, define the required variables.
my_lp_problem.solve()
print(" x1* = {}".format(x1.varValue))
print(" x2* = {}".format(x2.varValue))
print(" Z* = ",pulp.value(my_lp_problem.objective))
x1_Optimal_Value = x1.varValue
x2_Optimal_Value = x2.varValue
z_Optimal_Value = pulp.value(my_lp_problem.objective)