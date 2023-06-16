import warnings
warnings.filterwarnings("ignore")
## for data



from sklearn.ensemble import RandomForestClassifier

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


experiment_id = "0"
metric_name = "recall_test"

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
}
}