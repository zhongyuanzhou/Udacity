import sys
from copy import copy
sys.path.append("../tools/")
import pickle

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data
import sklearn
import remove_outlier

import evaluate

from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


import poi_ratio



features_list = [
    'from_messages',
    'from_poi_to_this_person',
    'from_this_person_to_poi',
    'shared_receipt_with_poi',
    'to_messages',
    'bonus',
    'deferral_payments',
    'deferred_income',
    'director_fees',
    'exercised_stock_options',
    'expenses',
    'loan_advances',
    'long_term_incentive',
    'other',
    'restricted_stock',
    'restricted_stock_deferred',
    'salary',
    'total_payments',
    'total_stock_value',
    ]


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

#features_list = ['poi', 'salary', 'bonus'] #1 
#features_list = ['poi', 'salary', 'bonus', 'from_this_person_to_poi'] #2
#features_list = ['poi', 'salary', 'from_poi_to_this_person', 'from_this_person_to_poi'] #3
features_list = ['poi','from_this_person_to_poi', 'from_poi_to_this_person', 'shared_receipt_with_poi'] #4
#features_list = ['poi','from_this_person_to_poi'] #5

### Load the dictionary containing the dataset
data_dict = pickle.load(open("../data/final_project_dataset.pkl", "r") )

### Task 2: Remove outliers
outliers = ['TOTAL']
remove_outlier.remove_outlier(data_dict, outliers)


### Task 3: Create new feature(s)
#Make Copies
my_dataset = copy(data_dict)
features_list = copy(features_list)

# add new feature new features
#new_feature.add_poi_interaction(my_dataset, features_list)


# add two new features
poi_ratio.add_poi_ratio(my_dataset, features_list)

#Used gaussianNB to quickly determine features with highest accuracy


#Gaussian test
#1 = Accuracy: 0.24480	Precision: 0.18368	Recall: 0.80600
#2 = Accuracy: 0.23282	Precision: 0.15703	Recall: 0.73700
#3 = Accuracy: 0.58418	Precision: 0.16291	Recall: 0.31100
#4 = Accuracy: 0.71678	Precision: 0.01757	Recall: 0.00500
#5 = Accuracy: 0.63971	Precision: 0.12392	Recall: 0.04300	F1: 0.06385

#4 = highest accuracy, try different classifier tunes to improve precision and recall

#Print features
print "{0} selected features: {1}\n".format(len(features_list) - 1, features_list[1:])


### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.

#clf = GaussianNB() 
#4 = Accuracy: 0.71678	Precision: 0.01757	Recall: 0.00500 <-excludes made up feature
#5 = Accuracy: 0.71489	Precision: 0.02833	Recall: 0.00850 <- includes made up feature
clf = sklearn.tree.DecisionTreeClassifier()
#Accuracy: 0.73856	Precision: 0.39827	Recall: 0.34550

#Decision tree showing immediate gains in all categories over GaussianNB.  
#Will use for tuning

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script.

#clf = sklearn.tree.DecisionTreeClassifier(max_depth = 1) #1                       
#Accuracy: 0.81478	Precision: 0.93701	Recall: 0.17850

#clf = sklearn.tree.DecisionTreeClassifier(max_depth = 5) #2
# Accuracy: 0.77133	Precision: 0.48155	Recall: 0.37850

#clf = sklearn.tree.DecisionTreeClassifier(max_depth = 10) #3
#Accuracy: 0.75467	Precision: 0.44439	Recall: 0.41550

#clf = sklearn.tree.DecisionTreeClassifier(criterion = 'entropy') #4
#Accuracy: 0.76611	Precision: 0.47042	Recall: 0.41750

#clf = sklearn.tree.DecisionTreeClassifier(criterion ='entropy',max_depth = 1) #5
#Accuracy: 0.81222	Precision: 0.93296	Recall: 0.16700

#clf = sklearn.tree.DecisionTreeClassifier(criterion ='entropy',max_depth = 10) #6
#Accuracy: 0.76800	Precision: 0.47511	Recall: 0.42000

#clf = sklearn.tree.DecisionTreeClassifier(min_samples_leaf=5) #7
#Accuracy: 0.76378	Precision: 0.46106	Recall: 0.37300

clf = sklearn.tree.DecisionTreeClassifier(min_samples_leaf=2) #8
#Accuracy: 0.78322	Precision: 0.51510	Recall: 0.41800

#Most all models meet requirements but I will use #8 as my final model

test_classifier(clf, my_dataset, features_list)

### Dump your classifier, dataset, and features_list so 
### anyone can run/check your results.

dump_classifier_and_data(clf, my_dataset, features_list)
