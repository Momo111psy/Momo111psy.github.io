import re
with open('dubai_leads_sample.csv', 'r') as f:
    count = len(f.readlines()) - 1
with open('index.html', 'r') as f:
    html = f.read()
new_html = re.sub(r'<span id="lead-count">.*?</span>', f'<span id="lead-count">{count}</span>', html)
with open('index.html', 'w') as f:
    f.write(new_html)
