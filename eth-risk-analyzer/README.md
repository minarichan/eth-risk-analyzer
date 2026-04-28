# Ethereum Transaction Risk Analyzer

## Overview

A Python-based blockchain analytics tool designed to evaluate Ethereum wallet activity and identify potentially suspicious transaction patterns.

## Quick Start

pip install -r requirements.txt
python eth_analyzer.py

Enter an Ethereum wallet address when prompted.

## Features

* Retrieves real-time transaction data using Etherscan API
* Performs transaction value and frequency analysis
* Detects behavioral anomalies (e.g. high-value transfers, address concentration)
* Assigns a wallet risk score (0–100)
* Exports structured datasets for further investigation
* Includes time-based anomaly detection to identify rapid transaction bursts often associated with automated or malicious activity.

## Example Output

--- Summary ---
Total transactions: 100
Total ETH moved: 0.0013
Largest transaction: 0.0012

--- Risk Analysis ---
⚠️ High concentration of transactions to a single address

Wallet Risk Score: 30/100

## How It Works

1. User inputs an Ethereum wallet address
2. The tool fetches transaction history
3. Data is analyzed for suspicious patterns
4. A risk score is generated
5. Results are exported as CSV files

## Technologies

* Python
* Pandas
* Etherscan API

## Example Use Case

This tool simulates basic blockchain forensic analysis, similar to workflows used in cryptocurrency fraud detection and compliance monitoring.

## Future Improvements

* Smart contract interaction analysis
* Known malicious wallet detection
* Visualization dashboard

## Author

Milena Belaja
