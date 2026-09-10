import pandas as pd

world = pd.read_csv(
    "https://github.com/nickeubank/MIDS_Data/"
    "raw/refs/heads/master/World_Development_Indicators/"
    "wdi_small_tidy_2015.csv"
)
world = world.plot.scatter(
    "Mortality rate, infant (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
)