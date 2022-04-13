# CS70 Grade "Calculator"
This program predicts the grade you need to score on the final when inputted your midterm score. 

Percentiles may vary slightly from semester to semester, so you want to score a little bit above the lower bound to be safe. Ideally, try to hit the median between the lower and upper bound.

*Disclaimer: I'm not responsible if you fail to declare or if you cry about not getting the grade that the calculator said you would get. I made this for myself out of pure anxiety to give myself some semblance of certainty.*

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

`cd` into the same folder as the .py file then run the following: 
```
python3 predict_70_final.py
```

**Rudimentary predictor factoring in Corr(MT, Final)**
```
python3 predict_70_corr.py
```

## How it works:
You have two options:
* Option A: You want to get an "[desired grade]" and want to find out the final std range that you need score within to get [desired grade].
    * Output: (lower bound std, upper bound std) for [desired grade]

* Option B: You want to get a very specific [desired overall std]. This option tells you exactly what std you need on the final to get that. 
    * Output: exact std for the final to get [desired std]

* Option C: All possible grade ranges. If I scored [__] on the midterm, what do I need for an A, A-, B+, ...
    * Output: [grade]: (lower bound std, upper bound std)

## Optional CLI Functionality:
You can additionally run
```
python3 predict.py score [-g desired grade] [-s desired std] [-a] [-c]
```

With either the `-g` or `-s` argument to see your desired grade or desired standard deviation, or the `-a` argument to show all grades, and the `-c` argument to use the correlation based grade estimator. Note that it is highly recommended to use `-ac` for the correlation based CLI input; use of `-g` and `-s` are experimental and may be inaccurate. Please run `python3 predict.py -h` for more information.
