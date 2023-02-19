import tensorflow as tf
import pandas as pd
import numpy as np

COLOUMN_NAMES = ['orig_port', 'resp_port', 'protocol', 'service', 'duration',
       'orig_bytes', 'resp_bytes', 'conn_state', 'missed_bytes', 'history',
       'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'label']

dataSetEval = pd.read_csv("EvaluationDataSet.copy.csv",names=COLOUMN_NAMES,header=0)

ensembSet1 = pd.read_csv("EnsembleData.first.copy.csv")
print(ensembSet1.head())
#ensembSet2 = pd.read_csv("EnsembleData.second.csv")

'''
ensembSet3 = dataSetMalicious3.set_index(['orig_port', 'resp_port', 'protocol', 'service', 'duration',
       'orig_bytes', 'resp_bytes', 'conn_state', 'missed_bytes', 'history',
       'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'label']).join(dataSetBenign.set_index(['orig_port', 'resp_port', 'protocol', 'service', 'duration',
       'orig_bytes', 'resp_bytes', 'conn_state', 'missed_bytes', 'history',
       'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'label']))
'''

CATEGORICAL_COLOUMNS = [ 'protocol', 'service','conn_state','history' ]
NUMERICAL_COLOUMNS = ['orig_port', 'resp_port',  'duration',
       'orig_bytes', 'resp_bytes',  'missed_bytes',
       'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', ]

train_y1 = ensembSet1.pop("label")

#train_y2 = ensembSet2.pop("label")
#train_y3 = ensembSet3.pop("label")
eval_y = dataSetEval.pop("label")

print(train_y1)
#print(train_y2.head())
#printf(train_y3.head())
print(eval_y.head())

feature_coloumns = []
for key in CATEGORICAL_COLOUMNS:
       if key == "label": pass
       vocabulary = ensembSet1[key].unique()
       feature_coloumns.append(tf.feature_column.categorical_column_with_vocabulary_list(key, vocabulary))
for key in NUMERICAL_COLOUMNS:
       feature_coloumns.append(tf.feature_column.numeric_column(key=key,dtype=tf.float32))

print(feature_coloumns)

def make_input_function(data_df,label_df,shuffle = True,num_epoch=10,batch_size=32):
       def input_function():
              dataset = tf.data.Dataset.from_tensor_slices((dict(data_df),label_df))
              if shuffle:
                     dataset = dataset.shuffle(1000)
              dataset = dataset.repeat(num_epoch).batch(batch_size)
              return dataset
       return input_function

train_input_fn = make_input_function(ensembSet1
, train_y1)

classifier = tf.estimator.LinearClassifier(feature_columns=feature_coloumns)

classifier.train(make_input_function(ensembSet1,train_y1))
eval_result = classifier.predict(input_fn=make_input_function(dataSetEval, eval_y))
print(f"Test set accuracy = {eval_result}")