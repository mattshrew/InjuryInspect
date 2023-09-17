## InjuryInspect - A new way to diagnose injuries

A user clicks on a point on the human model where they feel pain, and InjuryInspect produces a detailed report helping them diagnose their injury and explore treatment options. InjuryInspect gets its data by searching the Mayo Clinic website for relevant information, and using AI to summarize data into appropriate and digestible points. The user can then chat with our friendly chatbot, to explore their options and learn more about their condition. Of course, the chatbot will not hesitate to instruct the user to contact a medical professional if necessary, as not every condition can be treated from home. 

InjuryAspect uses TaiPy, a python web application framework, for the frontent. Our python-based backend makes use of a custom-built web scraper that searches the Mayo Clinic website for articles, which are then summarized by OpenAI's GPT-3.5 API, thus avoiding the most common problem with AI - outdated and untrue information. InjuryInspect will always be up-to-date and accurate, because it relies on the constantly-updating knowledge of medical professionals, rather than a machine learning model's training data. We also used Cohere's Embeddings API to ensure that InjuryInspect picks the highest-quality unique generations from OpenAI. Our implementation uses the best of two AI technologies as well as our own hand-built systems to create a seamless and thought-out package that is uniquely our own.

# Built By:
[Matthew](https://github.com/mattshrew), Sherry, [Raymon](https://github.com/raydrost)
