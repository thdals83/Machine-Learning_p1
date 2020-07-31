
from sklearn.datasets import load_diabetes
diabetes=load_diabetes()

print(diabetes.data.shape,diabetes.target.shape)
x=diabetes.data[:,2]
y=diabetes.target