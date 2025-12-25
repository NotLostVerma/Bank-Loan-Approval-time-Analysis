# Bank Loan Approval Time Analysis

## Project Overview
The project evaluates the time taken by banks to process loan approvals through elementary statistical procedures.
The aim is to analyze the time duration for approval, assess the efficiency of the process, and plot the approval time distribution using Histogram.

## Objectives
- Analyze loan approval duration using descriptive statistics
- Measure process efficiency based on approval time
- Visualize approval time distribution using histograms
- Interpret results to identify potential delays in the approval process

## Dataset
The dataset is a synthetic dataset created for academic analysis, using numpy and controlled number generation(Not done by me) which contains the following fields:
- Application_ID
- Applicant_Age
- Applicant_Income
- Credit_Score
- Loan_Amount
- Employment_Type
- Application_Channel
- Previous_Default
- Approval_Time_Days

## Methodology
- Calculated statistical values like mean, median, standard deviation, minimum value, and maximum value
- Created a histogram to examine the distribution of approval times
- Categorized loan approvals as efficient (less than 14 days) and delayed (more than 14 days) for the efficiency of the process

## Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook / VS Code

## Results
- The average time taken for approval of the loans and the corresponding variability were determined through statistical analysis
- Histogram plot showed us the distribution of approval times
- A major share of the apps was processed within the optimal approval time

## Conclusion
This analysis reveals that the time for loan approvals has moderate variability. Though most of the business applications are processed efficiently, the delay observed in a few indicates there is potential for optimizing the respective processes using automation and verification techniques.

## How to Run
1. Clone the repository
2. Install required libraries using `pip install -r requirements.txt`
3. Open and run `analysis.ipynb` or execute the Python script from the `src` folder

## Author
Krish Verma

## Medium Blog Post Link
> https://medium.com/@krishv553/statistical-analysis-of-bank-loan-approval-time-using-python-6e00dd8280ef
