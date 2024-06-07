import pandas as pd
import matplotlib.pyplot as plt

# load data
path = "/Users/sushmitha/Desktop/pattern_analysis/Pattern Analysis Test.xlsx"
df = pd.read_excel(path, sheet_name='Blog Data - October - Sep - Aug')

# Convert date columns 
df.columns = [pd.to_datetime(col) if "0:00:00" in str(col) else col for col in df.columns]
df.set_index("Blog Url", inplace=True)
total_views = df.sum(axis=1)

# Calculate average daily page views for each blog URL
average_views = df.mean(axis=1)
views_summary = pd.DataFrame({
    "Total Views": total_views,
    "Average Daily Views": average_views
})

# Convert index to str
views_summary.index = views_summary.index.astype(str)

# Extract blog names from URLs for better readability in the plot
def extract_blog_name(url):
    parts = url.split("/")
    for idx, part in enumerate(parts):
        if part == "blog" and idx + 1 < len(parts):
            return parts[idx + 1]
    return "Unknown"

# Apply the function 
views_summary['Blog Name'] = views_summary.index.map(extract_blog_name)

plt.figure(figsize=(12, 10))

# Extracting data for plotting
blog_names = views_summary['Blog Name'].values
total_views = views_summary['Total Views'].values

# Plotting
plt.barh(blog_names, total_views, color='skyblue')
plt.xlabel("Total Views")
plt.ylabel("Blog Name")
plt.title("Total Page Views for Each Blog")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
