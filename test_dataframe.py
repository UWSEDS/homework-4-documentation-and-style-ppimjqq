"""This is for CSE583 HW4

Revise your homework 3 to make it PEP8 compliant. The grading rubric is:

(2 pt) Module-level documentation.
(2 pt) Function-level documentation that includes descriptions of arguments and return values.
(3 pt) pylint score of at > 8. (Include the output from pylint in your homework repository.)"""

##1. Create a DataFrame from a URL that points to a CSV file.

    ## test from hw2
    # condition1: there are at least 10 rows in the DataFrame
    # condition2: The values in each column have the same python data type
    # condition3: The dataframe contains only the columns that you specified as the second argument

def test_create_dataframe(dataframe, columns):

    '''This function tests the three conditions discussed above.
    The dataframe is a daraframe entered and the columns are a list of strings.
    The return will be True or False'''

    if  len(dataframe) >= 10 and dataframe.equals(dataframe.dtypes) and  sorted(dataframe.columns) == sorted(columns):

        return True

    return False

        # raise ValueError("The dataframe doesn't meet the requirement in hw2")


def check_values_correct_types(dataframe):

    '''This function tests that all columns have values of the correct type'''
    for j in list(dataframe.columns):

        return all(type(dataframe[j][i]) == type(dataframe[j][0]) for i in range(len(dataframe[j])))

def check_nan_values(dataframe):

    ''' This function tests whether the dataframe has null values '''
    if dataframe.isnull().values.any():
        return True

    return False

def check_rows_morethan_one(dataframe):

    ''' This function tests whether the daraframe has at least one row '''
        # self.assertTrue(dataframe.shape[0]>=1)
    return len(dataframe) >= 1

# if __name__=='__main__':

#     DataFrameTest(dataframe)
