from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
import os

class ClassifierModel:

    def __init__(self):
        self.sc_X = StandardScaler()

    def read_data_set(self):
        knn = pd.read_csv("data/Iris.csv")
        knn.head()
        X = knn.iloc[:, [1, 2, 3, 4]].values
        y = knn.iloc[:, 5].values
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.20, random_state=0)

    def train_model(self):
        self.read_data_set()
        self.X_train = self.sc_X.fit_transform(self.X_train)
        self.X_test = self.sc_X.transform(self.X_test)
        self.classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
        self.classifier.fit(self.X_train, self.y_train)

    def test_accuracy(self):
        y_pred = self.classifier.predict(self.X_test)
        acc = accuracy_score(self.y_test, y_pred)
        print(acc)
        print(classification_report(self.y_test, y_pred))

    def run_model(self, input_data):
        input_data = self.sc_X.fit_transform(input_data)
        predicted_class = self.classifier.predict(input_data)
        return predicted_class

    def dump_pickle(self):
        knn_pickled_model = open('pickle_knn_model.pkl', 'wb')
        pickle.dump(self.classifier, knn_pickled_model)
        knn_pickled_model.close()

    def load_pickle(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        knn_pickled_model = open(dir_path + '/pickle_knn_model.pkl', 'rb')
        self.classifier = pickle.load(knn_pickled_model)


if __name__ == '__main__':
    model = ClassifierModel()

    print("Beginning to Pickle SVM Model!")
    model.train_model()
    model.test_accuracy()
    model.dump_pickle()
    print("Done: Model!\n")