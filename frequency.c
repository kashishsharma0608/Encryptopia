#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main()
{
    int rows, columns;
    printf("Enter the row and columns:");
    scanf("%d %d", &rows, &columns);
    char *string[rows][columns];
    for (int index = 0; index < rows; index++)
    {
        for (int index_2 = 0; index_2 < columns; index_2++)
        {
            string[index][index_2] = (char *)malloc(100 * sizeof(char));
        }
    }
    for (int index = 0; index < rows; index++)
    {
        for (int col_index = 0; col_index < columns; col_index++)
        {
            scanf("%s", string[index][col_index]);
        }
    }

    int visited[50][100] ;
    for(int i=0;i<50;i++){
        for(int j=0;j<100;j++){
            visited[i][j]=0;
        }
    }
    for (int row_index = 0; row_index < rows; row_index++)
    {

        {
            for (int column_index = 0; column_index < columns; column_index++)
            {

                if (visited[row_index][column_index])
                    continue;
                int counter = 0;

                for (int inner_row_index = 0; inner_row_index < rows; inner_row_index++)
                {
                    for (int inner_column_index = 0; inner_column_index < columns; column_index++)
                    {
                        if (visited[inner_row_index][inner_column_index])
                            continue;
                        
                        if (strcmp(string[row_index][column_index], string[inner_row_index][inner_column_index]) == 0)
                        {
                            counter++;
                            visited[inner_row_index][inner_column_index] = 1;
                        }
                        printf("1\n");
                    }
                     printf("%s occur %d times", string[row_index][column_index], counter);
                }


               
            }
        }
    }
    return 0;
}
