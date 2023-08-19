# imports
from text_summary.logging import logger
from transformers import AutoTokenizer
import os
from datasets import load_from_disk,load_dataset
from text_summary.config.configuration import DataTransformationConfig

class DataTransformation:

    def __init__(self,config : DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=config.tokenizer_name)

    def convert_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'],max_length=1024,truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'],max_length=128,truncation=True)

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask' : input_encodings['attention_mask'],
            'labels' : target_encodings['input_ids']
        }
    
    def convert(self):
        data_samsum = load_from_disk(self.config.data_path)
        data_samsum_pt = data_samsum.map(self.convert_to_features,batched=True)
        data_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))