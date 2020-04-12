from constraint import *

GRID_SIZE = 9
DOMAIN = [i for i in range(1, GRID_SIZE+1)]
VARIABLES = ["C{}{}".format(row, column) for row in range(1,GRID_SIZE+1) for column in range(1,GRID_SIZE+1)]
SUM_CONSTRAINT = sum(DOMAIN)
# grid = [
#     3, 4, 1, '',
#     '', 2, '', '',
#     '', '', 2, '',
#     '', 1, 4, 3
# ]

# grid = [
#     '', '', 1, '',
#     4, '', '', '',
#     '', '', '', 2,
#     '', 3, '', ''
# ]

# grid = [
#     2, '', '', '',
#     '', '', 3, '',
#     '', 4, '', '',
#     '', '', '', 1
# ]

# 9x9
grid = [
    '','','',2 ,1 ,8 ,3 ,'',9,
    '',2 ,'','','',3 ,7 ,'','',
    '',8 ,3 ,5 ,'',7 ,'',6 ,2,
    1 ,5 ,8 ,'',6 ,9 ,'',7 ,'',
    2 ,'',4 ,'','',5 ,'','',8,
    '',6 ,7 ,'','',1 ,'','',4,
    '',3 ,9 ,1 ,'','','',2 ,6,
    '','',2 ,'',3 ,6 ,4 ,'',7,
    '','',6 ,'',8 ,2 ,'',3 ,1
]

problem = Problem()

for variable, value in zip(VARIABLES, grid):
    if value == '':
        problem.addVariable(variable, DOMAIN)
    else:
        problem.addVariable(variable, [value])

#Row constraints
for row in range(1,GRID_SIZE+1):
    row_cases = list()
    for column in range(1,GRID_SIZE+1):
        row_cases.append("C{}{}".format(row, column))
    
    problem.addConstraint(AllDifferentConstraint(), row_cases)
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), row_cases)


#Column constraints
for column in range(1,GRID_SIZE+1):
    column_cases = list()
    for row in range(1,GRID_SIZE+1):
        column_cases.append("C{}{}".format(row, column))
    
    problem.addConstraint(AllDifferentConstraint(), column_cases)
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), column_cases)


# Bloc constraints
if (GRID_SIZE == 4):
    # 4x4
    problem.addConstraint(AllDifferentConstraint(), ['C11', 'C12', 'C21', 'C22'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C11', 'C12', 'C21', 'C22'])

    problem.addConstraint(AllDifferentConstraint(), ['C13', 'C14', 'C23', 'C24'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C13', 'C14', 'C23', 'C24'])

    problem.addConstraint(AllDifferentConstraint(), ['C31', 'C32', 'C41', 'C42'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C31', 'C32', 'C41', 'C42'])

    problem.addConstraint(AllDifferentConstraint(), ['C33', 'C34', 'C43', 'C44'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C33', 'C34', 'C43', 'C44'])

elif (GRID_SIZE == 9):
    # 9x9
    problem.addConstraint(AllDifferentConstraint(), ['C11', 'C12', 'C13', 'C21', 'C22', 'C23', 'C31', 'C32', 'C33'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C11', 'C12', 'C13', 'C21', 'C22', 'C23', 'C31', 'C32', 'C33'])

    problem.addConstraint(AllDifferentConstraint(), ['C14', 'C15', 'C16', 'C24', 'C25', 'C26', 'C34', 'C35', 'C36'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C14', 'C15', 'C16', 'C24', 'C25', 'C26', 'C34', 'C35', 'C36'])

    problem.addConstraint(AllDifferentConstraint(), ['C17', 'C18', 'C19', 'C27', 'C28', 'C29', 'C37', 'C38', 'C39'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C17', 'C18', 'C19', 'C27', 'C28', 'C29', 'C37', 'C38', 'C39'])

    problem.addConstraint(AllDifferentConstraint(), ['C41', 'C42', 'C43', 'C51', 'C52', 'C53', 'C61', 'C62', 'C63'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C41', 'C42', 'C43', 'C51', 'C52', 'C53', 'C61', 'C62', 'C63'])

    problem.addConstraint(AllDifferentConstraint(), ['C44', 'C45', 'C46', 'C54', 'C55', 'C56', 'C64', 'C65', 'C66'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C44', 'C45', 'C46', 'C54', 'C55', 'C56', 'C64', 'C65', 'C66'])

    problem.addConstraint(AllDifferentConstraint(), ['C47', 'C48', 'C49', 'C57', 'C58', 'C59', 'C67', 'C68', 'C69'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C47', 'C48', 'C49', 'C57', 'C58', 'C59', 'C67', 'C68', 'C69'])

    problem.addConstraint(AllDifferentConstraint(), ['C71', 'C72', 'C73', 'C81', 'C82', 'C83', 'C91', 'C92', 'C93'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C71', 'C72', 'C73', 'C81', 'C82', 'C83', 'C91', 'C92', 'C93'])

    problem.addConstraint(AllDifferentConstraint(), ['C74', 'C75', 'C76', 'C84', 'C85', 'C86', 'C94', 'C95', 'C96'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C74', 'C75', 'C76', 'C84', 'C85', 'C86', 'C94', 'C95', 'C96'])

    problem.addConstraint(AllDifferentConstraint(), ['C77', 'C78', 'C79', 'C87', 'C88', 'C89', 'C97', 'C98', 'C99'])
    problem.addConstraint(ExactSumConstraint(SUM_CONSTRAINT), ['C77', 'C78', 'C79', 'C87', 'C88', 'C89', 'C97', 'C98', 'C99'])


solution = problem.getSolution()

#Print correctly the solution
solution_grid = list()
for row in range(1,GRID_SIZE+1):
    row_grid = list()
    for column in range(1,GRID_SIZE+1):
        row_grid.append(solution["C{}{}".format(row, column)])
    
    solution_grid.append(row_grid)

for row in solution_grid:
    print(row)