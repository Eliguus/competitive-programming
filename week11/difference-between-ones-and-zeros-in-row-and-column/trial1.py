rows_of_1=[]
        rows_of_0=[]
        col_of_1=[]
        col_of_0=[]
        len_of_col=len(grid[0])
        len_of_row=len(grid)
        
        
        for col in range(len_of_col):
            sum_of_col=0
            for row in range(len_of_row):
                sum_of_col+=grid[row][col]
            col_of_1.append(sum_of_col)
            col_of_0.append(len_of_col-sum_of_col)
        for row in range(len_of_row):
            sum_of_row=0
            for col in range(len_of_col):
                sum_of_row+=grid[row][col]
            rows_of_1.append(sum_of_row)
            rows_of_0.append(len_of_row-sum_of_row)
        diff=[]
        for row in range(len_of_row):
            diff.append([0]*len_of_col)
        for row in range(len_of_row):
            for col in range(len_of_col):
                diff[row][col]=col_of_1[col]+rows_of_1[row]-col_of_0[col]-rows_of_0[row]
        return diff
