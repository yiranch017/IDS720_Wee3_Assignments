# GDP_and_CO2
This repository uses data from the World Development Indicators and plots GDP per capita against infant mortality.
By Laura Yiran

HI! This is Laura :D

## Week 4

### Exercise 1

Using `np.loadtxt()`, load the vector of household incomes located at [https://raw.githubusercontent.com/nickeubank/practicaldatascience/master/Example_Data/us_household_incomes.txt](https://raw.githubusercontent.com/nickeubank/practicaldatascience/master/Example_Data/us_household_incomes.txt). Please load the data by passing that URL directly into `np.loadtxt()` as a string—the autograder we're using needs to be able to run your code remotely, which it can't do if it references a file on your hard drive.

### Exercise 2

One of the best ways we have for getting a feel for our data is to plot our data. Plot a histogram of a numpy vector with:

```python
from matplotlib import pyplot as plt
plt.hist(your_array)
```

Use this `plt.hist()` method to plot your income data. Does it look like a normal distribution? Uniform? Does this make you think that income equality is relatively high or low in the United States?

> It doesn't look normal - heavily right-skewed. This suggests that income equality is relatively low in the United States

**Note:** The x-axis' will range will be determined by the data, with the x-axis being made long enough to include ALL data (but no longer). As a result, there *are* observations across the x-axis, even if there are too few for the bar to be visible.

**Note:** Be aware that this data only measures *income*—e.g., wages, salaries, etc. As a result, it actually massively underestimates incomes at the top of the United States income distribution because most of the income for high earners comes in the form of capital gains and investment appreciation which are not included here.

### Exercise 3

You will likely notice that much of the plot is difficult to see because most of the plot is taken up by very high earners. 

Since the x-axis of our plot is determined by the range of our data, we can create a histogram of US household incomes that includes only households making less than $500,000 to improve our ability to visualize what's going on at lower incomes. For these households—the non-millionaires—do we see a more uniform distribution of incomes? Or is there still a significant [right-skew / positive-skew](https://en.wikipedia.org/wiki/Skewness) (most people are on the left of the distribution, but there are more extreme values in the right tail) in the income distribution?

In other words, is the skewness in the US income distribution driven by extreme high earners, or is it evident at all income levels?

(Obviously the autograder will not be able to evaluate your answer to this question, but the TAs will).

> It's still right-skewed. This implies that the skewness is evident at all income levels.

### Exercise 4

The US poverty line is *about* 20,000 dollars a year. What share of households in these data fall below the US poverty line? (By "share" I mean the proportion, a value between 0 and 1).

(I say "about" because the actual poverty line for household income depends on the number of people in the household, which we have not included in these data.)

Using the `gini` function, calculate the Gini Index of income inequality in the US. What is that value?

Store your share of households under 20,000 as `ex4_share_below_poverty`, store the gini score as `ex4_gini`.

### Exercise 5

Go compare your estimate to that of [other countries here.](https://www.indexmundi.com/facts/indicators/SI.POV.GINI/rankings) (Note: in this table, estimated Gini values have been multiplied 100. In addition, as a result of sampling variation, income binning, differences in the exact methods used to calculate income, year of data, availability of data on top incomes, etc., your Gini for the US will be somewhat different from the Gini for the US in this table. It *should* be close to the data from the [US Census Bureau](https://www.statista.com/statistics/219643/gini-coefficient-for-us-individuals-families-and-households/)). How does the US compare to other countries? Is that what you expected? 
   - **Note:** The Gini Index of income is only one metric of inequality! Results would be very different if we were to calculate, for example, the ratio of the income of the top 0.1% of earners to the income of the lowest-earning 10% of the population, or if we calculated this metric using wealth instead of income!

> U.S. ranks 46th out of 162 countries on the World Bank GINI index ranking from high to low GINI values. The U.S. has the worst GINI index among developed countries.  
>It is sad, but this is what I expected.

### Exercise 6

- `Policy A`: giving every household that makes less than 40,000 dollars a check for 5,000 dollars, or 
- `Policy B`: giving every household that makes less than 30,000 dollars a check for 7,000 dollars. 

What is the new Gini under Policy A?  Store in the `results` dict under the key `"ex6_gini_policy_a"`.
What is the new Gini under Policy B?  Store in the `results` dict under the key `"ex6_gini_policy_b"`.

Which has lowered inequality more? Store your answer as the string `"Policy A"` or `"Policy B"` in the `results` dict under the key `"ex6_gini_which_reduced_more`.

**Note:** Vectors are mutable (like lists), so you should create a clean copy of your income data with the `.copy()` method (e.g. `experiment1 = income_vector.copy()`) before starting to make changes during each exercise. We'll talk a lot more about vector mutability in a future reading, but so long as you use `.copy()` you will be fine here! 

**Note:** Gini values won't change a lot due to these kinds of changes, so you'll need to look to three or four decimal places.

### Exercise 7

- `Policy C`: applying a tax of 5% to households making more than 250,000 dollars and using the money to pay down the National Debt. 

(In other words, `Policy C` would reduce the income of any households earning more than 250,000 dollars by 5%.)

Calculate the Gini Index resulting from the tax proposal. Store in the `results` dict under the key `"ex7_gini_policy_c"`.

### Exercise 8

Now suppose we were thinking about applying a 5% tax to people making more than 250,000 dollars and *evenly distributed that tax revenue* to households earning less than 30,000 dollars. Call this `Policy D`. 

To estimate the effective such a policy on inequality, first calculate the total amount of money that would be generated by this tax if the households in this data were all households in the US.  Store in the `results` dict under the key `"ex8_revenue_raised"`.
  
**Note:** because these data are just a *sample* of households in the US, the quantity you calculate isn't the actual revenue such a tax would generate in the real world; if you want to calculate the real amount that would be raised, you can multiply the quantity you calculate by 137 (our data include about 1 out of every 137 households in the US).

### Exercise 9

Now calculate the total number of households earning less than 30,000 dollars in these data, and divide the revenue generated by the tax by the number of households earning less than 30,000 dollars. This is the amount of transfer these household would receive. Store in your `results` dict with the key `"ex9_transfers"`.

**Note:** unlike in Question 8, the quantity you estimate here *is* a good estimate of the amount of money that would be available for each household if we imposed this tax on the real world. Why? Because both the quantity you estimated in Question 8 *and* the number of households you calculate here represent 1/137th the actual, real world quantities in the United States. So when you divide one by the other, you get the true ratio -- the fact that both are 1/137th the real quality cancels out!

### Exercise 10

Finally, update the incomes in our data *as if* we had enacted this policy -- reduce the incomes of households earning more than 250,000 dollars by 5% and increase the incomes of households earning less than 30,000 dollars by the quantity you estimated in Question 8. 

What is the resulting Gini Index of `Policy D`? Store as `ex10_gini_policy_d`.

### Exercise 11

Now suppose we also wanted to explore a slightly different intervention: `Policy E`. In `Policy E`, we would distribute the revenue generated with the same tax, but this time we would distribute it evenly to all households earning less than 40,000 dollars (instead of less than 30,000 dollars). 

What is the resulting Gini Index of `Policy E`? Store as `ex11_gini_policy_e`.

### Exercise 12

If the President asked you whether you could better reduce inequality (as measured by the Gini Index) by re-distributing the tax revenue from taxing households earning more than 250,000 dollars even to households earning less than 30,000 dollars (`Policy D`) or households earning less than 40,000 dollars (`Policy E`), which would you recommend? Assign the string `"Policy D"` or `"Policy E"` to your `results` dict under the key `ex12_policy_recommendation`.
