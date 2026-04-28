import requests
import pandas as pd

API_KEY = "YOUR_API_KEY_HERE"
WALLET = input("Enter Ethereum wallet address: ")

url = "https://api.etherscan.io/v2/api"

params = {
    "chainid": "1",
    "module": "account",
    "action": "txlist",
    "address": WALLET,
    "startblock": "0",
    "endblock": "99999999",
    "page": "1",
    "offset": "100",
    "sort": "desc",
    "apikey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

if data.get("status") != "1":
    print("Error:", data)
    exit()

df = pd.DataFrame(data["result"])

df["value"] = df["value"].astype(float) / 10**18

print("\n--- Summary ---")
print("Total transactions:", len(df))
print("Total ETH moved:", round(df["value"].sum(), 4))
print("Largest transaction:", round(df["value"].max(), 4))

print("\n--- First 5 Transactions ---")
print(df[["from", "to", "value"]].head())

# RISK ANALYSIS
print("\n--- Risk Analysis ---")

risk_score = 0

high_value = df[df["value"] > 50]
top_receivers = df["to"].value_counts().head(3)

df["timeStamp"] = pd.to_datetime(df["timeStamp"], unit="s")

time_diff = df["timeStamp"].diff().dt.total_seconds()

print(f"Rapid transactions count: {(time_diff < 10).sum()}")

if (time_diff < 10).sum() > 5:
    print("⚠️ Rapid transaction activity detected")
    risk_score += 20

if len(high_value) > 0:
    print(f"⚠️ {len(high_value)} high-value transactions detected")

print("\nTop receiver addresses:")
for address, count in top_receivers.items():
    print(f"{address} → {count} transactions")

risk_score = 0

if len(df) > 500:
    risk_score += 30

if len(high_value) > 5:
    risk_score += 40

if not top_receivers.empty:
    top_count = top_receivers.iloc[0]
    concentration_ratio = top_count / len(df)

    if concentration_ratio > 0.8:
        print("⚠️ High concentration of transactions to a single address")
        risk_score += 20

print(f"\nWallet Risk Score: {risk_score}/100")

# Save full transaction data
df.to_csv(f"{WALLET}_transactions.csv", index=False)

# Save suspicious transactions
suspicious_df = df[df["value"] > 50]
suspicious_df.to_csv(f"{WALLET}_suspicious_transactions.csv", index=False)

print("\nFiles saved successfully:")
print(f"{WALLET}_transactions.csv")
print(f"{WALLET}_suspicious_transactions.csv")
