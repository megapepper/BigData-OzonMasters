#!/opt/conda/envs/dsenv/bin/python

import sys, os
import logging
from joblib import load
import pandas as pd
#import csv
#from sklearn.metrics import mean_squared_error

sys.path.append('.')
from model import fields

#
# Init the logger
#
logging.basicConfig(level=logging.DEBUG)
logging.info("CURRENT_DIR {}".format(os.getcwd()))
logging.info("SCRIPT CALLED AS {}".format(sys.argv[0]))
logging.info("ARGS {}".format(sys.argv[1:]))

# tmp test 
#train_path = sys.argv[1]
#filtered_labels_path = sys.argv[2]

#load the model
model = load("1.joblib")


#tmp
valid_headers = [fields[0]]+[fields[i] for i in range(2, len(fields))]
#valid_headers = [fields[i] for i in range(2, len(fields))]
#valid_headers = fields
logging.info("valid_headers {}".format(valid_headers))
#read and infere
read_opts=dict(
        sep='\t', names=valid_headers, index_col=False, header=None,
        iterator=True, chunksize=100
)

for df in pd.read_csv(sys.stdin, **read_opts):
    pred = model.predict(df)
    out = zip(df.id, pred)
    print("\n".join(["{0}\t{1}".format(*i) for i in out]))
'''
with open('predicted.csv', 'w') as write_obj:
    csv_writer = csv.writer(write_obj)
    i = 0
    for val in pred:
        csv_writer.writerow([ind[i], val])
        i += 1

y_test = 
model_score = mean_squared_error(y_test, pred)
model_score2 = model.score(X_test, y_test)

logging.info(f"model score 1: {model_score:.3f}")
logging.info(f"model score 2: {model_score2:.3f}")

'''