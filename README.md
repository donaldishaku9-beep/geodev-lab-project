# My GeoDev Lab Africa project

Where are the gaps in school coverage in Brighter area (Tudun Wada South ward), 
Chanchaga LGA, Minna, Niger State, relative to where people actually live?

Built over twelve months with GeoDev Lab Africa, Cohort One.

## Project files
- [Week 1 — Project brief](./project-brief.md)
- [Week 2/3 — Data notes and quality checks](./data-notes.md)
- [Week 4 — Analysis summary](./month-1-summary.md)
- [Week 4 map Week 4 coverage map](./week4_school_coverage_map.png)
- Prepared data: [`processed/`](./processed/)

## Key finding
13% (2.11 km², or 2.11 out of 15.69 km²) of Tudun Wada South ward falls 
outside 1.5km of a school, based on GRID3's 47 mapped school locations.




## Month 2: Preparation of environment and early python
- Week 5: I setup python, VS code and the terminal. [hello.py](./hello.py) runs and [week5.png](./screenshots/week5.png) is the result.
- Week 6: Set up the project with uv and added pandas. [check.py](./check.py) prints the pandas version. The result, [week6.png](./screenshots/week6.png).
- Week 7: [analyse.py](./analyse.py) reads [wards.csv](./wards.csv), converts each area and classifies each ward. The result, [week7.png](./screenshots/week7.png).
- Week 8: [inspect_data.py](./inspect_data.py) reads [mydata.csv](./mydata.csv) and summarises `pop_sum` and `pop_mean`, the WorldPop population within 1.5 km of each of my 47 schools. The enrolment columns were empty, so I added these in QGIS. [week8.png](./screenshots/week8.png)
- Week 9: [summary.py](./summary.py) splits the inspection into three small functions, and `summarise_all` reports the count, smallest, largest and average of `pop_sum` and `pop_mean` in [mydata.csv](./mydata.csv). [week9.png](./screenshots/week9.png)

### Month 2 reflection

What finally clicked this month was debugging by looking at the real data. When my script crashed on `student_ct`, I counted the filled cells in every column and found that `student_ct`, `teacher_ct` and `secondary_` were empty for all 47 schools, so the problem was my data and not my code. What is still fuzzy is `encoding="utf-8-sig"`: I know it removes a hidden marker that causes a KeyError on the first column, but I don't fully understand where that marker comes from. My capstone shows that the population within about 1.5 km of a school ranges from roughly 10,800 to roughly 59,700 people (average [35293.79102526495]), so the number of people near each school varies a lot, and the empty enrolment columns mean I can't yet say how many pupils each school has.
Weeks 8 and 9 run on my Month 1 data: [mydata.csv](./mydata.csv) is my GRID3 schools layer for Tudun Wada South ward, with the two population columns I added in QGIS, so the Python scripts summarise the same 47 schools I mapped in Month 1.
