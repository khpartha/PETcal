import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate fake data for 24 months
months = np.arange(1, 25)  # Months 1 to 24
production = np.random.randint(100, 1000, size=24)  # Random production numbers between 100 and 1000

# Create a DataFrame
data = pd.DataFrame({
    'month': months,
    'production': production
})

print(data.head())  # Display the first few rows

# Plot the fake production data
plt.plot(data['month'], data['production'], marker='o')
plt.xlabel('Month')
plt.ylabel('Production')
plt.title('Production Data')
plt.show()
