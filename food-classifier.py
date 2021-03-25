from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]] # [weight, texture], 0 - smooth, 1 - bumpy
labels = [0, 0, 1, 1] # 0 - apple, 1 - orange
clf = tree.DecisionTreeClassifier() # box of rules
clf = clf.fit(features, labels) # training algorithm
print(clf.predict([[150, 0]])) # prediction
