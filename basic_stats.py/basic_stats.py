#!/usr/bin/env python
# coding: utf-8

# ## Script to calculate Basic Statistics

# # Equation for the mean:   $\mu_x = \sum_{i=1}^{N}\frac{x_i}{N}$
# 
# ### Equation for the standard deviation:  $\sigma_x = \sqrt{\sum_{i=1}^{N}\left(x_i - \mu \right)^2}\frac{1}{N-1}$
# 
# 
# **Instructions:**
# 
# **(1) Before you write code, write an algorithm that describes the sequence of steps you will take to compute the mean and standard deviation for your samples.  The algorithm can be written in pseudocode or as an itemized list.***
# 
# **(2) Use 'for' loops to help yourself compute the average and standard deviation.**
# 
# **(3) Use for loops and conditional operators to count the number of samples within $1\sigma$ of the mean.**
# 
# **Note:** It is not acceptable to use the pre-programmed routines for mean and st. dev., e.g. numpy.mean()

# ### Edit this box to write an algorithm for computing the mean and std. deviation.
# #### Algorithm to copmute the Mean: I will be breaking this down in three steps, input, process and output. 
# input: I will store all the elements(observations) of the list in a variable x. 
# 
# Process: I will create a counter then set it equal to zero, then use a for loop to iterate through the list and count the number of observations in the list. 
# After that, I will take the summation of the elements in the list and then divide that sum by the size of the list, N. 
# 
# Output: I will use a print function to print out the mean of x. 
# 
# 
# #### Algorithm to copmute the Std Deviation: I will be breaking this down in three steps, input, process and output.
# Input: I will store the mean of the list in a variable called mean_x and use it to compute std dev of x. 
# 
# Process: I will create a for loop to iterate through the list x, then create a new variable,diffsqrd, to store the difference between each element in the list and the mean, then square the difference. Then i will take the sum of all those numbers divide the sum by the mean and take the squareroot to get std dev. 
# 
# Output: I will use the print function to output the standard deviation 
# 
# ~~~
# 
# 
# 
# 
# 
# 
# ~~~

# ### Write your code using instructions in the cells below.

# # Put your Header information here.  Name, creation date, version, etc.
# # Sedat Touray
# ## September 23rd, 2020
# ### Geo 404
# #### Basic Stats 
# 

# In[1]:


# Import the matplotlib module here.  No other modules should be used.
import matplotlib.pyplot as plt 


# In[2]:


# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
# This will be your sample.
#for my sample i created a list called a_list to store the elements 
data = [1,2,3,4,5,6,7,8,9,15,11,23,67,12,18,32,45,7,8,17,87,21,34,64,24]


# In[3]:


# Pretend you do not know how long x is; compute it's length, N, without using functions or modules.
#since we are using my sample, I assigned my variable a new name, x. 

#set the counter x_len to 0
n = 0 
#using the for loop to iterate through the list 
for i in data:
    #Get counts of each element
    n= len(data)
#output the results using the print statement     
print("The lenght ,N, of x is: " + str(n))


# In[4]:


# Compute the mean of the elements in list x.
#set the counter x_len to 0
total = 0.0
#using the for loop to iterate through the list 
for i in data:
    #Get counts of each element
    total += i
    #get mean by dividing total by the lenght of the list
    mean = total / n
#output the results using the print statement     

print(mean)





# In[6]:


# Compute the std deviation, using the mean and the elements in list x.
sum_diffsqrd = 0
diffsqrd = 0
std_list = []
for i in range(len(data)):
    diffsqrd = (data[i]-mean)**2
    std_list.append(diffsqrd)
for i in range(len(std_list)):    
    sum_diffsqrd = sum_diffsqrd + std_list[i]
    stddev = ((sum_diffsqrd)/n)**(0.5)
print(stddev)


# In[8]:


# Use the 'print' command to report the values of average (mu) and std. dev. (sigma).
print(("The Mean value ") + ("\u03bc ") + "is " + str(mean))
print("The Standard Deviation " + ("\u03C3 ") + "is " + str(stddev))



# In[11]:


# Count the number of values that are within +/- 1 std. deviation of the mean.  
# A normal distribution /will have approx. 68% of the values within this range.  
# Based on this criteria is the list normally distributed?
def err(n):
    n = 0
    n = n + 1 or n - 1
    for i in range(int(mean)):
    
        return n     

err(n)    
    



# In[12]:


# Use print() and if statements to report a message about whether the data is normally distributed.
print("The data for x is not evenly distributed because only 4% of the values are within this range, so therefore, it is Skewed to the right. ")


# In[15]:


### Use Matplotlb.pyplot to make a histogram of x.
plt.hist(data, bins=25 )
#give appropriate title and labels 
plt.title("The histogram of x")
plt.ylabel("Frequency")
plt.xlabel("elements of x")
#display the histogram
plt.grid()
plt.show(data)


# ### OCG 593 students, look up an equation for Skewness and write code to compute the skewness. 
# #### Compute the skewness and report whether the sample is normally distributed.

# In[ ]:




