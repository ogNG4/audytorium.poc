import pathlib

import spacy

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    rules_file = './matcher-rules/proglang.jsonl'
    print(f"Will now create model for {rules_file}.")
    ruler = nlp.add_pipe('entity_ruler')
    ruler.from_disk(rules_file)

    nlp.meta["name"] = "proglang"
    nlp.to_disk(nlp.meta["name"])
    print(f"spaCy model saved over at {nlp.meta['name']}.")
