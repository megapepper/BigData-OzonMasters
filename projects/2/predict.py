#!/opt/conda/envs/dsenv/bin/python

import sys, os
import logging
from joblib import load
import pandas as pd

sys.path.append('.')
from model import fields, fields_without_cat, model

#
# Init the logger
#
logging.basicConfig(level=logging.DEBUG)
logging.info("CURRENT_DIR {}".format(os.getcwd()))
logging.info("SCRIPT CALLED AS {}".format(sys.argv[0]))
logging.info("ARGS {}".format(sys.argv[1:]))


#load the model
model = load("2.joblib")


valid_headers = [fields[0]]+[fields[i] for i in range(2, len(fields))]
#read and infere
read_opts=dict(
        sep='\t', names=valid_headers, index_col=False, header=None,
        iterator=True, chunksize=100
)
logging.info('check_point')
'''
read_table_opts = dict(sep="\t", names=fields, index_col=False)
df = pd.read_table(sys.argv[1], **read_table_opts)
logging.info(df)
df = df[fields_without_cat]
logging.info(df)
df.replace('\\N', '0', inplace = True)
pred = model.predict(df)
out = zip(df.id, pred)
print("\n".join(["{0}\t{1}".format(*i) for i in out]))
'''
#'''

for df in pd.read_csv(sys.stdin, **read_opts):
    df = df[fields_without_cat]
    #logging.info(df)
    df.replace('\\N', '0', inplace = True)
    pred = model.predict(df)
    for elem in pred:
        if elem == '\\N':
            elem = 0
    out = zip(df.id, pred)
    print("\n".join(["{0}\t{1}".format(*i) for i in out]))
#'''