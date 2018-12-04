import math


class DecisionTree:
    def __init__(self):
        pass

    def read_data(self, filename):
        fid = open(filename, "r")
        data = []
        d = []
        for line in fid.readlines():
            d.append(line.strip())
        for d1 in d:
            data.append(d1.split(","))
        fid.close()

        self.featureNames = self.get_features(data)
        data = data[1:]
        self.classes = self.get_classes(data)
        data = self.get_pure_data(data)

        return data, self.classes, self.featureNames

    def get_classes(self, data):
        data = data[1:]
        classes = []
        for d in range(len(data)):
            classes.append(data[d][-1])

        return classes

    def get_features(self, data):
        features = data[0]
        features = features[:-1]
        return features

    def get_pure_data(self, data_rows):
        data_rows = data_rows[1:]
        for d in range(len(data_rows)):
            data_rows[d] = data_rows[d][:-1]
        return data_rows

    def zero_list(self, size):
        d = []
        for i in range(size):
            d.append(0)
        return d

    def get_argmax(self, arr):
        m = max(arr)
        ix = arr.index(m)
        return ix

    def get_distinct_values(self, data_list):
        distinct_values = []
        for item in data_list:
            if distinct_values.count(item) == 0:
                distinct_values.append(item)
        return distinct_values

    def get_distinct_values_from_table(self, data_table, column):
        distinct_values = []
        for row in data_table:
            if distinct_values.count(row[column]) == 0:
                distinct_values.append(row[column])
        return distinct_values

    def get_entropy(self, p):
        if p != 0:
            return -p * math.log(p + 1e-30, 2)
        else:
            return 0

    def create_tree(self, training_data, classes, features, max_level=-1, level=0):
        n_data = len(training_data)
        n_features = len(features)

        try:
            self.featureNames
        except:
            self.featureNames = features

        new_classes = self.get_distinct_values(classes)
        frequency = self.zero_list(len(new_classes))
        total_entropy = 0
        index = 0
        for a_class in new_classes:
            frequency[index] = classes.count(a_class)
            prob = float(frequency[index]) / n_data
            total_entropy += self.get_entropy(prob)
            index += 1

        default = classes[self.get_argmax(frequency)]
        if n_data == 0 or n_features == 0 or (0 <= max_level < level):
            return default
        elif classes.count(classes[0]) == n_data:
            return classes[0]
        else:
            gain = self.zero_list(n_features)
            for feature in range(n_features):
                g = self.get_gain(training_data, classes, feature)
                gain[feature] = total_entropy - g

            best_feature = self.get_argmax(gain)
            new_tree = {features[best_feature]: {}}

            values = self.get_distinct_values_from_table(training_data, best_feature)
            for value in values:
                new_data = []
                new_classes = []
                index = 0
                for row in training_data:
                    if row[best_feature] == value:
                        if best_feature == 0:
                            new_row = row[1:]
                            new_names = features[1:]
                        elif best_feature == n_features:
                            new_row = row[:-1]
                            new_names = features[:-1]
                        else:
                            new_row = row[:best_feature]
                            new_row.extend(row[best_feature + 1:])
                            new_names = features[:best_feature]
                            new_names.extend(features[best_feature + 1:])
                        new_data.append(new_row)
                        new_classes.append(classes[index])
                    index += 1

                subtree = self.create_tree(new_data, new_classes, new_names, max_level, level + 1)

                new_tree[features[best_feature]][value] = subtree
            return new_tree

    def get_gain(self, data, classes, feature):
        gain = 0
        ndata = len(data)

        values = self.get_distinct_values_from_table(data, feature)
        feature_counts = self.zero_list(len(values))
        entropy = self.zero_list(len(values))
        value_index = 0
        for value in values:
            data_index = 0
            new_classes = []
            for row in data:
                if row[feature] == value:
                    feature_counts[value_index] += 1
                    new_classes.append(classes[data_index])
                data_index += 1

            class_values = self.get_distinct_values(new_classes)
            class_counts = self.zero_list(len(class_values))
            class_index = 0
            for classValue in class_values:
                for aclass in new_classes:
                    if aclass == classValue:
                        class_counts[class_index] += 1
                class_index += 1

            for class_index in range(len(class_values)):
                pr = float(class_counts[class_index]) / sum(class_counts)
                entropy[value_index] += self.get_entropy(pr)

            pn = float(feature_counts[value_index]) / ndata
            gain = gain + pn * entropy[value_index]

            value_index += 1
        return gain

    def show_tree(self, dic, seperator):
        if type(dic) == dict:
            for item in dic.items():
                print(seperator, item[0])
                self.show_tree(item[1], seperator + " | ")
        else:
            print(seperator + " -> (", dic + ")")
