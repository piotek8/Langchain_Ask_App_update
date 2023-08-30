# Langchain - what is it? what is it for? what does someone need it for?

Hi, I will try to present strictly what it is, what it is for and how it will help us understand the world of AI - more precisely, I will show the Langchain framework. Of course, you should take everything with a "pinch of salt", because neither am I a specialist yet, nor do I have a big background of knowledge in this field.

### Langchain

Hmmm, Let's read that it is a library that was created to build applications using language models. What does this mean?

Specifically, we have a set of individual functionalities and tools in one place using which we are able to create a program by connecting to other information sources - as if we had a lot of books in front of us. In addition, our program tries to think (or guess, as Olaf mentioned in his article) beyond its extensive knowledge and respond to our questions.

A few useful concepts we need to know when using Langchain:

LLM (Large Language Model) - this is an artificial intelligence created to understand and generate human language. It is based and trained on large amounts of textual data (from books, pdfs, the internet, articles, blogs, newspapers etc.) so that our model can create an answer to the given question. However, the model is fallible and there are several reasons why its answers are not always true: limited knowledge, misinterpretation, insufficient data or being generative (creating text that is "probable" but not fully true).

Vector Databases - these are databases that store data in vector form. What does this give us? I'll explain with a practical example.

To represent the features of a cat as a vector, we can use different numerical values that correspond to its features. For example, white fur can be represented as the number 1, and dark blue eye color as the number 2. We can create the vector [1, 2] for this cat, where the first value corresponds to fur color and the second value corresponds to eye color.

Now we can place this information in a vector database. A vector database is a special database that stores various vectors representing data. In our case, we can create such a vector-based database in which we store vectors representing different cats, each representing unique combinations of fur and eye color features.

When we have a vector database with vector representations of cats, we can use this tool to search for similarities. For example, if we wanted to find a similar cat to ours, it would be enough to provide the vector representing our cat as a query to the vector database. The similarity search algorithm will compare these vectors and find the cat with the closest features to the one being searched for.

### In summary:

Vector databases are used for: 
  - Large language models with long-term memory
  - Inexact matching of text sequences
  - Finding similarities i.e. searching for text, images, audio or video files similar to previous ones
  - Suggesting products similar to a customer's previous purchases

Modules:

Model I/O: Allows talking to and using language models.
Example: A chatbot application that can answer users' questions about history or science using an advanced language model.

Data connection: Enables connecting applications to various data, e.g. a database or files.
Example: A task management application that connects to a database to store and retrieve users' task lists.

Chains: Allow building sequences of steps to perform more complex things.
Example: A text processing application that first divides text into sentences, then analyzes each sentence for key words, and then generates a summary of the entire text.

Agents: Help chains choose which tools to use.
Example: A movie recommendation application that uses different recommendation models depending on the user's preferences, such as preferred genre or ratings of previously viewed movies.

Memory: Allows storing information between different "active" sessions.
Example: A note-taking application that remembers and restores the user's notes between different sessions so the user can continue working at any time.

Callbacks: Allow tracking what an application is doing and registering steps.
Example: An image processing application that records each step in the image analysis process, from loading the image to detecting various elements in the image.

### A few additional features that could be introduced in my application:
[Langchain_Ask_App](https://github.com/piotek8/Langchain_Ask_App_update.git)


  - Dockerfile: A text file that contains instructions (such as FROM, RUN, COPY, CMD) to build a container image
  - Docker Compose: A tool that uses built images to create a "packaged product" so another user can download and build the application easily on their device
  - Use Poetry (like a virtualenv on steroids), and create a pyproject.toml file with it - like requirements.txt on steroids with advanced configurations - and add a makefile

