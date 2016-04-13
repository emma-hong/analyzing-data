# Analyzing Data: NETS213 Homework 9 
Contributors: Molly Wang and Emma Hong

<b>dedupe-data-code.gz</b>: contains de-duplicated data and code to dedupe the original data

### Replicating Charts 

<b>how_graph.html</b>: html file for reproducing pie chart of gun types

<b>guntype_pie.py</b>: code for getting the data for the pie chart of gun types, input is the json file with deduped data

![Breakdown of fatal and nonfatal shootings by type of gun] (https://github.com/emma-hong/analyzing-data/blob/master/figures/how_pie.png)

<b>when_line.py</b>: code for getting the data for the line graph of time of day to gun-violence incidents (divided up by fatal/non-fatal), input is json file with deduped data

<b>when_graph.html</b>: html file for reproducing line graph of time of day to gun-violence incidents (divided up by fatal/non-fatal)

![Breakdown of incidents of gun-violence by hour](https://github.com/emma-hong/analyzing-data/blob/master/figures/when_line.png)
What's interesting is that most gun-violence incidents seem to occur during the day around 9AM. I expected more gun violence incidents to occur overnight. This expectation may have stemmed from the many movies I've watched where seedy underground activities and mobgang meetings that end in shootouts occur in the wee hours of the morning. I also expected less variation across the different hours in the day than is currently exhibited. There seems to be a wide range in the difference of gun-violence incidents from hour to hour.

### Creating New Charts 

<b>domestic_violence.html</b>: html file for creating a bar chart showing victims of domestic gun violence and the breakdown of male and female victims by age group 

<b>domestic_violence.py</b>: code for getting the data on gun violence cases marked as domestic violence, then from those, collecting data on the gender of victims and their ages

![Breakdown of domestic violence victims by age and gender] (https://github.com/emma-hong/analyzing-data/blob/master/figures/domestic_violence.png)

<b>suicide-pie.py</b>: code for getting all incidents of suicides by gun and the breakdown by gender and age

<b>suicide-py.html</b>: html file for pie graph representation of the brekadown of suicides by gun by gender and age and a diff pie graph contrasting male and female suicides

![Breakdown of suicides by age and gender](https://github.com/emma-hong/analyzing-data/blob/master/figures/suicide-pi.png)
I feel the data represented here is in line with my expectations. Suicide occurs at a much higher rate among females than males. Furthermore, the greatest age range in which these suicides occur is among the middle-aged. A potential reason for suicide is depression. About six million people are affected by late life depression, but only 10% ever receive treatment. (Brown University Long Term Care Quarterly, 1997) Furthermore, statistics have supported that women experience depression at twice the rate of men. This 2:1 ratio exists regardless of racial or ethnic background or economic status. The lifetime prevalence of major depression is 20-26% for women and 8-12% for men. (Journal of the American Medical Association, 1996). The data represented by the graph here supports these statistics.

![Suicides by gender](https://github.com/emma-hong/analyzing-data/blob/master/suicide-bar.png)
While the number of gun-related suicides here don't have that 2:1 ratio between female and male, it is noteworthy that there are significantly more gun-related suicides among females than males since males own more firearms. Similarly, suicides via other methods are more common (i.e. overdoses), and therefore this graph should not be taken be an indication that this sample data doesn't accurately represent that of the population.
