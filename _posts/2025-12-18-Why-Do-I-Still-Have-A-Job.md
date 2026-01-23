---
title: Why do I still have a Job? 
description: Because everything is still done in Email and Excel. A long somewhat coherent rant. On AI, LLMs, and Structured Data.
date: 2025-10-23 05:00:00 -0500
categories: [post]
tags: [data, automation, structured-data, ai, work]
pin: false
math: true
mermaid: true
image: assets/2025-12-18-Why-Do-I-Still-Have-A-Job.jpg
---
In around 2023 I first started working on a project utilizing [MegaDetector](https://github.com/agentmorris/MegaDetector) (now [Pytorch-Wildlife](https://microsoft.github.io/CameraTraps/)) that came about when I was trying to automate my animal classification and labeling job using image detection models as a research assistant. In that time I came across a book simply titled "Reproducible Analysis with R". In section 6.4 there is simple an image titled ["Multiple Tables" ](https://nceas.github.io/sasap-training/materials/reproducible_research_in_r_fairbanks/images/excel-org-02.png). It pictures one of the easiest ways that data can become unorganized - that there are different observations or pieces of data within the same row. This problem of course is relatively easy to fix if you put them into separate tables. However, this "fix" compounds over time as more imperfections take place, making it difficult to analyze or visualize the data. 

Before I go in further, I'm going to make conflicting opinions because I hold the two foundational beliefs in regard to AI, LLMs, and Automation and why people will still have jobs in the coming future.

1. When data is organized, there is little need for human labor. I fully believe most business task can be automated when data is structured.
2. Current LLM (called "AI", even when it's not) systems, even with error correction practices and continuous improvement have to interface with the imperfect data formats that currently are solved in closed environments. Muddy data can never be cleaned without proper context.

Right now, the current work infrastructure is based in some conjunction of a messaging platform (email, teams) + software specific task management (Reconciliation application, tax application) + a project management platform (such as Jira, Ticket System). There have been attempts to broach this of course with the advent of Enterprise-Resource-Planning (ERP) systems. ERP systems reduce the problem of data silos by combining multiple business operations pipelines into a structured format. However, if there is ever a user error in either using the system or trying to not use the system (such as downloading the data to excel) then the purpose is lost. 

When I read about the concept of ["management execution apps"](https://fourminutebooks.com/a-world-without-email-summary/) from Cal Newport's book "A World Without Email" it made complete sense to me why currently a majority of hand-off task are still inefficient. In my current company we call this an "end-to-end business process" and in the broader broad of computer science a "data pipeline. They are inefficient because there is a lack of clarity and structure. Much of my current jobs, and many out there, are making sure that you're pinging people enough times through email until they respond with the email that you need.

In Derek Thompson's podcast 'Plain English' there was an idea that came up of "Emptying email inbox as a competency of AGI". I think this is an extremely inefficient and incorrect way to think about the future of AGI and job replacement with the context of ["Live in the future, then build what's missing" from Paul Graham](https://paulgraham.com/startupideas.html). By using a metric of email - We are solving today's problems, not building tomorrow's solution.

To give an example of this - the RSS/Atom Feed. There is a plethora of reasons why it was not widely adopted. (such as not being able to collect information about who subscribes to a feed, aka data collection instead of privacy). But it is a dramatically more energy friendly way to post content to followers than newsletters, that require you to send an email individually to each subscriber.

>**The Newsletter solved today's problems, RSS built tomorrow's solution.**

>**LLMs/AI solve today's problem. Structured data builds tomorrow's solutions**

For the area I live in of Hampton roads there are collection of RSS feed and Newsletter's to know what's going to happen in the area. You can use an LLM to organize this data. [For example - the project I'm currently working on at-least has 20+ sources that I'm pulling from.]. However, it would have been much easier for me if everything was an RSS feed so I wouldn't have to HTTPS scrape a website individually for their blog post and updates.

Then I came across [ai-2027](https://ai-2027.com/) that "predict[s] that the impact of superhuman AI over the next decade will be enormous, exceeding that of the Industrial Revolution. This raised an eyebrow for me.

For those that have any experience with power automate, n8n, Zapier, IFTTT, Decisions.ai there are many finite and specific pieces at play that make a workflow either succeed or fail. A huge portion of that is error correction and decisions trees. When I was recently trying to make my own process, I came upon a very particular problem. When I was parsing an HTML document to get a string of characters for my URL link. Every single time through an LLM model it would mess up the link and change it up even with variability set to zero. I ultimately gave up because the marginal benefit was not there when a model was able to efficiently pull all other information and links. 

To say again: **LLMs/AI solve today's problem. Structured data builds tomorrow's solutions**

* Why don't we have a fully auditable government? Because of Data Silos
* Why do I still have a job? Because of data silos, unorganized data, and limited business structurization relative to what is needed for automation
* Why don't we have a unified healthcare information system? Because of Data Silos and Political Factors
* In essence, why don't we have XYZ when it comes to unification of a system? Because there is a massive infrastructure, cultural, and monetary cost associated with change.

So, what exactly do I mean by structured data? Going back to the beginning of the article there is a different between data being structured and data being organized. The easiest way to think about it is bring the mindset of "can I make this into a digital form that people can enter information into". 

* Grouping the M&M candy by color is organized
* Labeling each M&M candy by Unique ID, assigning them a color, giving a date and time labeled, unique position in color category, person assigned to eat candy, person candy was bought from, candy expiration date, list of ingredients in candy, is structured

I found a quote on reddit which adds to this sentiment of why ["Everything is a Graph"](https://www.reddit.com/r/programmingcirclejerk/comments/k1p7fb/im_not_a_good_programmer_but_i_can_say_very/): 
>Everything is literally a graph.
>
>When you dereference a pointer, the instruction doing the dereference is your source node. The address is your edge. The memory it's pointing to is the destination node.
>
>Whether or not the memory is cached and retrievable without going into main memory is determined by, you guessed it, a graph.
>
>Everything is a graph.
>
> Your process is connected to a process tree - a graph. It gets allocated a time slice, and is then scheduled by your OS. The scheduler stores information as a graph.
> 
> Everything is a graph.
>
> When you go to Google, you perform a DNS lookup first. The closest DNS server that's available is a node adjacent to your network whose edge contains the least weight among all the other nodes.
>
> Everything is a graph.
> When you parse user input, you're creating an FSM to tokenize the information. Each state is a node. Each transition is an edge.
>
> Everything is a graph.

The world in which my job is replace is that in which data is structured not organized. My email can already be organized by rules or an LLM system, but neither is going to solve the work tasks that needs to be done because there is an underlying structure that is not contained within the email file. I have a bias towards information systems because an introduction of an unstructured form like a person or LLM model can introduce untended consequences within that defined system. And even then, there are technologies coming out that can interact with your operating system and applications. So, it's not that hard to imagine an autonomous agent replacing that work task. But again - it's solving today's problems, not building tomorrow's solutions. If there is ever a change in the business process, there will have to be a reprogramming in how an agent will handle the input data. By driving change at the input level, you completely eliminate the need to an agent to exist.

Sometime this isn't the case. We have technology such as self-driving cars that are increasing in capability with Waymo cars now being in 10 cities it's a future into a world of less accident-prone commutes. So, all we have to do is wait if I'm wrong. And well...get paid to do some work.
