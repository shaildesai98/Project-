Group 4

# Project Title: Chicago Rideshare & Taxi Service Analysis

### Proposal Questions:
Which community areas have the highest ride services demand?
What is the relationship between fairs and tips over the span of the time selected and in general?
What is the average fare & tip amount per service?
How does ride service demand change over the months of the year?

### Group Members:
Giles, Timothy
Dunn, Thomas
Miller, Jason
Ortiz, Vanessa
Pineda, Luis Andres
Desa, Shail



We run the Astros Taxi Company in Chicago, IL.
Our business has been struggling with maintaining business due to the explosion in popularity of ride share apps across large cities, including Chicago.
The City of Chicago tracks Taxi and Transportation Network Providers  (“ride share”) data. Each row in the datasets represents one individual trip, containing info like timestamp, trip miles, fair, tips, etc.
The data is uploaded to the Chicago Data Portal, which is what was used for API call. 
Additionally, we pulled a “Chicago” data set from GeoDataSets to create a map of Chicago. GeoDataSets was downloaded into the conda environment and included as dependency in the code.
We encountered an issue with calling the data and were able to resolve it by downloading the data as a CSV file and taking randomized samples. We ended up downloading the 18 GB CSV file for the TNP data and taking a random sample of 350,000 rows out of the 69 million. To maintain the correct size relationship we also took a random sample of 32,000 rows of the taxi data.




### Ride trends by Community Areas

The city of Chicago is divided by Community Areas for urban planning. For this project, we were able to pull a data set of Chicago which includes the name of the community area, the Number ID, and the population for that area from both the 2010 and 2000 Census. Our hypothesis was that areas with higher populations would have a higher amount of rides as there would be more customers to order rides. A heat map was more appropriate for this analysis as placing taxis is geography dependent. We can’t pick the community areas to focus on purely based on the stats as it is possible that the best performing community areas are not next to each other, and therefore wouldn’t make sense to try to group drivers that way.
 For the most part, our assumption was correct. A pretty obvious exception was the Austin Community Area, which despite having the highest population in the Chicago city limits, had one of the lowest number of total rides. Conversely, the O’hare community area had one of the highest pick up rates despite having a low population. This is mostly due to Chicago O’Hare’s airport being present in the O’Hare community area. 



### Average Fare and Tip Amounts per Service Over Time

Using Rideshare and Taxi data from the Chicago Data Portal, we were able to analyze the average fare and tip amounts for Rideshare and Taxi services over the entire year of 2022. Our hypothesis was that Taxi services would be charging higher fares over time as they are used less frequently and have a higher overhead cost than rideshare companies. It was determined that rideshare services had a higher overall increase in average fare compared to taxi services.
For average tip amounts over time, our hypothesis was that rideshare services had higher tip amounts on average over time. It was found that taxi services actually have a higher average tip amount over each month, however, it could be inferred that ride share services have a more steady increase over time.



### Correlation Between Average Fare and Average Tip Amount Per Service

For statistical analysis, a Pearson Test was conducted to examine the correlation between average fare amounts and tip amounts per service. The Pearson correlation test was used to measure linear correlation between two variables, in this case Fare amount and Tip amount per service.
For Ride Share, the correlation coefficient is 0.843 (approximately), which indicates a strong positive correlation between the average fare and the average tip. The p-value is about 0.000575, which is less than 0.05, a common threshold for statistical significance. This suggests that the observed correlation is statistically significant, and it's very unlikely that it's due to chance. You would reject the null hypothesis of no correlation between the average fare and average tip for rideshare.
For taxis, the correlation coefficient is 0.703 (approximately), which indicates a moderate positive correlation between the average fare and the average tip. The p-value is about 0.01082, which is also less than 0.05, indicating that the observed correlation is statistically significant, and it's unlikely that it's due to chance. You would also reject the null hypothesis of no correlation between the average fare and average tip for Taxi.



### Average Trip Length and Speed

There is a slight difference in average speed with rideshares averaging 17.68 mph and taxis averaging 14.78 mph. Sundays, the fastest day, averages 2 - 3 mph faster than Saturdays, the slowest day.
The average trip for rideshare services was 5.18 miles and the average for taxi services was 5.4 miles, so there isn’t much difference between the average trip length. When looking at the distribution of trip lengths for both there is a noticeable bump at the 20 mile mark. It’s even larger in the taxi data, showing that out of the longer trips there are more clustered around the 20 mile mark that favors the taxi rides. Downtown Chicago is also a 20 mile trip from the airport, which suggests that there may be a higher chance of getting a cab over a rideshare from the airport compared to other areas.



### Rideshare & Taxi Demand throughout the year

Based on our analysis rideshare is by far the most popular method of transportation. And demand for ride share is way more compared to taxis. 
Furthermore, there is no correlation between months and the total of trips per month. The one difference I found is in the first 2 months, which barely crosses 20000 rides. But after the 2nd month the total amount rides go up by an average of 25000 rides. For the rest of the year, there is no significant difference. 
Surprisingly, there was no difference between the number of taxi rides per month. There is a very slight gradual increase as the year goes by. 

