from constraint import *

grid = [
    3, 4, 1, '',
    '', 2, '', '',
    '', '', 2, '',
    '', 1, 4, 3
]

problem = Problem()

domain = [1, 2, 3, 4]
variables = ["C{}{}".format(row, column) for row in range(1,5) for column in range(1,5)]

for variable, value in zip(variables, grid):
    if value == '':
        problem.addVariable(variable, domain)
    else:
        problem.addVariable(variable, [value])

#Row constraints
for row in range(1,5):
    row_cases = list()
    for column in range(1,5):
        row_cases.append("C{}{}".format(row, column))
    
    problem.addConstraint(AllDifferentConstraint(), row_cases)
    problem.addConstraint(ExactSumConstraint(10), row_cases)


#Column constraints
for column in range(1,5):
    column_cases = list()
    for row in range(1,5):
        column_cases.append("C{}{}".format(row, column))
    
    problem.addConstraint(AllDifferentConstraint(), column_cases)
    problem.addConstraint(ExactSumConstraint(10), column_cases)


#Bloc constraints
problem.addConstraint(AllDifferentConstraint(), ['C11', 'C12', 'C21', 'C22'])
problem.addConstraint(ExactSumConstraint(10), ['C11', 'C12', 'C21', 'C22'])

problem.addConstraint(AllDifferentConstraint(), ['C13', 'C14', 'C23', 'C24'])
problem.addConstraint(ExactSumConstraint(10), ['C13', 'C14', 'C23', 'C24'])

problem.addConstraint(AllDifferentConstraint(), ['C31', 'C32', 'C41', 'C42'])
problem.addConstraint(ExactSumConstraint(10), ['C31', 'C32', 'C41', 'C42'])

problem.addConstraint(AllDifferentConstraint(), ['C33', 'C34', 'C43', 'C44'])
problem.addConstraint(ExactSumConstraint(10), ['C33', 'C34', 'C43', 'C44'])


solution = problem.getSolution()


#Print correctly the solution
solution_grid = list()
for row in range(1,5):
    row_grid = list()
    for column in range(1,5):
        row_grid.append(solution["C{}{}".format(row, column)])
    
    solution_grid.append(row_grid)

for row in solution_grid:
    print(row)