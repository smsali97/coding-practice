from collections import Counter
class KNN:
    
    def __init__(self,X_train, y_train, k):
        self.X_train = X_train
        self.y_train = y_train
        self.k = k

    def _predict(self, x):
        
        distance_label = [[self.distance(x, x_train), y_train] for x_train, y_train in zip(self.X_train, self.y_train)]

        distance_label.sort(key=lambda x: x[0])

        k_nearest_labels = [label for _, label in distance_label[:self.k]]

        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
    
    def distance(self, x1, x2):
        return sum((a - b) ** 2 for a, b in zip(x1, x2)) ** 0.5
    
    def predict(self, X_test):
        return [self._predict(x) for x in X_test]
    
    def score(self, X_test, y_test):
        y_pred = self.predict(X_test)
        print('Predictions',y_pred)
        print('Actual',y_test)
        return sum(y == y_ for y, y_ in zip(y_pred, y_test)) / len(y_test)



    
def main():
    X_train = [[0, 0], [1, 0], [0, 1], [1, 1]]
    y_train = [0, 1, 1, 0]
    X_test = [[0, 0], [1, 0], [0, 1], [1, 1]]
    y_test = [0, 1, 1, 0]
    knn = KNN(X_train, y_train, 3)
    print(knn.score(X_test, y_test))

if __name__ == '__main__':
    main()
    