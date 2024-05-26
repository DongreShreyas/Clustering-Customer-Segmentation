# Customer Segmentation In Bank Customers

Customer segmentation involves grouping customers into specific marketing groups, perhaps narrowing them down by gender, interests, buying habits or demographic. The process requires a thought-out strategy, understanding how to manage and group your customers and which data you will use to do this. By differentiating their customer base, businesses can better target individuals and maximize sales, link-sell appropriately and provide more tailored shopping experiences. The aim of this project is to identify patterns followed by users, grouping them with other users with the same characteristics and discover which values of every feature identify that group. To be more specific, we will identify user types in credit card holders' data collected over 6 months.

# Project Process

The process followed by the project was:

Exploratory Data Analysis: Distribution and relation between features are studied. Also, missing values and repeated values are handled.
Cluster Analysis: The correct number of clusters is chosen using the WCSS and Silhouette score
Clustering Implementation: The customer segmentation is performed using K-Means algorithm.
Final Observations: The different type of users are described and final conclusions are made.
The final type of users found in the dataset were:

1.Type 1-(One off buyer): This is a common user type principally characterized by spending a lot of money in one go frequently.
2.Type 2-(Inactive user): They are not frequent users of the bank services.
3.Type 3-(Installment buyer): This type of users don't usually buy in one go, they usually have installment spendings instead.
4.Type 4-(Average user): They are completely analogous to type 1 users but they have lower balance and lower credit limit.
5.Type 5-(Responsible user): This type of user usually buys a few items rarely, also is characterized for using the payment in advance services frequently.
6.Type 6-(New users): These are low tenured users, they haven't done enough purchases in any way yet.
7.Type 7-(low active user): This is the most active kind of user.

Complete description is available at the Final Observations section

# Dataset Statistical Description

For better understanding consult the variable description table. Some inferences:

1.The average balance amount of users is $1,564 but this value is modified by the skewness caused by the highest balance amounts. A better is indicator is the median, that indicates $873.38 is the most approximate common balance amount among the credit card holders.
2.The balance frequency is high for most cases (for more than 75% of the the credit card holders). This means, for this particular set, the users are constantly receiving or spending money.
3.The number of purchases, again is affected by the skewness of high values. The normal amount of purchases made by credit card holders is 362 (median).
4.The credit card holders usually have bought at max. 38 items in one go (median).
5.The credit card holders usually have bought 89 items in installment purchases (median). At least 25% of the users don't buy installment purchases.
6.At least 75% of the credit card holders doesn't give any cash in advance
7.The purchase frequency is similar to balance frequency but doesn't take into account received money. 25% of the credit card holders has almost no purchase frequency meanwhile other 25% have a considerably high purchase frequency. The 50% remaining range between those two.
8.Purchases are not happening in one go.
9.Only a 25% of the credit card holders have a purchase installments high frequency.
10.Cash in advance is not being paid frequently for almost all credit card holders.
11.75% of the credit card holders have made less than 17 purchase transactions.
12.The credit limit for the credit card holders usually range between $3,000 and $3,600. The maximum credit limi tis $30,000 and the minimum credit limit is $50.
13.The most common range of amount of payments is between $380 and $1901
14.The percent of full payment paid by the user is near to 0 for the most cases.
15.25% of the users have been credit card holders for less than 12 months, on the other hand 75% have been credit card holders for 12 months.
16.For most of the variables we can see there is a skew to the right column, but for cases like PURCHASES_FREQUENCY or PURCHASES_INSTALLMENT_FREQUENCY are bimodal distributions, probably another mode can be considered. This is a first indicator of possible user types.


# Cluster analysis

Before performing the actual clustering, we will analyze how many clusters there are, in other words, how many user types are present in our dataset. For this project two different techniques were compared and analyzed in order to identify the right number of user types. By the way, there is not a definitive answer of number of clusters, there are multiple right choices according to how specific the user segmentations needs to be. We will try to be as specific as it is reasonable to be, for the number of users' type selection. The implemented techniques were:

Within clusters sum of squares (Elbow method): This technique measures the squared average distance of all the points within a cluster using the euclidean distance between a given point and the centroid to which it is assigned. As the number of clusters increases, it will always decrease the within sum of squares (WCSS). So we can use an large number of clusters in order to get a low value of WCSS but then the clusters will start to loose sense of what they represent. To determine the optimal number of clusters, we have to select the value of k at the “elbow” i.e. the point after which the distortion/inertia start decreasing in a linear fashion.

# Cluster implementation

Once we know the actual number of different type of users we have, the next step is to create every group and identify what characteristics can identify them better and what are the most common values in the feature set for that kind of user. Also, we will label all the user from the dataset using this characteristics. The main goal is to identify every user into its corresponding group according to the features or characteristics they have.

For grouping the user types we implemented the K-Means algorithm. K-Means is one of the most popular "clustering" algorithms. K-means stores 
centroids that it uses to define clusters. A point is considered to be in a particular cluster if it is closer to that cluster's centroid than any other centroid.
K-Means finds the best centroids by alternating betweenAssigning data points to clusters based on the current centroids.Choosing centroids (points which are the center of a cluster) based on the current assignment of data points to clusters.


# Conclusion
Finally, we conclude that there are 7 different type of users in the dataset that can be differentiated from each other according to their characteristics, these type of users are:

1.Type 1 (One off buyer): This is a common user type (about 20% of the total) principally characterized by spending a lot of money in one go frequently. They used to have a medium-high balance with a high credit limit that allow them to have this lifestyle. They usually don't use any cash in advance option.
2.Type 2 (Inactive user): One of the least common group (about 23%). They are frequent users of the bank services, they usually have high balances, high credit limit and buy using the bank services just a more times even though they have been clients for a while.
3.Type 3 (Installment buyer): This represents a really common active user type (about 13%). This type of users uses a lot the bank services similarly to the Type 1 users but with lower balance and lower credit limit. Another important aspect is that they don't usually buy in one go, they usually have installment spendings instead. They usually don't use any cash in advance option.
4.Type 4 (Average user): This is an average type of users, represents about the 18% of the total. They are completely analogous to type 1 users, the most important differences are that they have lower balance and lower credit limit, hence lower amount of purchases done and lower frequency. But the main difference is that type 1 users tend to have a high percent of full payment paid meanwhile this type of users have lower values.
5.Type 5 (Responsible user): This is the most common user type (about 10.2% of the total). This type of user usually buys a few items rarely, also is characterized for using the payment in advance services frequently.
6.Type 6 (New users): This is the least common user type (about 10% of the total). These are low tenured users, they haven't done enough purchases in any way yet, they have low credit limit and low payments. One important fact is that new users tend to pay in advance meanwhile users with longer tenure don't.
7.Type 7 (Low active user): This user represents about 6.5% of the total. This is the low active kind of user, they have the low balance among all types, they make a less of transactions, purchases and payments. They are also the less active users in all kinds of advance payments.

