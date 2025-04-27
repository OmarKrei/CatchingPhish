# CatchPhish - An ML Approach to Catching Phishing URL's 
Author: Omar Kreidie
<br>Link to Dataset: https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset

## 1. Project Overview 
### Problem Area
Cybercrime is on an upwards trajectory and with Generative AI tools becoming readily accessible to anyone with an internet connection, it's only a matter of time before even the laziest of scammers start fooling us. It's not difficult to imagine that large corporations have the IT infrastructure and man power to protect their employees from cyber threats, but what about Small to Medium Businesses (SMB's)? According to a cyber crime study by Accenture, 43% of all cyberattacks are on SMB's and as stated by the World Economic Forum, 95% of all cyber breaches are attributed to human error [1]. 

So why don't we just get anti-virus & anti-malware security and call it a day? Well, security is like an onion, the more layers of security you have, the more protected you are. Common security suites like McAfee, Bitbolid, and Sentinal 1 are good for stopping many kinds of harmful attacks and react very well after mistakes where made, but what if we can avoid committing the mistake completely? This is where building a system that predicts whether a URL is legitimate or a phishing attempt provide immeasurable value. It's that extra layer of security that helps protect SMB's from total ruin. 
### Who's The Victim in All of This? 
As mentioned in my problem statement, SMB's are the most vulnerable and that is because of various factors like: 

- SMB's often avoid investing in effective security for many reasons. The most common reasons are, lack of education in the field, cost, and from my experience in the field, optimism bias [2].  
- Scammers often target SMB's because they are aware of the lack of security and also recognize that SMB's are incapable of reacting effectively after an attack has taken place [3].

### The Value Added 

The objective for this project is to build an ML model that can detect and classify phishing URL's. Given that URL's can be sent through various mediums like E-Mails, Text Messages, and, Social Networks. Building a model that can accurately decipher phishing from legitimate using only the URL, will add an extra layer of security to protect anyone from that costly human error. 

### The Data Science Solution

Relying on humans to classify phishing URL's is a losing battle, especially with how powerful and easy to use Generative AI models are becoming. E-mails, messages, and all forms of mediums in which you can receive a phishing URL will be replicated to astounding percision. That's why building a model that can classify phishing from legitimate is more crucial now than ever. 

In this project I will do the following: 
- Data Wrangling + Preliminary EDA: Clean the dataset, feature selection, and preliminary EDA.
- Data Pre-Processing and EDA: Hypothesis testing, Statistical analysis, and building a Logistic Regression model to help filter out the features. I am predicting that there will be a significant amount of collinearity.
- Predictive modeling: In this section, I will build models using Random Forest classification, XGBoost, and Neural Networks. Ideally, I can build a model with an accuracy range above 95%. 

## 2. Data Information + Dictionary
### Brief overview
The data was retrieved from [PHIUSIIL Phishing URL Dataset](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset). The dataset has 235,795 Rows and 56 Features. The target feature is the 'label' common which is binary. 0 = Phishing and 1 = Legitimate. The data is fairly evenly split, which avoids class imbalance, helping us build a stronger predictive model. there are 134850 Legitimate and 100945 Phishing URL's. 

### Full Data Dictionary
# Data Dictionary

| Column Name                  | Data Type  | Description |
|------------------------------|-----------|-------------|
| **FILENAME**                 | object    | Name of the file containing the URL. |
| **URL**                      | object    | The full URL being analyzed. |
| **URLLength**                | int64     | Length of the URL in characters. |
| **Domain**                   | object    | The domain name extracted from the URL. |
| **DomainLength**             | int64     | Length of the domain name. |
| **IsDomainIP**               | int64     | Indicator if the domain is an IP address (1 = Yes, 0 = No). |
| **TLD**                      | object    | The top-level domain (e.g., .com, .org). |
| **URLSimilarityIndex**       | float64   | Similarity score of the URL compared to known legitimate domains. |
| **CharContinuationRate**     | float64   | Measure of continuous character sequences in the URL. |
| **TLDLegitimateProb**        | float64   | Probability that the TLD belongs to a legitimate site. |
| **URLCharProb**              | float64   | Probability of character distribution in the URL being legitimate. |
| **TLDLength**                | int64     | Length of the top-level domain. |
| **NoOfSubDomain**            | int64     | Number of subdomains in the URL. |
| **HasObfuscation**           | int64     | Indicates if the URL contains obfuscation techniques (1 = Yes, 0 = No). |
| **NoOfObfuscatedChar**       | int64     | Number of obfuscated characters in the URL. |
| **ObfuscationRatio**         | float64   | Ratio of obfuscated characters in the URL. |
| **NoOfLettersInURL**         | int64     | Number of letters in the URL. |
| **LetterRatioInURL**         | float64   | Ratio of letters in the URL. |
| **NoOfDigitsInURL**          | int64     | Number of digits in the URL. |
| **DigitRatioInURL**          | float64   | Ratio of digits in the URL. |
| **NoOfEqualsInURL**          | int64     | Number of equal signs (=) in the URL. |
| **NoOfQMarkInURL**           | int64     | Number of question marks (?) in the URL. |
| **NoOfAmpersandInURL**       | int64     | Number of ampersands (&) in the URL. |
| **NoOfOtherSpecialCharsInURL** | int64   | Number of special characters in the URL. |
| **SpecialCharRatioInURL**    | float64   | Ratio of special characters in the URL. |
| **ISHTTPS**                  | int64     | Indicates if the URL uses HTTPS (1 = Yes, 0 = No). |
| **LineOfCode**               | int64     | Number of lines of code in the webpage source. |
| **LargestLineLength**        | int64     | Length of the longest line of code in the webpage source. |
| **HasTitle**                 | int64     | Indicates if the webpage has a title tag (1 = Yes, 0 = No). |
| **Title**                    | object    | The title of the webpage. |
| **DomainTitleMatchScore**    | float64   | Similarity score between the domain and webpage title. |
| **URLTitleMatchScore**       | float64   | Similarity score between the URL and webpage title. |
| **HasFavicon**               | int64     | Indicates if the webpage has a favicon (1 = Yes, 0 = No). |
| **Robots**                   | int64     | Indicates if the webpage has a robots.txt file (1 = Yes, 0 = No). |
| **IsResponsive**             | int64     | Indicates if the webpage is mobile-responsive (1 = Yes, 0 = No). |
| **NoOfURLRedirect**          | int64     | Number of times the URL redirects to another page. |
| **NoOfSelfRedirect**         | int64     | Number of times the URL redirects to itself. |
| **HasDescription**           | int64     | Indicates if the webpage has a meta description (1 = Yes, 0 = No). |
| **NoOfPopup**                | int64     | Number of popups found on the webpage. |
| **NoOfiFrame**               | int64     | Number of iframe elements in the webpage. |
| **HasExternalFormSubmit**    | int64     | Indicates if the page submits forms to an external site (1 = Yes, 0 = No). |
| **HasSocialNet**             | int64     | Indicates if the webpage contains social media links (1 = Yes, 0 = No). |
| **HasSubmitButton**          | int64     | Indicates if the webpage has a submit button (1 = Yes, 0 = No). |
| **HasHiddenFields**          | int64     | Indicates if the webpage contains hidden input fields (1 = Yes, 0 = No). |
| **HasPasswordField**         | int64     | Indicates if the webpage has a password input field (1 = Yes, 0 = No). |
| **Bank**                     | int64     | Indicates if the webpage contains banking-related terms (1 = Yes, 0 = No). |
| **Pay**                      | int64     | Indicates if the webpage contains payment-related terms (1 = Yes, 0 = No). |
| **Crypto**                   | int64     | Indicates if the webpage contains cryptocurrency-related terms (1 = Yes, 0 = No). |
| **HasCopyrightInfo**         | int64     | Indicates if the webpage includes copyright information (1 = Yes, 0 = No). |
| **NoOfImage**                | int64     | Number of images on the webpage. |
| **NoOfCSS**                  | int64     | Number of CSS files linked in the webpage. |
| **NoOfJS**                   | int64     | Number of JavaScript files linked in the webpage. |
| **NoOfSelfRef**              | int64     | Number of self-references in the webpage. |
| **NoOfEmptyRef**             | int64     | Number of empty references in the webpage. |
| **NoOfExternalRef**          | int64     | Number of external references in the webpage. |
| **label**                    | int64     | The classification label (e.g., 0 for legitimate, 1 for phishing). |

## 3. Project WorkFlow
### 1. Data Collection:
- Get a dataset: [PHIUSIIL Phishing URL Dataset](https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset)
- Load the data into Pandas and turn it into a DataFrame to begin analysis

### 2. Data Preprocessing/Wranglign + Preliminary EDA:
-  Handling missing values or duplicates if needed
-  Analyze data quality
-  Feature Engineering - Convert categorical data types to dummie variables where applicable 
-  Analyze relationships between features
-  Visualize patterns 

### 3. Full Exploratory Data Analysis (EDA) + Baseline Modeling: 
- More distributions and visualizations! 
- Hypothesis Testing - find which features have a statistically significant impact on the target variable 
- Explore and evaluate relationships between different features and target variable
- Build a preliminary Logistic Model 

### 4. Advanced Modeling:
Using these models because they are most useful for categorical classification 
- Refine Logistic Model 
- Build a Random Forest model because in a dataset with 56 features, Random Forest will allow me ot analyze feature importance
- Build an XGBoost model because it efficiently handles both numerical and categorical features
- Attempt to build a Neural Network 


## 4. Repository Navigation
### Notebooks

#### 1_DataWrangling + Prelim EDA

#### <br> References: 
[1] https://smallbiztrends.com/small-business-cybersecurity/
<br>[2] https://www.ibc.ca/news-insights/news/small-businesses-are-underestimating-their-cyber-risk-despite-increased-threats
<br>[3] https://www.forbes.com/sites/edwardsegal/2022/03/30/cyber-criminals/
