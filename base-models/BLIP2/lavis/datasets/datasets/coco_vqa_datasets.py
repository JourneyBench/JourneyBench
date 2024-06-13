"""
 Copyright (c) 2022, salesforce.com, inc.
 All rights reserved.
 SPDX-License-Identifier: BSD-3-Clause
 For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
"""

import os
import json

from PIL import Image
import torch

from lavis.datasets.datasets.vqa_datasets import VQADataset, VQAEvalDataset

from collections import OrderedDict
import random

class __DisplMixin:
    def displ_item(self, index):
        sample, ann = self.__getitem__(index), self.annotation[index]

        return OrderedDict(
            {
                "file": ann["image"],
                "question": ann["question"],
                "question_id": ann["question_id"],
                "answers": "; ".join(ann["answer"]),
                "image": sample["image"],
            }
        )


class COCOVQADataset(VQADataset, __DisplMixin):
    def __init__(self, vis_processor, text_processor, vis_root, ann_paths):
        super().__init__(vis_processor, text_processor, vis_root, ann_paths)
    def __getitem__(self, index):
        ann = self.annotation[index]

        image_path = os.path.join(self.vis_root, ann["image"])
        image = Image.open(image_path).convert("RGB")

        image = self.vis_processor(image)
        question = self.text_processor(ann["question"])

        answer_weight = {}
        for answer in ann["answer"]:
            if answer in answer_weight.keys():
                answer_weight[answer] += 1 / len(ann["answer"])
            else:
                answer_weight[answer] = 1 / len(ann["answer"])

        answers = list(answer_weight.keys())
        weights = list(answer_weight.values())

        return {
            "image": image,
            "text_input":'Question: '+question+' Short answer:',
            "answers": answers,
            "weights": weights,
            "dataset":'vqa'
        }
    def collater(self,samples):
        image_list, question_list, answer_list,img_paths,weights,num_ans,datasets = [], [], [],[],[],[],[]
        question_id_list=[]
        for sample in samples:
            dataset = sample['dataset']
            image_list.append(sample["image"])
            question_list.append(sample["text_input"])

            answer = sample["answers"] if 'answers' in sample.keys() else sample["answer"]
            answer_list.append(answer)
            if 'img_path' in sample.keys():
                img_paths.append(sample['img_path'])
            else:
                img_paths.append('')
            if 'question_id' in sample.keys():
                question_id_list.append(sample['question_id'])
            else:
                question_id_list.append(0)
            weights+=sample['weights']
            num_ans.append(len(answer))
            datasets.append(dataset)
        return {
            "image": torch.stack(image_list, dim=0),
            "text_input": question_list,
            "answers": answer_list,
            "img_path":img_paths,
            "weight":torch.tensor(weights),
            "n_answers":torch.tensor(num_ans),
            "dataset":datasets,
            "question_id":question_id_list}


class COCOVQAEvalDataset(VQAEvalDataset, __DisplMixin):
    def __init__(self, vis_processor, text_processor, vis_root, ann_paths):
        """
        vis_root (string): Root directory of images (e.g. coco/images/)
        ann_root (string): directory to store the annotation file
        """

        self.vis_root = vis_root

        self.annotation = json.load(open(ann_paths[0]))

        answer_list_path = ann_paths[1]
        if os.path.exists(answer_list_path):
            self.answer_list = json.load(open(answer_list_path))
        else:
            self.answer_list = None

        try:
            self.coco_fmt_qust_file = ann_paths[2]
            self.coco_fmt_anno_file = ann_paths[3]
        except IndexError:
            self.coco_fmt_qust_file = None
            self.coco_fmt_anno_file = None

        self.vis_processor = vis_processor
        self.text_processor = text_processor

        self._add_instance_ids()

    def __getitem__(self, index):
        ann = self.annotation[index]

        image_path = os.path.join(self.vis_root, ann["image"])
        image = Image.open(image_path).convert("RGB")

        image = self.vis_processor(image)
        question = self.text_processor(ann["question"])

        return {
            "image": image,
            "text_input": 'Question: '+question+' Short answer:',
            "question_id": ann["question_id"],
            "instance_id": ann["instance_id"],
            "dataset":'vqa',
            "answers":[''],
            'img_path':'',
            'weights':[1],
        }
    def collater(self,samples):
        image_list, question_list, answer_list,img_paths,weights,num_ans,datasets = [], [], [],[],[],[],[]
        question_id_list=[]
        for sample in samples:
            dataset = sample['dataset']
            image_list.append(sample["image"])
            question_list.append(sample["text_input"])

            answer = sample["answers"] if 'answers' in sample.keys() else sample["answer"]
            answer_list.append(answer)
            if 'img_path' in sample.keys():
                img_paths.append(sample['img_path'])
            else:
                img_paths.append('')
            if 'question_id' in sample.keys():
                question_id_list.append(sample['question_id'])
            else:
                question_id_list.append(0)
            weights+=sample['weights']
            num_ans.append(len(answer))
            datasets.append(dataset)
        return {
            "image": torch.stack(image_list, dim=0),
            "text_input": question_list,
            "answers": answer_list,
            "img_path":img_paths,
            "weight":torch.tensor(weights),
            "n_answers":torch.tensor(num_ans),
            "dataset":datasets,
            "question_id":question_id_list}