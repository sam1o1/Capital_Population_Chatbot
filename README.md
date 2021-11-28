# **Capital&Population Finder** 
## Table of Content:

 - [Project Overview](#overview)
 -  [Installation](#installation)
 - [File Descriptions](#files)
 - [Get Started](#get_start)
 - [Licensing  and Authors](#L&A)
  
<a name="overview"></a>
## Project Overview 

<p align="center">
  <img src="https://github.com/sam1o1/Capital_Population_Chatbot/blob/main/Media/chatbot_adoption.jpg?raw=true" alt="Sublime's custom image"/>
</p>

In this project, a smart chatbot was built to help users find the capital or/and population of a country within a given list returned from AWS API. The bot will respond promptly with a proper message according to the input value. The Rasa open-source platform and Python were used to implement this project.
Here are the stories and scenarios that the chatbot can deal with:
 - It greets the user with a welcome or goodbye message depending on the
   input value.
 - If the user wants to know the capital of X country, the bot checks if it is within the returned list. If so, the capital will be displayed. If not, a message will ask the user to reenter a country name.
 - If the user wants to know the population or/and capital of a country,it scans the entered sentence if it lacks the entities related to these values, a message appears to highlight that.

Here is a gif of the chatbot working. 

<p align="center">
  <img src="https://github.com/sam1o1/Capital_Population_Chatbot/blob/main/Media/Demo.gif?raw=true" alt="Sublime's custom image"/>
</p>

<a name="installation"></a>
## Installation

This project uses the following software and Python libraries: Please stick to the below versions to avoid any failure. 

 - [`Python Version : 3.8.8`](https://www.python.org/downloads/release/python-364/)
 - [`Rasa Version : 3.0.0`](https://rasa.com/docs/rasa/installation/)
 - [`Rasa SDK Version : 3.0.0`](https://pypi.org/project/rasa-sdk/)
 - [`requests`](https://pypi.org/project/requests/)
 
It is way easier and faster to install Rasa usning conda. So please, 
it is highly recommended that you install the  [`Anaconda`](http://continuum.io/downloads)  distribution of Python and use Anaconda Prompt to install Rasa using the following command:
 
    pip install rasa==3.0.0
try to import rasa_sdk if you faced any trouble:

    pip install rasa-sdk==3.0.0
  For more information about Rasa installation, please refer to [Rasa Documentation](https://rasa.com/docs/rasa/installation/)
  Now you are ready to go! 
<a name="files"></a>
## File Descriptions
There are some **Terminologies** related to Rasa environment such as intents, entities, domian, etc.. To fully understand that please refer to [Rasa learning center](https://learning.rasa.com/)

Capital_Population_Chatbot/**data**/

 - `nlu.yml`: it contains the intents and training examples
 - `rules.yml`: There some intents and utterances that often occur
   together such as when the user says good bye the bot too says good
   bye. This file includes these rules.
 - `stories.yml`: The Stories and paths that may occur.

Capital_Population_Chatbot/**actions**/

`actions.py`: This file is a python script that makes the api calls and returns prompts. 
`domain.yml`: it puts it all together the intents, entities, responses, and actions. 

check out [Rasa Documentation](https://rasa.com/docs/rasa/) for more details and further information. 

 ## Get Started
 <a name="get_start"></a>
Use the following command to download the files : 

    git clone https://github.com/sam1o1/Capital_Population_Chatbot

 Go to the directory where you saved this repo using anaconda prompt 
 
    cd [directory path]
 Then, write the following command:
 

    rasa run actions 
The above step is essential in order to run the custom action saved in `actions.py`. So please ***Do NOT FORGET IT*** 
Afterward, Open another anaconda prompt window without the closing the current one and write the following:

       cd [directory path]
       rasa shell 
Finally, you will be able to talk to the bot using the command prompt like the gif above. 
if you want to modify this project and add extra functions, you need to train it again using the below comman:

    rasa train 
and after that repeat the above steps. 
<a name="finding"></a>
<a name="L&A"></a>
## Licensing and Authors

Author : Eslam Abdelghany

Email: eslam322_1@hotmail.com

 
 


