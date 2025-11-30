## Product Sales Forecasting: EDA, Hypothesis Testing, Modeling
#### Introduction:
Retail businesses operate in an environment where uncertainty in demand can lead to severe operational inefficiencies. Too little inventory leads to stock-outs and lost revenue; too much inventory increases holding costs and ties up capital unnecessarily. The ability to accurately forecast sales is therefore one of the most critical competencies for modern retail operations.
In this project, I worked on building an end-to-end Product Sales Forecasting pipeline using a real-world retail dataset. The goal was to understand sales behaviour through EDA, evaluate business claims using hypothesis testing, build a machine learning model to forecast sales, and finally deploy the model using a Flask API.
This blog summarises the entire process - insights, learnings, hypothesis test outcomes, modelling results, and how these insights can assist decision-makers in designing more effective strategies around inventory, staffing, promotions, and supply chain optimisation.

### Data Overview:
The dataset consists of 188,340 rows of daily store-level sales records with features such as:
Store_id: Unique store identifier
Store_Type: Category of store (S1, S2, S3, S4)
Location_Type: Location code (L1–L5)
Region_Code: Regional grouping (R1–R4)
Date: Transaction date
Holiday: Whether the date was a holiday
Discount: Whether discounts were offered
#Order: Number of orders
Sales: Total sales (target variable)

A quick .info() check showed:
No missing values
Data types were mostly correct
Date column needed to be converted to datetime
Several categorical columns required encoding
Numeric columns needed transformation for modelling

After converting the date, additional temporal features were extracted:
Year
Month
Day
Weekday

These would later help capture seasonal and cyclic patterns.

### Exploratory Data Analysis:
The EDA phase helped us understand how sales behave across time, regions, store types, and external factors.
#### a. Univariate analysis:
Sales Distribution:
Sales were highly right-skewed - indicating most days have moderate sales, but some days produce exceptionally high revenue. The boxplot confirmed the presence of upper outliers, which are typically driven by:
Promotional events
Holiday spikes
Seasonal effects

Sales DistibutionOrders Distribution:
Orders also showed positive skewness, with a median around ~63 orders/day but extreme values exceeding 300+. This aligns with common retail patterns: majority of days are stable, but some experience exceptionally high demand.

#### b. Time Series Trends:
Daily Sales Over Time:
Daily aggregated sales revealed:
Clear seasonal trends
Multiple upward spikes aligned with holiday/discount periods
Periodic troughs immediately after major sales weeks (post-sale cooldown)

Monthly Aggregation:
Monthly totals exhibited:
Strong seasonality
Slight upward trend year-over-year
Highest sales in peak buying seasons (Nov–Jan)

Understanding monthly seasonality is essential for forecasting and capacity planning.
#### c. Categorical Analysis:
Sales By store type:
Boxplots showed stark differences between the four store types:
S4 stores consistently produced the highest sales
S1 stores had the lowest median sales
S2 and S3 stores were mid-range

This suggests store format strongly influences sales - either due to store size, product mix, or customer base.
Sales By Region:
Region-level averages showed:
R1 and R4 dominated overall sales
R2 and R3 underperformed in comparison

This variation indicates geographical factors significantly influence sales - demographics, purchasing power, and competition differ by region.
#### d. Correlation Insights:
The correlation heatmap of numeric features revealed:
Sales and #Order have the strongest positive correlation
Holiday has a weak negative correlation with sales
Month/Day correlations reflect seasonal/cyclic patterns

The strong Sales–#Order correlation is expected: more orders naturally lead to higher sales.

### Hypothesis Testing:
To validate (or invalidate) common retail assumptions, we conducted statistical hypothesis tests.

#### Hypothesis 1: Do Discounts Increase Sales?

Null Hypothesis (H0): There is no difference in sales between discount and non-discount days.
Alternate Hypothesis (H1): Sales differ on discount days
Result:
t-stat = 145.93
p-value < 0.0001

Conclusion:
 We reject H0 - discount days have significantly higher sales.
Business Meaning:
 Discounts do boost customer purchasing behavior, confirming their effectiveness as a revenue lever.
#### Hypothesis 2: Do Holidays Affect Sales?
Null Hypothesis: Holiday and non-holiday sales show no difference.
Alternate Hypothesis: Holiday sales differ significantly
Result:
t-stat = -66.17
p-value < 0.0001

Conclusion:
 Sales on holidays are significantly different from non-holiday days.
 Since the t-statistic is negative, non-holiday sales are actually higher in this dataset.
Interpretation:
 Unlike typical assumptions, holidays here do not necessarily boost sales, which might indicate:
Holiday closures
Limited hours
Reduced shopping activity in some regions

#### Hypothesis 3: Do Store Types Have Different Sales?
One-way ANOVA was performed.
Result:
F-stat = 35,123.64
p-value < 0.0001

Conclusion:
 Store types differ significantly in mean sales.
Tukey HSD post-hoc tests confirmed every pair of store types differs significantly.

### Machine Learning Model:
Two models were trained:
Linear Regression (Baseline)
RandomForestRegressor (Advanced)

Data preprocessing included:
One-Hot Encoding for categorical variables
Standard scaling for numeric variables
Pipeline creation for clean workflow

Linear Regression Results
Metric Values:
MAE: 3669.87, RMSE: 5081.38, R2: 0.9236
Random Forest Results
Metric Values:
MAE: 1932.79, RMSE: 2922.09, R2: 0.9747
A massive improvement over Linear Regression:
47% decrease in MAE
42% decrease in RMSE
5% increase in R²

A score of 0.9747 indicates the model explains 97.47% of variance.
Feature Importance:
Top contributing features:
#Order
Store Type encodings
Region_Code encodings
Discount
Month / Day

This indicates that:
Demand volume (#Order) drives sales strongest
Store and region characteristics are key demand determinants
Discounts influence consumer behavior
Calendar effects matter

### Insights and Business Recommendation:
1. Discounts Work - Use Them Strategically
Since discounts significantly increase sales:
Schedule discount campaigns during low-demand periods
Use them to clear old inventory
Consider targeted store-level discounting (based on store type & region performance)

2. Holidays Do NOT Increase Sales for This Retailer
Holiday sales were lower than regular days:
Adjust staffing to avoid over-staffing on holidays
Reduce inventory buffers
Explore online promotions instead of in-store holiday campaigns

3. Store-Type-Specific Strategies
Since all store types significantly differ:
S4 stores → High inventory, aggressive promotions
S1 stores → Conservative stocking, efficiency-driven operations
S2 & S3 → Balance between volume and efficiency

4. Regional Forecasting Needed
Regions vary widely in performance:
R1 & R4 deserve priority allocation
R2 & R3 require targeted interventions:
localized marketing
product mix changes
competitive pricing adjustments

5. Predictive Model is Highly Accurate
With an R² of 0.9747, the model can be integrated into:
Weekly replenishment systems
Supply chain planning
Promotion planning
Demand forecasting dashboards

### Conclusion
This study provided a comprehensive, real-world demonstration of how data science can transform retail decision-making. By combining exploratory analysis, statistical hypothesis testing, machine learning, and deployment, we built an actionable forecasting system grounded in evidence.
The key learnings include:
Discounts significantly increase sales
Holidays unexpectedly reduce sales
Store type and region strongly affect performance
RandomForest delivered excellent predictive accuracy (R² ≈ 0.975)
Deployment ensured real-world usability

A system like this can help retail teams optimize inventory, reduce wastage, and maximize revenue - turning raw data into measurable business impact.