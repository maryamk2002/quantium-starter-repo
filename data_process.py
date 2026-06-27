import pandas as pd

# Read the files
df1 = pd.read_csv(r"C:\Users\user\Desktop\Forage\quantium-starter-repo\data\daily_sales_data_0.csv")
df2 = pd.read_csv(r"C:\Users\user\Desktop\Forage\quantium-starter-repo\data\daily_sales_data_1.csv")
df3 = pd.read_csv(r"C:\Users\user\Desktop\Forage\quantium-starter-repo\data\daily_sales_data_2.csv")


master_df = pd.concat([df1, df2, df3])
#only keep pink morsel
master_df = master_df[master_df["product"] == "pink morsel"]
master_df["price"] = master_df["price"].str.replace("$", "", regex=False)
master_df["price"] = master_df["price"].astype(float)

master_df["sales"] = master_df["quantity"] * master_df["price"]

master_df = master_df[["sales", "date", "region"]]

# Save it to a clean CSV without adding random row numbers
master_df.to_csv("formatted_data.csv", index=False)