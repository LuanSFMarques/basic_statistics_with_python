# *Basic Statistics with Python*
## **Summary**
```python
print("Hello Statistics!")
```
Welcome to the *Basic Statistics with Python* course! Here you will learn the fundamentals of statistics and how to apply them using Python. You’ll also get hands-on experience importing and using essential libraries such as NumPy, pandas, Matplotlib, SciPy, and Seaborn.

Throughout the course, we will explore the theoretical meaning of key statistical concepts, covering their general meaning, analytical interpretation, and technical applications.

Statistics is a powerful tool for understanding the behavior of datasets and interpreting what they represent in the real world. It equips you to avoid being misled by false information, extract meaningful insights, and—in more advanced topics—learn how to manipulate data effectively. While this course focuses on the basics, don’t underestimate the value of mastering these foundational concepts. A solid understanding of statistics allows you to quickly extract insights from data, whether by interpreting graphs or analyzing statistical results. Our goal is to provide a well-structured learning experience by combining theoretical knowledge with practical problem-solving.

So, let’s embark on this exciting journey together!

## **Table of Contents**
- Requirements
- Central Tendency (Theory)
- Central Tendency (Practice)
- Dispersion
- Distribution
- Final Project

## **Requirements**
In this section, we will cover the requirements and some initial setup content.

---

*Jupyter Lab*

To begin with the development environment (for using Python), I recommend using Jupyter Lab. It is a web-based development environment, part of the Project Jupyter, designed for working with notes, code, and data in general. It is easy to use and is by far one of the fastest ways to analyze data, at least in terms of studying.

Jupyter Lab functions like a code editor but allows you to separate your code into blocks and execute them individually. You can create code blocks and note blocks (in Markdown style), which makes it easy to annotate your code in a clean and visually appealing way. This structure helps you organize and identify different parts of your project effortlessly.

To learn how to use this tool, I recommend watching this video:

- https://www.youtube.com/watch?v=5pf0_bpNbkw

Here you will learn how to install Jupyter and start a project. Don’t be intimidated by the initial setup process—it’s straightforward once you get the hang of it.

- "But what if I don’t want to use Jupyter Lab or Jupyter Notebook?" 

Well, you can use VSCode or any other code editor you prefer! However, be aware that using Jupyter Lab or Jupyter Notebook will significantly boost your productivity in the long run. Jupyter Lab makes annotations and split code execution incredibly easy.

---

*Basic Math and functions*

A basic understanding of math and how functions work is essential for a deeper understanding of the calculations involved in statistics. While you won’t need to manually implement statistical formulas (as they are built into libraries like NumPy, pandas, and SciPy), familiarity with numbers and mathematical concepts is highly beneficial.

---

*Python*

Obviously, you will need Python installed on your computer for this course. I am using Python 3.13.1, so be mindful of potential version compatibility issues if your Python version is significantly older.

If you are using VSCode, I recommend installing extensions like Pylance and the Python Debugger to make debugging your code much easier.

This course assumes you have a basic understanding of Python. We won’t use advanced Python features, but we will rely heavily on libraries that connect us to statistical concepts.

---

*Python Libraries*

Some of the libraries listed here will be used occasionally, while others will be used extensively. The most important library you need to install is NumPy, as it provides efficient handling of arrays and numerical operations, making it essential for large-scale data processing. You’ll use it frequently—or its counterpart, pandas, which is built on top of NumPy.

Speaking of pandas, this library is crucial when working with dataframes (similar to spreadsheets). For example, if you have a table of students with three columns—name, age, and final score—you can use pandas to store this data in a DataFrame. From there, you can perform statistical analysis and much more.

These two libraries are the main ones, but we will also use Matplotlib, SciPy, and Seaborn. These libraries will help us create graphs and utilize various statistical functions.

- "How to Install the Libraries?"

To install the required libraries, use the following commands in your terminal (one by one). 

Note: Do not type the > symbol, it simply represents the command prompt.
```cmd
> pip install numpy
> pip install pandas
> pip install matplotlib
> pip install seaborn
> pip install scypy
```

Finally, use this block of code to test if all the libraries are working:
```python
import numpy as np
import pandas as pd
import matplotlib.pyploy as plt
import seaborn as sns
import scipy

# Show the current installed version of the librarie
print(np.__version__)
print(pd.__version__)
print(plt.__version__)
print(sns.__version__)
print(scipy.__version__)
```

## **Central Tendency**

### **Central Tendency (Theory)**

*Note: If you're already comfortable with this topic and understand the nuances well, feel free to skip to the practical part!*

A lot of things in the world can be measured by looking at a single number that represents a large set of numbers. For example, you might judge whether a class of students is performing well by checking if the **mean score** of the entire class is above the minimum passing grade. So, a class with a mean score of 3.5 out of 4 is better than a class with a mean of 3 out of 4, right? Well, not necessarily.

We’ll explore why relying solely on the mean can sometimes mislead us—and others who may not have a strong grasp of basic statistics. The mean can hide important details about the data. That’s where other measures of central tendency, like the **median** and **mode**, come into play.

But before diving into those, let’s clarify what **central tendency** actually means:
- *Central tendency is a central or typical value for a probability distribution. Colloquially, measures of central tendency are often called averages.*

In simple terms, central tendency is about summarizing an entire collection of numbers into a single, representative value. Sounds straightforward, right? Let’s look at the three most common measures of central tendency:
1. **Mean**
2. **Median**
3. **Mode**

Each of these measures does something slightly different, and their results may or may not be the same.

---

#### **1. Mean**
The **mean** of a set of numbers is the sum of all the values divided by the number of values.

- **Example**: (10, 20, 30, 40, 50)
- **Mean**: (10 + 20 + 30 + 40 + 50) / 5 = **30**

You’re probably already familiar with the mean, but let’s see why I said earlier that a class with a mean of 3.5 isn’t necessarily better than one with a mean of 3.

Here are two sets of numbers representing the scores of two classes:

- **First Class**: (0.2, 0.9, 1.5, 2.2, 2.7, 3.5, 4.0, 4.0, 4.0, 4.0)  
  **Mean**: 3.5

- **Second Class**: (2.8, 2.8, 2.9, 2.9, 3.0, 3.0, 3.1, 3.1, 3.2, 3.2)  
  **Mean**: 3.0

At first glance, the first class seems better because its mean is higher. But look closer: the second class is much more consistent. While the first class has some students scoring 4.0 (which is great), it also has five students scoring below 2.8 (the lowest score in the second class). 

The mean of the first class is 16% higher than the second, but 50% of its students scored lower than the worst-performing student in the second class. This shows why you need to be careful when interpreting the mean—it might not always tell the full story.

---

#### **2. Median**
The **median** is the middle value in a dataset when the numbers are arranged in order. It’s like finding the “center point” of the data. If the dataset has an odd number of values, the median is the middle one. If it’s even, the median is the average of the two middle values.

- **Examples**:
  - (1, 2, 3, 4, 5) → **Median**: 3
  - (14, 25, 100, 245, 1000) → **Median**: 100
  - (15, 16, 17, 18) → **Median**: (16 + 17) / 2 = **16.5**

You might be wondering, “Why would I use the median?” Well, the median gives you important insights, especially when used alongside the mean.

Let’s look at two classes that both have a mean of 2.5:

- **First Class**: (1.5, 1.5, 1.5, 4, 4)  
  **Median**: 1.5

- **Second Class**: (0.5, 2.0, 3.0, 3.3, 3.7)  
  **Median**: 3.0

Even though both classes have the same mean, their medians are very different. The first class has a median lower than its mean, while the second class has a median higher than its mean. These differences can reveal interesting patterns in the data.

We’ll explore this further in a future chapter when we discuss **distribution** and **dispersion**, which look at how numbers are spread out in a dataset.

#### **3. Mode**

The last method of central tendency we’ll explore is the **mode**. The mode is the value that appears most frequently in a dataset. While it’s not as commonly used in datasets with many unique values, it’s particularly useful for smaller datasets or when dealing with categorical data.

Let’s look at an example: Imagine we’re studying how many apples 10 people eat every day. Here’s the data:

- **Data**: (0, 0, 0, 1, 1, 1, 1, 2, 2, 3)

In this case, the number **1** appears 4 times, which is more frequent than any other value. So, we can say that **1** is a good representation of the average apple consumption per day.

You might wonder, “Why not just use the mean or median?” Let’s calculate them:

- **Mean**: (0 + 0 + 0 + 1 + 1 + 1 + 1 + 2 + 2 + 3) / 10 = **1.1**
- **Median**: (1 + 1) / 2 = **1**

The mean (1.1) feels a bit odd when talking about “average apple consumption”. The median (1) seems reasonable, but let’s look at two more examples to see why the mode can be more useful in some cases.

---

##### **Example 1:**
- **Data**: (0, 0, 0, 0, 1, 2, 2, 2, 3)  
  **Median**: 1

Here, the median is **1**, but notice that the number **1** only appears once, while **0** and **2** each appear 4 and 3 times, respectively. This can be misleading because the median doesn’t reflect the most common behavior in the dataset.

---

##### **Example 2:**
- **Data**: (0, 0, 0, 1, 1, 2, 2, 2, 2, 3)  
  **Median**: (1 + 2) / 2 = **1.5**

In this case, the median is **1.5**, which is a decimal value. Again, this might not be the most intuitive representation of “average apple consumption.”

---

#### **Why Use the Mode?**
The mode is particularly useful when the data has clear, repeating values or when you’re dealing with categorical data (e.g., favorite colors, types of fruit). 

*Note: You could use the mode to check if a very specific decimal number repeats in a sample of billions of numbers for example, but it is more suited for specific cases.*

---

#### **Key Takeaways**
- **Mean**: Sum of all values divided by the size of the sample.
- **Median**: Middle point in the sample.
- **Mode**: Recognize the number that repeats the most in a sample.

Remember, summarizing data always involves some loss of information. It’s up to you to choose the right tool for the job and interpret the results critically. With practice, you’ll develop a keen sense of when to use each measure of central tendency and understand when a certain value is "biased" and doesn't represents the real meaning of the data.

---

### **Central Tendency (Practice)**

Finally, the practical part! This section is straightforward because it’s very easy to apply these central tendency functions using Python. You’ll only need to import NumPy and SciPy.

NumPy is essentially a library that does what standard Python lists don’t do well: handle numbers efficiently. NumPy arrays use much more sophisticated methods and structures to make our "lists" faster to manipulate, especially when dealing with very large datasets.

On the other hand, SciPy is a library specifically designed for scientific and technical computing. I won’t spend too much time explaining what it does, but for now, know that we’ll borrow a central tendency function from it.

---

#### **Importing Libraries**

```python
import numpy as np
from scipy import stats
```

The first line uses an alias ("np") to call the NumPy library, making it easier to reference throughout the script, and the second line imports only the stats module from SciPy. This means we’re using just a small part of the SciPy library in our code.

---

#### **Creating a NumPy Array**

Let’s start by creating a NumPy array (similar to a Python list). To create a NumPy array, we use np.array() and pass a Python list as an argument, then assign the result to a variable.

```python
array1 = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(f"Numpy Array 1: {array1}\n")
```

Output:

```terminal
> Numpy Array 1: [  0  10  20  30  40  50  60  70  80  90 100]
```

If you’re not familiar with the second line, it uses an f-string (formatted string literal) to merge text with a variable. By placing the variable inside {}, its value is automatically inserted into the string.

Typing [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] can be tedious, especially if you need a larger range (e.g., 0 to 1000 in steps of 10). Instead, you can use np.arange() to automate this process. Here’s how:

```python
array2 = np.arange(0, 101, 10)
print(f"Numpy Array 2: {array2}\n")
```

Output:

```terminal
> Numpy Array 2: [ 0 10 20 30 40 50 60 70 80 90 100]
```

You’ll notice that, except for the slight formatting difference, the result is the same as the first array. The np.arange() function creates an array that starts at 0, ends before 101 (100).

*Note: If you ever forget how to use np.arange() (or any other function), don’t hesitate to look it up! This is a normal part of learning and coding. Over time, you’ll become more familiar with these tools and use them effortlessly.*

---

#### **Applying Central Tendency Functions**

Now we can use all the three central tendency functions we learned in practice! Two of three function (*mean and median*) will be available in the numpy lib, and the last one (*mode*) will be available in the "scipy.stats" module.

```python
array2_mean = array2.mean()
array2_median = np.median(array2)
array2_mode = stats.mode(array2).mode # we need to call ".mode" again in the end of the line because the function .mode() returns a object, inside this object we have what we want, the "mode" as an numpy int.

print(f"Array 2 mean: {array2_mean}")
print(f"Array 2 median: {array2_median}")
print(f"Array 2 mode: {array2_mode}")
```

Output

```terminal
> Array 2 mean: 50.0
> Array 2 median: 50.0
> Array 2 mode: 0
```

So, pretty simple right? To call the mean function, we just put .mean() in the end of our numpy array. To call the median function, we need to get the function from np module and insert our numpy array as an argument. To call the mode function we need to get the mode function from stats (module from scipy) and use the array as an argument again.

*Note: Sometimes you will see that not all functions work with the same instructions, like the mean function (that is a built-in function inside the numpy array class) and the median function (that is a separated functions inside the module numpy, using you array as an argument inside this function). Just keep practice and this inconstancies will never bother you.*

So, there we have it! The just used the three main functions in central tendency, but we are not here just to know the commands, right? Let's look further and take some very simple insights.

---

#### **Histogram**

Sometimes, stare to numbers, especially in larger samples, will not give you a real notion of what that data means. A tool that is very often used to analyse numeric data is graphs, or in this case, histogram graph!

Histogram is a type of graph show to us how much numbers in certain intervals repeat in a sample, in crescent order.

Take this image as a reference:
![Hist Graph](/By_type/Statistics/basic_statistics_with_python/images/hist_graph1.png)

Here the x-axis represents the interval numbers and the y-axis represents the frequency of appearance. To take an example, between the interval of -0.96 and 0.93 we have more than 17.500 numbers. The blue columns are called "beans", and it represents here the intervals! So when we build our own graph, we can tell "how many intervals we want", or technically speaking, how much beans. 

Look at this another example of the same graph but with many more beans!
![Hist Graph](/By_type/Statistics/basic_statistics_with_python/images/hist_graph2.png)

We have a better notion of the visual structure of our data, but we have less visual precision in numbers because the intervals are very small (we could increase the size of the image and add more ticks in the x-axis indicating more intervals, but it will make the image polluted for educational purposes).

*Note: The more beans we have, the smaller the intervals will become and more precise the graph will be! Just remember that the number of intervals must be in context of the data*

---

#### **Histogram Graph Plot with Matplotlib**

First things first, "plot" means that we are making graphical representation of our data in a graph, making a relationship between two or more variables.

To create a plot of our data (array3), we need to use "Matplotlib" library. This will allow us to easily create some basic graphs just to look and learn more about or array.

Follow the instructions bellow to create the graph that i displayed earlier.

First, we need to import the "matplotlib" amoung our others libraries:
```python
import matplotlib.pyplot as plt
```

Here we are importing a module from matplotlib (like we have done with scipy, getting the stats module). You will not want to write "matplotlib.pyplot" in every line, so we used an easy alias "plt".

Before we create our graph, we need a new array, follow the next command block:
```python
array3 = np.random.normal(loc=0, scale=2, size=50000)
print(f"Numpy Array 3: {array3}\n")
```

Output
```python
> Numpy Array 3: [-0.22725259  2.75397768 -2.31461563 ... -1.73485301  0.62375124  0.46577891]
```


This new function called "random.normal()" will create what we call a "bell curve" with random values. The meaning of this type of array will be explaned in a future section. Just know that the histogram of these numbers will form what it looks like a "bell". We passed 50.000 in the argument "size" to create an array with 50.000 numbers, simple as that.

*Note: The intention here is to focus on the graph making and interpretation in central tendency. The meaning of the "array 3" function is part of another section!*

After this, we already can create our graph!


```python
plt.hist(array3, bins=200)
plt.show()
```

Output
![Hist Graph](/By_type/Statistics/basic_statistics_with_python/images/hist_graph2.png)

So, is very simple to make this kind of basic graph. First, just use "plt" module to call the "hist" function. Inside this function, pass the array as an argument and the numbers of bins (we used 200, so it's 200 intervals!).

The next thing is show the graph for us! If you use jupyter lab, you will only need the first line ("plt.hist(array3, bins=200)") to plot the graph and show it for you. But if you are using vscode or other similar code editon, you will need to use the command "plt.show()".

*Note: We created an array using np.random.normal(). This functions, as you can see, create RANDOM numbers based on some conditions, so my graph and your graph may look a little different.*




