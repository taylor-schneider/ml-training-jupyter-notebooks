import pandas
import numpy

def calculate_velocity_and_acceleration(df, column_name):
    n = df[column_name].shape[0]

    # Add some empty columns to the dataframe to hold velocity and acceleration for the open
    df["{0}_v".format(column_name)] = numpy.zeros(n)
    df["{0}_a".format(column_name)] = numpy.zeros(n)


    # loop through the data points and calculate the statistics
    for t in range(1, n):
    
        # Calculate the velocity
        velocity = df[column_name][t] - df[column_name][t -1]
        df.at[t, "{0}_v".format(column_name)] = velocity
    
        # Caclulate the acceleration
        acceleration = df["{0}_v".format(column_name)][t] - df["{0}_v".format(column_name)][t -1]
        df.at[t, "{0}_a".format(column_name)] = acceleration
    
    return df
	
# Write a function to determine if two numbers have the same sign
def same_signs(a, b):
    if a > 0 and b > 0:
        return True
    if a > 0 and b < 0:
        return False
    if a < 0 and b > 0:
        return False
    if a < 0 and b < 0:
        return True
    else:
        return False

def same_space(a, b):

	if a[0] <= b[0] and a[1] >= b[1]:
		return True
		
	if a[0] >= a[0] and b[1] <= a[1]:
		return True
	
	return False
		
def calculate_iflection_point(df, column_name, debug=False):    

    n = df[column_name].shape[0]

    # Add some empty columns to the dataframe to hold velocity and acceleration for the open
    df["{0}_ip".format(column_name)] = numpy.zeros(n)
    
    # loop through the data points determine if we have hit an inflection point
    # We want to look for points where the acceleration equals zero or changes direction (cd)
    # and the velocity changes directions
    segment_count = 0
    for t in range(1, n):

        v = df["{0}_v".format(column_name)][t]
        v_1 = df["{0}_v".format(column_name)][t - 1]
        a = df["{0}_a".format(column_name)][t]
        a_1 = df["{0}_a".format(column_name)][t - 1]

        v_cd = int(not same_signs(v, v_1))
        a_cd = int(not same_signs(a, a_1))

        cd = int(v_cd and a_cd)
        
        # If this is the second point in the series we will get fals positives so ignore this one
        if t == 1:
            cd = 0

        if debug:
            df.at[t, "{0}_v_ip".format(column_name)] = v_cd
            df.at[t, "{0}_a_ip".format(column_name)] = a_cd
			
        df.at[t, "{0}_ip".format(column_name)] = cd
    
    return df

def convert_date_string_to_date(input_string):
    
    # The input variable will be a byte array
    # We will convert this to a string
    #input_string = raw_bytes.decode("utf-8")

    # We then do our manipulation
    input_string = input_string.strip()

    # Make it a date
    result = numpy.datetime64(input_string, 'D')

    return result