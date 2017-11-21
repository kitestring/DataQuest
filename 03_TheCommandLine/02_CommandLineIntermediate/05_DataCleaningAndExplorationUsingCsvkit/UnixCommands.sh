# csvstack
csvstack -n year -g 2005,2007,2013 Hud_2005.csv Hud_2007.csv Hud_2013.csv > Combined_hud.csv
head -10 Combined_hud.csv
wc -l Combined_hud.csv

#csvlook
head -10 Combined_hud.csv | csvlook

#csvcut
csvcut -n Combined_hud.csv
csvcut Combined_hud.csv
csvcut -c 2 Combined_hud.csv

#csvstat
csvstat Combined_hud.csv

#csvcut | csvstat
csvcut -c 4 Combined_hud.csv | csvstat

#csvgrep
csvgrep -c 2 -m -9 Combined_hud.csv | head -10 | csvlook

#filtering out problematic rows
csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only.csv
