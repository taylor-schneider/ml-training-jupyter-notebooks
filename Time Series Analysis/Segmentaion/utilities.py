import pandas
import numpy
import matplotlib.pyplot as pyplot

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

def plot_dataframe(dataframe1, x_axis_name, y_axis_name, scatter=True, line=False):
    
    # Create a new graph object
    figure, axis = pyplot.subplots(nrows=1,ncols=1,figsize=(12,6))

    # Get the dimensions of the graph area
    #xmin = dataframe1[x_axis_name].min()
    #xmax = dataframe1[x_axis_name].max()
    #ymin = dataframe1[y_axis_name].min()
    #ymax = dataframe1[y_axis_name].max()
 
    #axis.set_xlim([xmin,xmax])
    #axis.set_ylim([ymin,ymax])

    # Graph a scatter plot on the graph we created
    if scatter:
        axis.scatter(dataframe1[x_axis_name], dataframe1[y_axis_name])
    
    if line:
        axis.plot(dataframe1[x_axis_name], dataframe1[y_axis_name], color="green")
    
    # Beautify the x-labels
    pyplot.gcf().autofmt_xdate()
    
    return figure, axis


	
	