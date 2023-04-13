def solution(brown, yellow):
    total_tiles = brown + yellow
    for row in range(1, total_tiles+1):
        if total_tiles % row == 0:
            col = total_tiles // row
            if (row-2)*(col-2) == yellow:
                return [max(row, col), min(row, col)]
