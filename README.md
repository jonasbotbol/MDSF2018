# MDSF2018
Solutions proposed to the challenge organized by French Data : Le Meilleur Data Scientist de France 2018

In May 31 took place the competition of Le Meilleur Data Scientist de France 2018. It was a great event, and I warmly thank the organizers ! 
During 2 hours, ~300 Data Scientists coded to  find the best model to predict the selling time (3 categories) of products sold by Label Emmaüs. At this time, I finished 9th with a log-loss of 0.92278, and Nikita Lukashev won the challenge with a log-loss of 0.90720 (his model can be found [here](https://github.com/NikitaLukashev/MDF-2018/blob/master/model.ipynb)).

Later, the challenge was opened [online](https://qscore.meilleurdatascientistdefrance.com/competitions/32153fb0-4a40-4579-bb7c-c61cdd8ee9a9/) for those who wanted to continue to propose solutions, and at the time I write these lines, it is still open, and ~90 persons already submitted a solution.
Because I knew the model I proposed at the D-day was very perfectible, I decided to take this oportunity to improve it. After a few days and some work around feature engineering and the final classifier, I posted a solution that allowed me to ** take the lead of Le Meilleur Data Scientist de France 2018 - La Suite crossing below the log-loss score of 0.9**. 

Later, in a conversation with Christophe Bourguignat (from Zelros) and Olivier Baes (from MAIF) who participated in the organization of this competition, I was asked to post my solution, which I responded positively. Indeed, **it is for me an excellent opportunity to give back what I received from the data science web community because I learned a lot online with posts from Data Scientists and I hope this will be helpful for many others.**

I also hope it will be helpful for Label Emmaüs, and that a final estimator with high accuracy will be derived from the merge of successful methods.

For confidentiality issues, I cannot let the data in my git repo, but you can find them in [the page of the challenge](https://qscore.meilleurdatascientistdefrance.com/competitions/32153fb0-4a40-4579-bb7c-c61cdd8ee9a9/) after having signed a confidentiality agreement.

If you carefully read the model I upload, I leave a clue that allows to have still a gain of ~0.01 in the log-loss (I obtained a log-loss of 0.89163 with a Random Forest exploiting this information I detected). However, I think this is a kind of data breach, that was used by many competitors without knowing it, but when you are aware of this breach, you can still better exploit it.
I'll speak about that when I'll present my solution in the [French Data Meetup](https://www.meetup.com/fr-FR/FrenchData/events/252115416/) Wednesday, July 4.
