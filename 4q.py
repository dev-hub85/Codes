class QueenConstraint:
    def __init__(self, queen1, queen2):
        self.queen1 = queen1
        self.queen2 = queen2

    def is_satisfied(self, assignment):
        # If either queen is not in the assignment, they cannot conflict
        if self.queen1 not in assignment or self.queen2 not in assignment:
            return True
        # Row positions for both queens
        row1, row2 = assignment[self.queen1], assignment[self.queen2]
        col1, col2 = self.queen1, self.queen2
        # Check if in the same row or same diagonal
        return row1 != row2 and abs(row1 - row2) != abs(col1 - col2)


class CSP:
    def __init__(self, variables, domains):
        self.variables = variables  # Columns of the chessboard
        self.domains = domains  # Possible rows for each column
        self.constraints = {var: [] for var in variables}

    def add_constraint(self, constraint):
        self.constraints[constraint.queen1].append(constraint)
        self.constraints[constraint.queen2].append(constraint)

    def is_consistent(self, var, assignment):
        for constraint in self.constraints[var]:
            if not constraint.is_satisfied(assignment):
                return False
        return True

    def solve(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        # Select the next unassigned variable
        unassigned = [v for v in self.variables if v not in assignment]
        current_var = unassigned[0]

        for value in self.domains[current_var]:
            new_assignment = assignment.copy()
            new_assignment[current_var] = value

            if self.is_consistent(current_var, new_assignment):
                result = self.solve(new_assignment)
                if result:
                    return result
        return None


def print_solution(solution, size):
    board = [["." for _ in range(size)] for _ in range(size)]
    for col, row in solution.items():
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))


def four_queens_csp():
    size = 8
    variables = list(range(size))  # Columns of the chessboard
    print(variables)
    domains = {var: list(range(size)) for var in variables}  # Rows for each column
    print(domains)

    csp = CSP(variables, domains)

    # Add constraints to ensure no two queens can attack each other
    for i in range(size):
        for j in range(i + 1, size):
            csp.add_constraint(QueenConstraint(i, j))

    solution = csp.solve()
    if solution:
        print_solution(solution, size)
    else:
        print("No solution found")


four_queens_csp()
