# Import libraries to manipulate data
import pandas
import numpy 
import matplotlib.pyplot as pyplot

# Define a utility function to plot a dataframe
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

# Write a conversion function to handle our data that is in date format
def convert_date_string_to_date(input_string):
    
    # The input variable will be a byte array
    # We will convert this to a string
    #input_string = raw_bytes.decode("utf-8")

    # We then do our manipulation
    input_string = input_string.strip()

    # Make it a date
    result = numpy.datetime64(input_string, 'D')

    return result

def calculate_moving_mean_and_std(dataframe, column_name):
    
    # Add a mean and variance column to the dataframe
    mean = numpy.empty(dataframe.shape[0], dtype=float)
    std= numpy.empty(dataframe.shape[0], dtype=float)

    # Loop through the rows of the dataframe and calculate the moving mean and std deviation
    x = 0
    for idx, row in dataframe.iterrows():
        mean[x] = dataframe[column_name][0:x].mean()
        std[x] = dataframe[column_name][0:x].std()
        x += 1
        
    return pandas.DataFrame({"mean": mean, "std": std, "date": dataframe["date"]}, index=dataframe.index)
	
def plot_moving_mean_and_std_for_dataframes(dataframe, x_axis_name, axis):
        
    # Graph the mean and std
    axis.plot(dataframe[x_axis_name], dataframe["mean"], color = "red")
    axis.plot(dataframe[x_axis_name], dataframe["mean"] + dataframe["std"], color = "black")
    axis.plot(dataframe[x_axis_name], dataframe["mean"] - dataframe["std"], color = "black")  
    
    # Beautify the x-labels
    pyplot.gcf().autofmt_xdate()