# CS70 Grade "Calculator"
This program predicts the grade you need to score on the final when inputted your midterm score. 

Percentiles may vary slightly from semester to semester, so you ideally want to score a little bit above the lower bound to be safe.

*Note: I'm not responsible for you failing to declare or if you cry about not getting the grade that the calculator said you would get.*

## Requirements
1. Python 3
2. Scipy module
3. Numpy module

Note: you may have to use pip instead of pip3

### Installation for Linux/MacOS users:
```
pip3 install python3
pip3 install scipy
pip3 install numpy
```

## Running the Program:

`cd` into the same folder as the .py then run the following: 
```
python3 predict_70_final.py
```

## How it works:
You have two options:
* Option A: You want to get an "[desired grade] and want to find out the final std range that you need score within to get [desired grade].
    * Output: [lower bound std, upper bound std] for [desired grade]

* Option B: You want to get a very specific [desired overall std]. This option tells you exactly what std you need on the final to get that. 
    * Output: exact std for the final to get [desired std]

* Option C: All possible grade ranges. If I scored [__] on the midterm, what do I need for an A, A-, B+, ...

## Optional CLI Functionality:
You can additionally run
```
python3 predict.py score [-g desired grade] [-s desired std]
```

With either the `-g` or `-s` argument to see your desired grade or desired standard deviation.
