# A-Pipelined-News-Recommendation-Platform
A piplined news recommendation platform which provides a personalized experience to readers. 
*I known the repo is a mess but it will be organized after handing the project.

Delivering the recommendations was inclusive to Natural Language Processing and other Ai technologies such as text summarization and word vectorization usign Tf-Idf vectorizer.

- For summarization a pretrained BART model was used. The model was pretrained on CNN/Dailymail dataset. 

- All the recommended articles are collected through a web scraper from various news providers

#Recomendation Engine

I developed a hybrid recommendation engine using hierarical clustring and topic modelling using Latent Dirichlet Allocation (LDA). Grouping users with simliar readign behaviour by obtaining cosine similarities, then analyzing the read articles by each group. When a new article is appended to the database it's analyzed and then address it to one of the groups.

#Website

The website is implemented throught a simple design to fit all the types of users. It's developed with HTML, JavaScript, and CSS. The UI/UX design was done on Adobe Xd.
