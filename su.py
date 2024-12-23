class SudokuConstraint:
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2

    def is_satisfied(self, assignment):
        # If either cell is not assigned, they cannot conflict
        if self.cell1 not in assignment or self.cell2 not in assignment:
            return True
        # Cells conflict if they have the same value
        return assignment[self.cell1] != assignment[self.cell2]

class CSP:
    def __init__(self, variables, domains):
        self.variables = variables  # Cells of the Sudoku grid
        self.domains = domains  # Possible values for each cell
        self.constraints = {var: [] for var in variables}

    def add_constraint(self, constraint):
        self.constraints[constraint.cell1].append(constraint)
        self.constraints[constraint.cell2].append(constraint)

    def is_consistent(self, var, assignment):
        for constraint in self.constraints[var]:
            if not constraint.is_satisfied(assignment):
                return False
        return True

    def solve(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        # Most Constrained Variable (MRV)
        unassigned = [v for v in self.variables if v not in assignment]
        current_var = min(unassigned, key=lambda var: len(self.domains[var]))

        for value in self.domains[current_var]:
            new_assignment = assignment.copy()
            new_assignment[current_var] = value

            if self.is_consistent(current_var, new_assignment):
                result = self.solve(new_assignment)
                if result:
                    return result
        return None

def print_sudoku(solution):
    board = [[0 for _ in range(9)] for _ in range(9)]
    for (row, col), value in solution.items():
        board[row][col] = value
    for row in board:
        print(" ".join(map(str, row)))

def sudoku_csp(puzzle):
    size = 9
    variables = [(row, col) for row in range(size) for col in range(size)]
    print(variables)
    domains = {var: [puzzle[var[0]][var[1]]] if puzzle[var[0]][var[1]] != 0 else list(range(1, 10)) for var in variables}
    print(domains)
    csp = CSP(variables, domains)

    # Add row constraints
    for row in range(size):
        for col1 in range(size):
            for col2 in range(col1 + 1, size):
                csp.add_constraint(SudokuConstraint((row, col1), (row, col2)))

    # Add column constraints
    for col in range(size):
        for row1 in range(size):
            for row2 in range(row1 + 1, size):
                csp.add_constraint(SudokuConstraint((row1, col), (row2, col)))

    # Add subgrid constraints
    for box_row in range(0, size, 3):
        for box_col in range(0, size, 3):
            cells = [(box_row + i, box_col + j) for i in range(3) for j in range(3)]
            for i in range(len(cells)):
                for j in range(i + 1, len(cells)):
                    csp.add_constraint(SudokuConstraint(cells[i], cells[j]))

    solution = csp.solve()
    if solution:
        print_sudoku(solution)
    else:
        print("No solution found")

# Example Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if __name__ == "__main__":
    sudoku_csp(puzzle)
