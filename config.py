import warnings
warnings.filterwarnings("ignore")

from sklearn.tree import DecisionTreeClassifier

# ensample imports 
from sklearn.ensemble import (
                              RandomForestClassifier, 
                              GradientBoostingClassifier,
)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression



experiment_id = "473545552416447086"
metric_name = "precision_test"

# Step 2: define the metrices
my_scoring = {
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "f1_score": "f1",
    "auc": "roc_auc"
}


# Step 1: Define models and their hyperparameters
models = {
    "logistic_regression": {
    "estimator": LogisticRegression(),
    "param_grid": {
        "classifier__penalty": ["l1", "l2"],
        "classifier__C": [0.1, 1, 10],
        "classifier__solver": ["liblinear", "lbfgs"]
    }
},
    "random_forest": {
        "estimator": RandomForestClassifier(),
        "param_grid": {
            "classifier__n_estimators": [10, 50, 100],
            "classifier__max_depth": [3, 5, None],
            "classifier__min_samples_split": [2, 5]
        }
    },
    "decision_tree": {
    "estimator": DecisionTreeClassifier(),
    "param_grid": {
        "classifier__max_depth": [3, 5, None],
        "classifier__min_samples_split": [2, 5],
        "classifier__min_samples_leaf": [1, 2]
    }
},
    "gradient_boosted_trees": {
    "estimator": GradientBoostingClassifier(),
    "param_grid": {
        "classifier__n_estimators": [50, 100, 200],
        "classifier__learning_rate": [0.01, 0.1, 1],
        "classifier__max_depth": [3, 5, None],
        "classifier__min_samples_split": [2, 5],
        "classifier__min_samples_leaf": [1, 2]
    }
}, 
    "k_nearest_neighbors": {
    "estimator": KNeighborsClassifier(),
    "param_grid": {
        "classifier__n_neighbors": [3, 5, 7],
        "classifier__weights": ['uniform', 'distance'],
        "classifier__algorithm": ['ball_tree', 'kd_tree', 'brute'],
        "classifier__leaf_size": [10, 30, 50],
        "classifier__p": [1, 2]
            }
        },
}

        
       

