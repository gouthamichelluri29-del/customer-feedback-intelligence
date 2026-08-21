import joblib
import pandas as pd

from huggingface_hub import hf_hub_download
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

MODEL_PATH = "models/sentiment_model.joblib"

def load_data():
    train_path = hf_hub_download(
        repo_id ="Cleanlab/amazon-reviews",
        filename = "train.csv",
        repo_type ="dataset"
    )
    test_path = hf_hub_download(
        repo_id ="Cleanlab/amazon-reviews",
        filename = "test.csv",
        repo_type ="dataset"
    )
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df


def balance_training_data(train_df):
    negative_df = train_df[train_df["label"]== "negative"]
    positive_df = train_df[train_df["label"]== "positive"].sample(
        n=len(negative_df),
        random_state = 42,
    )
    balanced_df = pd.concat(
        [positive_df,negative_df]
    ).sample(
        frac=1,
        random_state=42,
    ).reset_index(drop=True)

    return balanced_df

def train_model(train_df):
    model = Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=(1,2),
                    min_df=2,
                    max_features= 20000,
                ),

            ),
            (
                "classifier",
                LogisticRegression(max_iter=1000),
            ),
        ]
    )
    x_train = train_df["review_text"]
    y_train = train_df["label"]

    model.fit(x_train,y_train)
    return model

def evaluate_model(model, test_df):
    x_test = test_df["review_text"]
    y_test = test_df["label"]

    predictions = model.predict(x_test)

    print("\nAccuracy:")
    print(accuracy_score(y_test,predictions))
    print("\nClassification report:")
    print(classification_report(y_test, predictions, digits=4))
    print("\nConfusion matrix:")
    print(confusion_matrix(y_test, predictions))


def save_model(model):
    joblib.dump(model, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")

def main():
    train_df, test_df = load_data()

    print("\nOriginal training distribution:")
    print(train_df["label"].value_counts())

    train_df =balance_training_data(train_df)

    print("\nBalanced training distributions:")
    print(train_df["label"].value_counts())

    model = train_model(train_df)

    evaluate_model(model, test_df)
    save_model(model)

if __name__=="__main__":
    main()