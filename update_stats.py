import datetime

# Count current leads
with open('dubai_leads_sample.csv', 'r') as f:
    count = sum(1 for line in f) - 1

# Update the HTML file
with open('index.html', 'r') as f:
    content = f.read()

# Replace the number and add trial info
content = content.replace('107', str(count))
content = content.replace('2026-01-20 16:07', datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

with open('index.html', 'w') as f:
    f.write(content)
