

```python
# Dependencies
import pandas as pd
import os
import json
```


```python
#reading the data
data_file = os.path.join("HeroesOfPymoli", "purchase_data2.json")
data_file

```




    'HeroesOfPymoli\\purchase_data2.json'




```python
data_json = pd.read_json(data_file)
#with open(data_file) as input_file:
   # data = json.load(input_file)
```


```python
data_df = pd.DataFrame(data_json)
#data_df.to_csv("purchase_data_cleaned.xls")
data_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Iloni35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>12</td>
      <td>Dawne</td>
      <td>3.36</td>
      <td>Aidaira26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>Male</td>
      <td>5</td>
      <td>Putrid Fan</td>
      <td>2.63</td>
      <td>Irim47</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>2.55</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>Philodil43</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8</td>
      <td>Male</td>
      <td>8</td>
      <td>Purgatory, Gem of Regret</td>
      <td>2.22</td>
      <td>Hainaria90</td>
    </tr>
    <tr>
      <th>6</th>
      <td>40</td>
      <td>Male</td>
      <td>148</td>
      <td>Warmonger, Gift of Suffering's End</td>
      <td>4.65</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>7</th>
      <td>28</td>
      <td>Male</td>
      <td>27</td>
      <td>Riddle, Tribute of Ended Dreams</td>
      <td>3.38</td>
      <td>Undirra90</td>
    </tr>
    <tr>
      <th>8</th>
      <td>18</td>
      <td>Male</td>
      <td>111</td>
      <td>Misery's End</td>
      <td>1.79</td>
      <td>Eolideu96</td>
    </tr>
    <tr>
      <th>9</th>
      <td>36</td>
      <td>Male</td>
      <td>139</td>
      <td>Mercy, Katana of Dismay</td>
      <td>4.25</td>
      <td>Aesurstilis64</td>
    </tr>
  </tbody>
</table>
</div>



## Player Counts


```python

#Total Number of Players
total_players = data_df['SN'].nunique()

#Number of Unique Items
unique_items = data_df['Item ID'].nunique()

#Average Purchase Price
average_price = data_df['Price'].mean()

#Total Number of Purchases
number_of_purchases = len(data_df.index)

#Total Revenue
total_revenue = (data_df['Price'].sum())


player_count = pd.DataFrame({"Total Number of Players":[total_players],"Number of Unique Items":[unique_items],
                             "Average Price":[average_price],"Number of Purchases":[number_of_purchases],"Total Revenue":
                            [total_revenue]})

player_count['Total Revenue'] = player_count['Total Revenue'].map("${0:,.2f}".format)
player_count['Average Price'] = player_count['Average Price'].map("${0:,.2f}".format)

player_count = player_count[['Total Number of Players','Number of Unique Items','Average Price', 'Number of Purchases'
       , 'Total Revenue']]
      
                                                             
player_count
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Number of Players</th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>74</td>
      <td>64</td>
      <td>$2.92</td>
      <td>78</td>
      <td>$228.10</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics


```python
unique_player_count = data_df.groupby('Gender')['SN'].nunique()
percent_of_players = unique_player_count*100/total_players

summ_tab = pd.DataFrame({"Total Count":unique_player_count,"Percentage of Players":percent_of_players})
#adding % symbol
summ_tab["Percentage of Players"] = summ_tab["Percentage of Players"].map("{0:,.2f}%".format)
summ_tab.head()


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>17.57%</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>81.08%</td>
      <td>60</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.35%</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Purchase Analysis


```python

purchase_count = data_df.groupby('Gender')['Item ID'].count()
average_purchase_price = data_df.groupby('Gender')['Price'].mean()
total_purchase_value = data_df.groupby('Gender')['Price'].sum()
normalized_total = total_purchase_value/purchase_count


purchase_analysis = pd.DataFrame({"Purchase Count":purchase_count,"Average Purchase Price":average_purchase_price,
                                 "Total Purchase Value":total_purchase_value,"Normalized Totals":normalized_total
                                 })
purchase_analysis = purchase_analysis[["Purchase Count","Average Purchase Price","Total Purchase Value","Normalized Totals"]]

#Adding Formatting

purchase_analysis["Average Purchase Price"]= purchase_analysis["Average Purchase Price"].map("${0:,.2f}".format)
purchase_analysis["Total Purchase Value"]= purchase_analysis["Total Purchase Value"].map("${0:,.2f}".format)
purchase_analysis["Normalized Totals"]= purchase_analysis["Normalized Totals"].map("${0:,.2f}".format)
purchase_analysis


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>13</td>
      <td>$3.18</td>
      <td>$41.38</td>
      <td>$3.18</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>64</td>
      <td>$2.88</td>
      <td>$184.60</td>
      <td>$2.88</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1</td>
      <td>$2.12</td>
      <td>$2.12</td>
      <td>$2.12</td>
    </tr>
  </tbody>
</table>
</div>



## Setting Bins


```python

#The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)

hp_bins = [1,10,14,19,24,29,34,39,100]
labels = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
pd.cut(data_df['Age'],hp_bins,labels = labels)
data_df['Age Bins'] = pd.cut(data_df['Age'],hp_bins,labels = labels)
data_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Bins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Iloni35</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>12</td>
      <td>Dawne</td>
      <td>3.36</td>
      <td>Aidaira26</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>17</td>
      <td>Male</td>
      <td>5</td>
      <td>Putrid Fan</td>
      <td>2.63</td>
      <td>Irim47</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>Male</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>2.55</td>
      <td>Irith83</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22</td>
      <td>Male</td>
      <td>154</td>
      <td>Feral Katana</td>
      <td>4.11</td>
      <td>Philodil43</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics


```python
age_player_count = data_df.groupby('Age Bins')['SN'].nunique()
age_percent_of_players = (age_player_count*100/total_players)

age_summ_tab = pd.DataFrame({"Total Count":age_player_count,"Percentage of Players":age_percent_of_players})
#adding % symbol
#age_summ_tab["Percentage of Players"] = summ_tab["Percentage of Players"].map("{0:,.2f}%".format)
age_summ_tab

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Age Bins</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>6.756757</td>
      <td>5</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.054054</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>14.864865</td>
      <td>11</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.945946</td>
      <td>34</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>10.810811</td>
      <td>8</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.108108</td>
      <td>6</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>8.108108</td>
      <td>6</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.351351</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)


```python
age_purchase_count = data_df.groupby('Age Bins')['Item ID'].count()
age_average_purchase_price = data_df.groupby('Age Bins')['Price'].mean()
age_total_purchase_value = data_df.groupby('Age Bins')['Price'].sum()
age_normalized_total = age_total_purchase_value/age_purchase_count

age_purchase_analysis = pd.DataFrame({"Purchase Count":age_purchase_count,"Average Purchase Price":age_average_purchase_price,
                                 "Total Purchase Value":age_total_purchase_value,"Normalized Totals":age_normalized_total
                                 })
age_purchase_analysis = age_purchase_analysis[["Purchase Count","Average Purchase Price","Total Purchase Value","Normalized Totals"]]

age_purchase_analysis["Average Purchase Price"]= age_purchase_analysis["Average Purchase Price"].map("${0:,.2f}".format)
age_purchase_analysis["Total Purchase Value"]= age_purchase_analysis["Total Purchase Value"].map("${0:,.2f}".format)
age_purchase_analysis["Normalized Totals"]= age_purchase_analysis["Normalized Totals"].map("${0:,.2f}".format)
age_purchase_analysis

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Bins</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>5</td>
      <td>$2.76</td>
      <td>$13.82</td>
      <td>$2.76</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>3</td>
      <td>$2.99</td>
      <td>$8.96</td>
      <td>$2.99</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>11</td>
      <td>$2.76</td>
      <td>$30.41</td>
      <td>$2.76</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>36</td>
      <td>$3.02</td>
      <td>$108.89</td>
      <td>$3.02</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>9</td>
      <td>$2.90</td>
      <td>$26.11</td>
      <td>$2.90</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>7</td>
      <td>$1.98</td>
      <td>$13.89</td>
      <td>$1.98</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>6</td>
      <td>$3.56</td>
      <td>$21.37</td>
      <td>$3.56</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1</td>
      <td>$4.65</td>
      <td>$4.65</td>
      <td>$4.65</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders


```python
sn_purchase_count = data_df.groupby('SN')['Item ID'].count()
sn_average_purchase_price = data_df.groupby('SN')['Price'].mean()
sn_total_purchase_value = data_df.groupby('SN')['Price'].sum()
sn_normalized_total = sn_total_purchase_value/sn_purchase_count

sn_purchase_analysis = pd.DataFrame({"Purchase Count":sn_purchase_count,"Average Purchase Price":sn_average_purchase_price,
                                 "Total Purchase Value":sn_total_purchase_value,"Normalized Totals":sn_normalized_total
                                 })
sn_purchase_analysis = sn_purchase_analysis[["Purchase Count","Average Purchase Price","Total Purchase Value","Normalized Totals"]]

sn_purchase_analysis["Average Purchase Price"]= sn_purchase_analysis["Average Purchase Price"].map("${0:,.2f}".format)
sn_purchase_analysis["Total Purchase Value"]= sn_purchase_analysis["Total Purchase Value"].map("${0:,.2f}".format)
sn_purchase_analysis["Normalized Totals"]= sn_purchase_analysis["Normalized Totals"].map("${0:,.2f}".format)
sn_purchase_analysis.sort_values("Total Purchase Value",ascending = False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Sundaky74</th>
      <td>2</td>
      <td>$3.71</td>
      <td>$7.41</td>
      <td>$3.71</td>
    </tr>
    <tr>
      <th>Aidaira26</th>
      <td>2</td>
      <td>$2.56</td>
      <td>$5.13</td>
      <td>$2.56</td>
    </tr>
    <tr>
      <th>Eusty71</th>
      <td>1</td>
      <td>$4.81</td>
      <td>$4.81</td>
      <td>$4.81</td>
    </tr>
    <tr>
      <th>Chanirra64</th>
      <td>1</td>
      <td>$4.78</td>
      <td>$4.78</td>
      <td>$4.78</td>
    </tr>
    <tr>
      <th>Alarap40</th>
      <td>1</td>
      <td>$4.71</td>
      <td>$4.71</td>
      <td>$4.71</td>
    </tr>
  </tbody>
</table>
</div>



## Identify the 5 most popular items by purchase count, then list (in a table):


```python
item_purchase_count = data_df.groupby(['Item ID','Item Name'])['Item ID'].count()
item_purchase_count
#item_average_purchase_price = data_df.groupby(['Item ID','Item Name'])['Price'].mean()
item_price = data_df.groupby(['Item ID','Item Name'])['Price'].max()
item_total_purchase_value = data_df.groupby(['Item ID','Item Name'])['Price'].sum()
item_normalized_total = item_total_purchase_value/item_purchase_count

item_purchase_analysis = pd.DataFrame({"Purchase Count":item_purchase_count,"Item Price":item_price,
                                 "Total Purchase Value":item_total_purchase_value
                                 })
item_purchase_analysis = item_purchase_analysis[["Purchase Count","Item Price","Total Purchase Value"]]

#item_purchase_analysis["Item Price"]= item_purchase_analysis["Item Price"].map("${0:,.2f}".format)
item_purchase_analysis["Total Purchase Value"]= item_purchase_analysis["Total Purchase Value"].map("${0:,.2f}".format)
#item_purchase_analysis["Normalized Totals"]= item_purchase_analysis["Normalized Totals"].map("${0:,.2f}".format)
item_purchase_analysis.sort_values("Purchase Count",ascending = False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>94</th>
      <th>Mourning Blade</th>
      <td>3</td>
      <td>3.64</td>
      <td>$10.92</td>
    </tr>
    <tr>
      <th>90</th>
      <th>Betrayer</th>
      <td>2</td>
      <td>4.12</td>
      <td>$8.24</td>
    </tr>
    <tr>
      <th>111</th>
      <th>Misery's End</th>
      <td>2</td>
      <td>1.79</td>
      <td>$3.58</td>
    </tr>
    <tr>
      <th>64</th>
      <th>Fusion Pummel</th>
      <td>2</td>
      <td>2.42</td>
      <td>$4.84</td>
    </tr>
    <tr>
      <th>154</th>
      <th>Feral Katana</th>
      <td>2</td>
      <td>4.11</td>
      <td>$8.22</td>
    </tr>
  </tbody>
</table>
</div>



## Identify the 5 most profitable items by total purchase value, then list (in a table):


```python
item_purchase_analysis.sort_values(["Total Purchase Value","Item Price"],ascending = False).head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>117</th>
      <th>Heartstriker, Legacy of the Light</th>
      <td>2</td>
      <td>4.71</td>
      <td>$9.42</td>
    </tr>
    <tr>
      <th>93</th>
      <th>Apocalyptic Battlescythe</th>
      <td>2</td>
      <td>4.49</td>
      <td>$8.98</td>
    </tr>
    <tr>
      <th>90</th>
      <th>Betrayer</th>
      <td>2</td>
      <td>4.12</td>
      <td>$8.24</td>
    </tr>
    <tr>
      <th>154</th>
      <th>Feral Katana</th>
      <td>2</td>
      <td>4.11</td>
      <td>$8.22</td>
    </tr>
    <tr>
      <th>180</th>
      <th>Stormcaller</th>
      <td>2</td>
      <td>2.77</td>
      <td>$5.54</td>
    </tr>
  </tbody>
</table>
</div>


