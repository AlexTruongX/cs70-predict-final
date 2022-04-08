import numpy as np
import scipy.stats as st
import argparse
"""
@author Alex Truong
Predicts final score while factoring in 50% two-way clobber policy for CS70
"""

def mt1_zscore(raw_score):
    # Updated 4/5/22
    mean = 132.72
    std = 39.01

    return (raw_score - mean)/std

def avg_std(score1, score2):
    return (score1 + score2)/2

def grade(percentile):
    if 0.95 <= percentile <= 100:
        return 'A+'
    elif 0.78 <= percentile <= 0.95:
        return 'A'
    elif 0.66 <= percentile <= 0.78:
        return 'A-'
    elif 0.43 <= percentile <= 0.66:
        return 'B+'
    elif 0.26 <= percentile <= 0.43:
        return 'B'
    elif 0.16 <= percentile <= 0.26:
        return 'B-'
    elif 0.11 <= percentile <= 0.16:
        return 'C+'
    elif 0.07 <= percentile <= 0.11:
        return 'C'
    elif 0.04 <= percentile <= 0.07:
        return 'C-'
    else:
        return 'F'

def grade_to_z(grade):
    grade = grade.strip().upper()
    # Percentiles pulled from Berkeley Time (historically accurate)
    grades_to_p = {'A+' : [0.95, 0.99], 'A' : [0.78, 0.95], 'A-' : [0.66, 0.78],
                'B+' : [0.43, 0.66], 'B' : [0.26, 0.43], 'B-' : [0.16, 0.26],
                'C+':[0.11, 0.16], 'C' : [0.07, 0.11], 'C-' : [0.04, 0.07],
                'F' : [0.00, 0.04]}

    if grade not in grades_to_p:
        print(f"You are actually trolling. {grade} is not a possible grade.")
        exit()
    else:
        percentile = grades_to_p[grade]
        lower_z = round(st.norm.ppf(percentile[0]), 2) # norm.ppf is inverse of norm.cdf
        upper_z = round(st.norm.ppf(percentile[1]), 2)
        return [lower_z, upper_z]

def predict_final_std_range(grade, mt1_raw):
    grade_range = grade_to_z(grade)
    mt1_std = mt1_zscore(mt1_raw)
    lower = predict_final_std_exact(grade_range[0], mt1_raw, should_print=False)
    upper = predict_final_std_exact(grade_range[1], mt1_raw, should_print=False)
    print(f'Midterm 1 std: {mt1_std}')
    print(f'To get an {grade}, you need to get a final std between ({lower},{upper}) based on past data.')


def predict_final_std_exact(desired_std, mt1_raw, should_print=True):
    mt1_std = mt1_zscore(mt1_raw)

    for final_std in np.arange(-3, 3, 0.0001):
        clobber = avg_std(mt1_std, final_std)
        delta = 0.01
        overall_std = round(avg_std(max(mt1_std, clobber), max(final_std, clobber)), 2)

        if abs(overall_std - desired_std) <= delta:
            overall_p = st.norm.cdf(overall_std) # converts to percentile in normalized distribution
            overall_grade = '\033[1m' + grade(overall_p)

            if should_print:
                print(f'Desired std for a grade of an {overall_grade}\033[0m: {desired_std}')
                print(f'Midterm 1 std: {mt1_std}')
                print(f'You need a final std of {round(final_std, 2)} to get a {overall_grade} \033[0min the class.')
                return
            else:
                return round(final_std, 2)

    print("Probabilistically Impossible")
    exit() 

def predict():
    print('\u2500' * 10)
    print("Option A: I want to end the class with <desired grade>, what final std range do I need to score within?")
    print("Option B: I want to end the class with <exact desired std>, what exact final std do I need?")
    print(' ' * 10)
    choice = input('Which option sounds like you? A or B? ').strip().upper()

    if choice == 'A':
        mt1_raw = input('Enter your midterm 1 raw score: ')
        grade = input('Enter the grade you want to end the class with (e.g B+): ')
        print()
        predict_final_std_range(grade, float(mt1_raw))
    elif choice == 'B':
        mt1_raw = input('Enter your midterm 1 raw score: ')
        overall_desired_std = input('Enter the standard deviation you want to end the class with: ')
        print()
        predict_final_std_exact(float(overall_desired_std), float(mt1_raw))

    print('\u2500' * 10)


if __name__ == "__main__":
    # calling the main function
    predict()
