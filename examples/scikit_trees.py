#!/usr/bin/env python

import numpy as np
import pandas as pd
import pickle

from ai_streaming.model_streaming.ml_stremer import MLStreamer

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

class TestModel(MLStreamer):


    def __init__(self):
         MLStreamer.__init__(self)
         self.score = None
        

    def arg_setup(self, argumentar):
        argumentar.add_split_data()
        argumentar.add_custom_files(['alive'])

    def file_loader_setup(self, loader, config):
        loader['alive'] = lambda x: pd.read_csv(x)
        

    def model_setup(self, config):
        tree = DecisionTreeClassifier(criterion='gini',
                                      splitter='best',
                                      max_depth=None,
                                      min_samples_split=2,
                                      min_samples_leaf=1,
                                      min_weight_fraction_leaf=0.0,
                                      max_features=None,
                                      random_state=None,
                                      max_leaf_nodes=None,
                                      min_impurity_decrease=0.0,
                                      min_impurity_split=None,
                                      class_weight=None,
                                      presort=False)
        print('Decision Tree built!')
        return tree

    
    def model_load(self, files, keras):
        print("Not supported!")
        exit(1)
        


    def load_data(self, config, files):
        train, validate, test = files

        print(f'Loading train data from {train}')
        print(f'Loading test data from {test}')


        encoder = LabelEncoder()
        
        train_df = pd.read_csv(train)
        train_df = train_df[config['columns']]
        train_df = pd.get_dummies(train_df, columns=['Sex'], drop_first=True)    
        train_df['Age'] = train_df['Age'].fillna(train_df['Age'].mean())
        train_df = train_df.sample(frac=1)
        train_df.dropna(inplace=True)
        
        train_df['Embarked'] = train_df[['Embarked']].apply(encoder.fit_transform)
        

        test_df = pd.read_csv(test)
        test_df = test_df[config['test_columns']]
        test_df = pd.get_dummies(test_df, columns=['Sex'], drop_first=True)
        test_df['Age'] = test_df['Age'].fillna(test_df['Age'].mean())
        test_df.fillna(method='ffill', inplace=True)
        test_df['Embarked'] = test_df[['Embarked']].apply(encoder.transform)

        prediction = config['predict']
        X_train = train_df.loc[:, train_df.columns != prediction].values
        y_train = train_df.loc[:, train_df.columns == prediction].values
        X_test = test_df.loc[:, test_df.columns != 'PassengerId'].values
        index_test = test_df.loc[:, test_df.columns == 'PassengerId'].values

        
        print('X_train shape', X_train.shape)
        print('y_train shpe:', y_train.shape)
        print('X_test shpe:', X_test.shape)

        
        # exit(1)
        return (X_train, y_train, X_test, index_test)

        
            
    def pipeline(self, config, model):
        print('Runnung inner pipeline')
        return dict()

    
    def train_model(self, config, data, model, pipeline):
        X, y, _, _ = data
        
        print('Fitting the tree')
        model.fit(X, y)
                        
    
    def eval_model(self, config, data, model, pipeline):
        X, y, X_test, index_test = data

        self.score = model.score(X, y)
        print("Score on train set:", self.score)

        test_result = model.predict(X_test)
        res_df = pd.DataFrame({"Passengerid": index_test.ravel(), "Survived":test_result})
        print(res_df.head(10))

    def save_model(self, config, model, ouput):

        print(self.score)
        
        pass
        
        


def main():
    TestModel().run()

if __name__ == '__main__':
    main()
