# CS70 Grade "Calculator"
This program gives an statistical approximation for the standard deviation you need to score on the final if you want a specific grade given your midterm score. 

Percentiles may vary slightly from semester to semester, so you want to score a little bit above the lower bound to be safe. Ideally, try to hit the median between the lower and upper bound.

*Disclaimer: I'm not responsible if you fail to declare or if you end not getting the grade that the calculator said you would get. I made this for myself out of pure anxiety to give myself some semblance of certainty.*

## Requirements/Dependencies
1. Python 3.8+
2. Scipy
3. Numpy

### Installation for Linux/MacOS users:

`cd` into the `cs70-predict-final` folder you just installed and run the following:
```
pip3 install -r requirements.txt # if pip3 doesnt work try pip
```

If the above fails, you can manually run the commands yourself: 
```
pip3 install scipy
pip3 install numpy
```
#### Still running into issues?
If you're still running into issues after installing the modules, double check to make sure that your Python version is up-to-date by typing `python3 –-version` into the terminal.

## Running the Program:

`cd` into the same folder as the .py file then run the following: 

*Calculate your expected letter grade using your Spring 2022 midterm and final score:*
```
python3 calc_overall_grade.py
```

*Predictor factoring in Corr(MT, Final) & Weights of MT & Final*
```
python3 predict_70_corr.py
```

*Unweighted Predictor*
```
python3 predict_70_final.py
```

## How it works:
The predictor factors in the two-way 50%-clobbering policy and assumes everyone has 100% in all other categories besides exams, which according to course staff, buckets HW-Option students without homework i.e very similar to No-HW Option students. 
* For HW-Option students: the reason we can make this assumption is because this "extreme case" where everyone gets full points on HW "is actually the norm for almost all students getting above a B-.  With the new 73% is enough policy for homework, this is even more true; 90% of the students whose final score was above the B range received essentially full points on the homework" (according to TA). It's also quite difficult to account for actual deviations but the difference is nearly negligible. 
* Factors excluded: deviations within HW bins (i.e non-100%) and class-wide z-score shifting after clobbering.


You have three options:

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
