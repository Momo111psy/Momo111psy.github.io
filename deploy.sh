#!/bin/bash
# Update the lead count in the HTML file
python3 update_stats.py
# Add, Commit, and Push
git add index.html dubai_leads_sample.csv
git commit -m "Site Update: $(date +'%Y-%m-%d %H:%M')"
git push origin main
