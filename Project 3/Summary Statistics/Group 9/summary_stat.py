import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/perespen/Downloads/CCC_Exercise_1_Data_Python.csv", sep = ";", decimal = ",")

# descriptive statistics of Apple's stock return
mean_apple = pd.DataFrame.mean(data.Return_Apple)
median_apple = pd.DataFrame.median(data.Return_Apple)
std_apple = pd.DataFrame.std(data.Return_Apple)
skew_apple = pd.DataFrame.skew(data.Return_Apple)
kurt_apple = pd.DataFrame.kurt(data.Return_Apple)
stat_apple = pd.DataFrame([[mean_apple, median_apple, std_apple, skew_apple, kurt_apple]],
                       columns=[0, 1, 2, 3, 4])
stat_apple = stat_apple.T

# descriptive statistics of Alphabets's stock return
mean_alphabet = pd.DataFrame.mean(data.Return_Alphabet)
median_alphabet = pd.DataFrame.median(data.Return_Alphabet)
std_alphabet = pd.DataFrame.std(data.Return_Alphabet)
skew_alphabet = pd.DataFrame.skew(data.Return_Alphabet)
kurt_alphabet = pd.DataFrame.kurt(data.Return_Alphabet)
stat_alphabet = pd.DataFrame([[mean_alphabet, median_alphabet, std_alphabet, skew_alphabet, kurt_alphabet]],
                       columns=[0, 1, 2, 3, 4])
stat_alphabet = stat_alphabet.T

sum_stat = pd.concat([stat_apple, stat_alphabet], axis=1)
sum_stat.index = ["mean", "median", "std", "skew", "kurt"]
sum_stat.columns = ["Apple", "Alphabet"]
print(sum_stat.round(4))

# histogram of Apple's stock returns
r_apple = [data.iloc[0:250, 2]]
plt.hist(r_apple, bins = 100)
plt.show()

# histogram of Alphabet's stock returns
r_alphabet = [data.iloc[0:250, 4]]
plt.hist(r_alphabet, bins = 100)
plt.show()

# scatter plot of Apple's and Alphabet's stock returns
plt.scatter(r_apple, r_alphabet)
plt.show()