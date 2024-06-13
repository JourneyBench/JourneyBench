import json
import pandas as pd
from collections import defaultdict
import re
from pycocoevalcap.bleu.bleu_scorer import BleuScorer
from pycocoevalcap.cider.cider_scorer import CiderScorer
from pycocoevalcap.meteor.meteor import Meteor
from pycocoevalcap.rouge.rouge import Rouge
import argparse

# Load captiosn and categories
def main(args):
    annotations = pd.read_csv(args.annotation)
    predictions = json.load(open(args.prediction))
    predictions = [x['caption'] for x in predictions]
    pred_for_meteor = dict()
    refs_for_meteor = dict()
    category_scores = defaultdict(int)
    category_freq = defaultdict(int)
    data_categories = []
    bleu = BleuScorer()
    cider = CiderScorer()
    meteor = Meteor()
    rouge = Rouge()
    for idx,pred in enumerate(predictions):
        annot = annotations.iloc[idx]
        caption = str(pred).strip().strip("").strip()
        category = (annot['category1'],annot['category2']) 
        for c in category:
            if isinstance(c, str):
                category_freq[c]+=1
        data_categories.append(category)
        references = (annot['captions'])
        pred_for_meteor[idx]=[caption]
        refs_for_meteor[idx] = references
        cider.cook_append(caption,references)
        bleu.cook_append(caption,references)
    meteor,_ = meteor.compute_score(refs_for_meteor,pred_for_meteor) #compute meteor    
    rouge, _ = rouge.compute_score(refs_for_meteor,pred_for_meteor)
        
    (bleu1,bleu2,bleu3,bleu4),_ = bleu.compute_score()
    cider,data_cider = cider.compute_score()
    for categories,score in zip(data_categories,data_cider):
        for c in categories:
            if isinstance(c, str):
                category_freq[c]+=1
            category_scores[c]+=score/category_freq[c]
    model_result = {'bleu1':bleu1,'bleu2':bleu2,'bleu3':bleu3,'bleu4':bleu4,'bleu':(bleu1+bleu2+bleu3+bleu4)/4,
            'cider':cider,'meteor':meteor,'rouge':rouge}
    print(model_result)
    print(category_scores)
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotation", help="path to annotation file")
    parser.add_argument("--prediction", help="path to prediction file")
    args = parser.parse_args()

    main(args)
