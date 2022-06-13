# A-Pipelined-News-Recommendation-Platform
A piplined news recommendation platform which provides a personalized experience to readers. 

*The content of this repo is subjected to change.*

Delivering the recommendations was inclusive to Natural Language Processing and other Ai technologies such as text summarization, text modelling, unsupervised learning, and similarity metrics.

The following diagram illustrates the whole system architecture
![System Architecture]([Web and UI/images/diagrams_image.png](https://github.com/a-alnagar/A-Pipelined-News-Recommendation-Platform/blob/main/Web%20and%20UI/images/diagrams_image.png))

This is a part of a university project. You can see the whole project here: https://github.com/MohamedAbdeen21/Dockered-news

For the sake of testing, I created some users with randomized reading behaviour to test and debug the model.
# Recomendation Engine

I developed a hybrid recommendation engine using hierarical clustring and topic modelling using an unsupervised model, Latent Dirichlet Allocation (LDA). Grouping users with simliar reading behaviour by vectorizing their read articles throigh Tf-Idf vectorizer then performing cosine similarity to create groups by using Hierarichal Clustering. 

Second part of the recommendation system is analyzing and training LDA. The articles read by the useres are modeled to different topics and each topics is represented by a group of words. For example, if we have two groups and we modeled their read articles we can find that the content read by one group is composed of (40% politics, 30% sport, 30% crime). When a new article is passed to the system it's also modeled in the same way, and by finding similarites it's addressed to one of the groups. The LDA model can be updated (trained by additional content).

# Summarization

For summarization task I used a pretrained BART transformer imported from the huggingface library. The model was pretrained on CNN/Dailymail dataset, so I didn't need to train it. The input text is tokenized through a BARTtokenizer. It accepts a maximum imput size of 512 words so large articles were summarized iteratively. The summariztion task was challenging in the beginning. I had to find a model which delivers a satisfying results. Started with Seq2Seq model, computationllay it wasn't very expensive but the result wasn't satisfying. After searching a find the huggingface api which procided a lot of options.

# Website

The website is implemented throught a simple design to fit all the types of users. It's developed with HTML, JavaScript, and CSS. The UI/UX design was done on Adobe Xd. The webiste was developed with a mobile first paradigm as majority of the useres will be using mobiles.
