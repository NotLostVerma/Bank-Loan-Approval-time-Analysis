# %%
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path 

# Load the dataset
BASE_DIR = Path.cwd()
csv_path = BASE_DIR / "bank_loan_approval_time_dataset.csv"

df = pd.read_csv(csv_path)
df
# %%
# Calculating statistics for approval times
mean_time = df["Approval_Time_Days"].mean()
std_time = df["Approval_Time_Days"].std()
median_time = df["Approval_Time_Days"].median()
min_time = df["Approval_Time_Days"].min()
max_time = df["Approval_Time_Days"].max()

# %%
# Displaying the computed statistics
print("Mean Approval Time:", mean_time)
print("Standard Deviation:", std_time)
print("Median:", median_time)
print("Min:", min_time)
print("Max:", max_time)

# %%
# Plotting the distribution of approval times
plt.hist( df["Approval_Time_Days"],
    bins=15,
    color="#43D857",
    edgecolor="black",
    alpha=0.85)
plt.xlabel("Approval Time (Days)")
plt.ylabel("Number of Applications")
plt.title("Distribution of Loan Approval Time")
plt.show()

# %%
# Identifying efficient vs delayed approvals
efficient = df[df["Approval_Time_Days"] <= 14]
delayed = df[df["Approval_Time_Days"] > 14]

print("Efficient approvals:", len(efficient))
print("Delayed approvals:", len(delayed))

