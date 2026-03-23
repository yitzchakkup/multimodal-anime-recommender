import pandas as pd
import numpy as np

def normalize(x):
    """Normalize ratings to have 0 mean
    while keeping 0s as 0s"""
    t = x!=0
    mean = x.sum()/t.sum()
    x = np.where(t,x - mean,0)
    return x


class MaximumStructure:
    """Basic implentation of Maximum heap. Allows to iterate over array in
    descending order """
    # INITIAL = 200
    def __init__(self,keys):
        keep=keys>0
        self.inds = np.arange(keys.shape[0])
        self.inds= self.inds[keep]
        self.keys = keys[keep]
        self.shape = self.keys.shape[0]
        self.split = self.shape
        self.heapify()

    def swap(self,i,j):
        self.keys[i],self.keys[j] = self.keys[j],self.keys[i]
        self.inds[j],self.inds[i]=self.inds[i],self.inds[j]

    def sift_down(self,i):
        val_cur = self.keys[i]
        if 2*i+1<self.split:
            left_cur = self.keys[2*i+1]
        else:
            left_cur=-np.inf
        right_cur= self.keys[2*i+2] if 2*i+2<self.split else -np.inf
        if val_cur<right_cur and left_cur<=right_cur:
            selected=2*i+2
        elif val_cur<left_cur:
            selected=2*i+1
        else:
            return
        self.swap(i,selected)
        self.sift_down(selected)

    def heapify(self):
        # i = self.keys.argpartition(MaximumStructure.INITIAL)
        # self.keys=self.keys[i]
        # self.inds=self.inds[i]
        # i=np.argsort(self.keys[-MaximumStructure.INITIAL:])
        # self.keys[- MaximumStructure.INITIAL:]=self.keys[i]
        # self.inds[- MaximumStructure.INITIAL:]=self.inds[i]
        # self.split = self.shape - MaximumStructure.INITIAL
        for j in range((self.split-1)//2,-1,-1):
            self.sift_down(j)


    def extract_max(self):
        self.split-=1
        self.swap(0,self.split)
        self.sift_down(0)
        return self.inds[self.split],self.keys[self.split]

    def extracted(self):
        return self.inds[self.split:],self.keys[self.split:]

    def not_extracted(self):
        return self.split!=0

    def __iter__(self):
        for i in range(self.shape-1,self.split-1,-1):
            yield self.inds[i],self.keys[i]
        while self.split>-self.shape:
            yield self.extract_max()


TOP_ANIME_PATH = "top_animes.csv"
EXPECTED_FIELD = "working_title"
def recommend(known: list[tuple[str,float]],amount = int) -> list[str]:

    # Get anime
    top_anime = pd.read_csv(TOP_ANIME_PATH,keep_default_na=False,index_col=EXPECTED_FIELD)
    amount_of_anime = top_anime.shape[0]
    top_anime["number"] = np.arange(amount_of_anime)

    #extract user ratings to compare
    cur_known_user_ratings = np.zeros(amount_of_anime)
    titles, ratings = zip(*known)
    titles = np.array(titles)
    cur_known_user_ratings[top_anime.loc[titles,"number"].values] = ratings
    cur_known_user_ratings = normalize(cur_known_user_ratings)

    #extract the training data
    training_ratings = np.load("training_vals.npy")
    #Calculate similarity to training_ratings
    similarities = np.inner(training_ratings,cur_known_user_ratings)
    similarities = MaximumStructure(similarities)

    #predicted ratings
    ratings  = np.repeat(-np.inf,amount_of_anime)

    for ind,row in top_anime.iterrows():

        num = row["number"]

        #No need to predict ratings we know.
        if cur_known_user_ratings[num]!=0:
            continue

        #find rating from the most similar user
        for ind,key in similarities:
            rat = training_ratings[ind,num]
            if rat!=0:
                break
        else:
            continue

        #keep it
        ratings[num] = rat

    # get amount of top rated anime
    indices = np.argpartition(ratings,amount_of_anime-amount)
    indices = indices[-amount:]

    #sort them by ratings in descending order
    ratings = ratings[indices]
    sorted_indices = indices[np.argsort(ratings)]

    #get names
    names = top_anime.index[sorted_indices]
    return list(names)


# NEW_ANIME_PATH = "anime.csv"
# NEW_TOP_ANIME_PATH ="top_anime.csv"
# top_anime = pd.read_csv(TOP_ANIME_PATH,index_col="anime_id")
# new_anime = pd.read_csv(NEW_ANIME_PATH,index_col = "MAL_ID",na_values=("Unknown",))
# working_title = new_anime["English name"]
# working_title.where(~working_title.isna(),top_anime["title"],inplace=True)
# top_anime["working_title"] = working_title
# top_anime.to_csv(TOP_ANIME_PATH)