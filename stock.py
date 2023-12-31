
import matplotlib.pyplot as plt
import pandas as pd

# Create the data
data = pd.DataFrame({
    "Stock": ["Alibaba", "CRISPR Therapeutics", "CrowdStrike", "D-Wave", "DocuSign", "Honeywell International", "IBM", "IonQ", "Nimbus Group", "Okta", "Pfizer", "Pinterest", "Polestar", "Quantum Computing", "Raytheon Technologies", "Rigetti Computing", "Salesforce", "Spotify", "Unit Software"],
    "Purchase Price (USD)": [91.5271, 52.21538, 124.77164, 2.11582, 59.06852, 214.88852, 138.8268, 11.41994, 3.57112, 81.8741, 40.92774, 21.92162, 3.9837, 1.32986, 97.15132, 1.0731, 151.64128, 121.92376, 30.74162],
    "Current Price (USD)": [110.37, 76.74, 146.66, 2.70, 84.27, 288.25, 134.25, 14.40, 4.34, 101.95, 52.32, 34.73, 5.75, 2.10, 119.34, 1.42, 171.55, 132.70, 40.04],
    "Profit or Loss (USD)": [61.40, -240.56, -12.82, 193.18, -250.13, -73.37, -4.6, -33.3, -38.44, -702.03, -831.25, -4791.25, -2963.25, -435.9, -891.14, -7.0, -512.32, -1874.60, -1568.45],
    "Percentage": [6.73, -45.43, -0.97, 932.14, -42.62, -34.09, -3.29, -29.21, -10.88, -79.29, -831.25, -2178.07, -792.76, -77.77, -891.14, -65.88, -34.44, -148.28, -51.91]
})

# Calculate the size of the bubbles
size = data["Profit or Loss (USD)"].abs() / 1000

# Set the colors
colors = ["red" if profit < 0 else "green" for profit in data["Percentage"]]

# Plot the bubble chart
plt.scatter(data["Purchase Price (USD)"], data["Current Price (USD)"], s=size, c=colors, alpha=0.7, label="Stocks")

# Add a title and labels
plt.title("My Stocks")
plt.xlabel("Purchase Price (USD)")
plt.ylabel("Current Price (USD)")
plt.legend()

# Show the plot
plt.show()


