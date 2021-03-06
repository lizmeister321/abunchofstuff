I've learned a LOT at my last few jobs.
There are a seemingly endless number of "Intro to Python" or "Ruby 101" resources, but some of these intermediate-level tasks can be a bit trickier.
This is a list of the tools and resources I've found especially helpful since I started logging all the things I've been learning back in February 2017.


**this page updated as needed. Last update 4/9/18**

# BOOKS:
* Many of the developers at my office work in **Scala**. I was having a really hard time trying to get started, since apparently no one in the Java or Scala community can remember a time when they were a beginner.
The book ["Programming in Scala"](https://www.amazon.com/Programming-Scala-Comprehensive-Step-Step/dp/0981531644) was written by the creator of Scala, and is (surprisingly) clear. 
  * There is also a [Coursera course](https://www.coursera.org/learn/progfun1) taught by the author, but don't be fooled, it is not an intro-level class.
It presumes that you have a full grasp of Scala syntax and functional programming, which is a very different way of working than Python and other object-oriented languages.

* **TensorFlow** is the new "It" tool in the Machine Learning community, so our CEO bought the team a copy of ["Hands-On Machine Learning with Scikit-Learn and TensorFlow"](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291).
I haven't finished the book yet, but it is very clear and concise, and is designed to have you coding along with the book as you go. Has all the instructions for setting up your working environment too, which is always handy. 

# ARTICLES:
* A core component of our product here relies on **Graph theory**, which I do not know at all. [This article](https://dev.to/vaidehijoshi/a-gentle-introduction-to-graph-theory) was a really clear jumping off point

* This isn't a technical article, but [Lauren Ancona's blog post](http://laurenancona.com/blog/illustration/everyones-been-winging-it-since-forever) will make you feel less alone on those days when you feel like you're the only one who doesn't get it. 

* One project I'm working on requires parsing XML from a website and storing it to later feed through our Natural Language Processing (NLP) program. [Alvin Alexander's blog](http://alvinalexander.com/source-code/scala-how-to-http-download-xml-rss-feed-timeout) had an easy-to-use setup to get going right away with parsing XML


# WEBSITES: 

* Despite doing a lot of address matchng work, I am pretty much garbage with **Regular Expressions**. This [series of web-based exercises](https://regexone.com/) was the closest I've come to actually understanding pattern strings.
You can jump around or work from Lesson 1 on, so it's a good tool for practicing/testing code as well.

* Another resource we work with regularly in my office is **MongoDB**, which is a "NoSQL" relational database. I have only worked in SQL environments before, so i'm watching [this series of Back to Basics videos provided by MongoDB](https://resources.mongodb.com/getting-started-with-mongodb/back-to-basics-1-introduction-to-nosql) to get up to speed.

* Recently, I discovered in trying to run a Jupyter Notebook on my work computer that Windows partitions its memory in an odd enough way that some data work isn't doable without a lot of effort. To that end, I set up an Amazon Web Services Elastic Cloud Computing (aka AWS EC2) instance to allow myself to process large sets of data in python. Figuring out how to launch the instance, connect, load the software, and get Jupyter notebooks running in the browser took a lot of reading, but I got it to work! [These](https://chrisalbon.com/aws/basics/run_project_jupyter_on_amazon_ec2/) [articles](https://medium.com/@alexjsanchez/python-3-notebooks-on-aws-ec2-in-15-mostly-easy-steps-2ec5e662c6c6) [were all](https://towardsdatascience.com/setting-up-and-using-jupyter-notebooks-on-aws-61a9648db6c5) [useful](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-python34-boto3/) [collectively](https://hackernoon.com/aws-ec2-part-3-installing-anaconda-on-ec2-linux-ubuntu-dbef0835818a) -- took a little from each to get the whole system up and running in the end. 
