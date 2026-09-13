import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv", parse_dates=["order_date"])
df["revenue"] = df["quantity"] * df["unit_price"]

print("Total Revenue:", round(df["revenue"].sum(), 2))
print("\nRevenue by Region:")
print(df.groupby("region")["revenue"].sum().sort_values(ascending=False))

monthly = df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum()
monthly.plot(kind="line", marker="o", title="Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_revenue.png", dpi=150)
plt.show()
