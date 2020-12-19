## Automated Machine Learning with Model Deployment

This project is an example of how I am able to take an input dataset and create a fully functional machine learning model that can predict future success that is accessible via an http endpoint.  This specific model highlights a bank marketing dataset and tries to predict whether the potential client will use the bank's services based on training data from past experience.  The project began with just a standard csv file, and used Automated Machine Learning (AutoML) a fairly accurate model was derived using DevOps techniques from a Python script that can be duplicated for other datasets with little effort.  The model is then published to Azure as an endpoint that can be used from an service that can generate an http request.  I also used Apache Benchmark to load test the endpoint.

## Architectural Diagram
![Key Steps Diagram](KeyStepsDiagram.png)

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 
The first step is to set up a method of authentication to use for the scripts so that the automation can run without user intervention.
![Authentication Creation](Udacity-sp-created.png)
Once everything is set up the data needs to be uploaded and registered in Azure.  A profile may also be generated to help identify possible areas of improvement.
![Bank Marketing Dataset in Azure](Bank%20Marketing%20dataset.png)
The dataset can be uploaded as part of the initial Automated ML run, or chosen later.  
Once the initial run has been completed, the run can be automated using the Python SDK
The scripts can be configured to show the run details.
![Run Details Widget](Run%20Details%20Widget%20output.png)
The experiment and pipeline will be shown in Azure ML Studio
![Experiment Complete](SDK%20Experiment%20Complete.png)
Automated ML will give the best model based on the settings chosen
![Best Model](Best%20Model%20Explanation.png)
After the best model is obtained, it needs to be published.
![Endpoint With Application Insights enabled](Endpoint%20With%20App%20Insights.png)
The published model can then have logs saved to Application Insights.  The logs can be access either programmatically or through Azure.
![Logs output](logs.py%20output.png)
The model can then be run by hitting an http endpoint whenever needed to get an estimate.


## Screen Recording
https://youtu.be/IBKF7ZX60Rw

## Standout Suggestions
I ran the processes locally using a personal Azure workspace to make sure that I could set up an entire environment and understand the dependencies involved.  I also installed and used Apache Benchmark to load test the resulting endpoint, which can give key metrics as to the health and viability of a model.

![Benchmarking Results](benchmark%20endpoint.png)

## Ideas for Improvement
Using a larger dataset and turning on Deep Learning could give a better model result.  Additional model steps could be added to parallelize model preparation if there were other steps that needed to be taken to process the data, especially if there was more data.