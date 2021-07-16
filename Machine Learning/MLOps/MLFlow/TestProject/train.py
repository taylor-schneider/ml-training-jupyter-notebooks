import sys
import argparse
import numpy
import pandas
import statsmodels.api
import itertools
import warnings


warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore", category = statsmodels.api.tools.sm_exceptions.ValueWarning)

print("Parsing Args")
parser = argparse.ArgumentParser(description='A Python Web Server')
parser.add_argument('-d', '--data-file', help='A data file to load.', required=True)
parser.add_argument('-t', '--ticker', help='The ticker to model.', required=True)
args = parser.parse_args()

print("Loading Data")



def convert_date_string_to_date(input_string):
    
    # The input variable will be a byte array
    # We will convert this to a string
    #input_string = raw_bytes.decode("utf-8")

    # We then do our manipulation
    input_string = input_string.strip()

    # Make it a date
    result = numpy.datetime64(input_string, 'D')

    return result

converter_mapping = {
    "date": convert_date_string_to_date
}

import pandas
pandas_dataframe = pandas.read_csv(args.data_file, converters=converter_mapping)
aaba_dataframe = pandas_dataframe[pandas_dataframe["ticker"] == args.ticker]
aaba_dataframe = aaba_dataframe.sort_values(by="date", ascending=True)

print("Showing Data")
print(aaba_dataframe.head())

print("Train The Machine Learning Model")

# Split the data into a train and test set
datapoint_count = aaba_dataframe.shape[0]
split_point = int(datapoint_count * 0.8)
train_df = aaba_dataframe[:split_point]
test_df = aaba_dataframe[split_point:]

# Generate the posisble parameters for the model
p = d = q = range(0, 3)
pdq_combinations = list(itertools.product(p, d, q))

# Train the model
#      Find the optimal parameter set and the coresponding performance metric
#


best_param_set = None
best_perf_metric = -1

for pdq in pdq_combinations:
    
    # Create the model
    model = statsmodels.api.tsa.statespace.SARIMAX(
        train_df["open"], 
        order=pdq, 
        enforce_stationarity=True, 
        enforce_invertibility=True)
    
    # Fit the model to the data
    fit_model = model.fit(disp=0)
    
    # Calculate performance metric
    aic = fit_model.aic
    
    # Record the results
    if aic < best_perf_metric or best_perf_metric == -1:
        best_param_set = pdq
        best_perf_metric = aic
        
    break

print("The best parameter set {} yielded an AIC of {}".format(best_param_set, best_perf_metric))
fit_model.summary()
                    
