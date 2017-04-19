import pandas as pd
import numpy as np
from regression import SoftmaxRegression

df = pd.read_csv("/Users/yliang/data/trunk4/spark/assembly/target/tmp/LogisticRegressionSuite/multinomialDataset/part-00000", header = None)
X = np.array(df[df.columns[2:6]])
y = np.array(df[df.columns[0]])
smr = SoftmaxRegression(fit_intercept=False, alpha=1000.0, max_iter=100, tol=1e-06, standardization=False)
smr.fit(X, y)
print("coefficients = " + str(smr.coef_))
print("intercept = " + str(smr.intercept_))