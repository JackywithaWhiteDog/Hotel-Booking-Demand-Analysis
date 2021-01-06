import numpy as np

def save_prediction(filename, arrival_date, label):
  prediction = np.concatenate((arrival_date.to_numpy().reshape(-1,1), label.reshape(-1,1)), axis=1)
  np.savetxt(filename, prediction, fmt=('%s','%i'),
            delimiter=',', header='arrival_date,label', comments='')