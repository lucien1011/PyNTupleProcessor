from Core.Module import Module
from sklearn.externals import joblib
import numpy as np

mlp_classifier_fname        = "mlp-classifier.pkl"
x_train_fname               = "X_train.npy"
y_train_fname               = "Y_train.npy"
x_validation_fname          = "X_validation.npy"
y_validation_fname          = "Y_validation.npy"

class MVASkimmer(Module):
    def __init__(self,name,mva_setting):
        super(MVASkimmer,self).__init__(name)
        self.mva_setting = mva_setting

    def begin(self):
        self.clf = joblib.load(self.mva_setting.modelPath)

    def analyze(self,event):
        npArray = np.array(self.mva_setting.varFunc(event)).reshape(1, -1)
        prob = self.clf.predict_proba(npArray)
        return prob[0,1] > self.mva_setting.threshold

    def end(self):
        self.mva_setting.varFunc.end()
