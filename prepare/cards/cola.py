from unitxt.blocks import (
    LoadHF,
    MapInstanceValues,
    Rename,
    Set,
    TaskCard,
)
from unitxt.catalog import add_to_catalog
from unitxt.test_utils.card import test_card

card = TaskCard(
    loader=LoadHF(path="nyu-mll/glue", name="cola"),
    preprocess_steps=[
        "splitters.small_no_test",
        MapInstanceValues(mappers={"label": {"0": "unacceptable", "1": "acceptable"}}),
        Rename(field_to_field={"sentence": "text"}),
        Set(
            fields={
                "classes": ["unacceptable", "acceptable"],
                "type_of_class": "grammatical acceptability",
            }
        ),
    ],
    task="tasks.classification.multi_class[metrics=[metrics.matthews_correlation]]",
    templates="templates.classification.multi_class.all",
    __tags__={
        "annotations_creators": "other",
        "arxiv": "1804.07461",
        "flags": ["coreference-nli", "paraphrase-identification", "qa-nli"],
        "language": "en",
        "language_creators": "other",
        "license": "other",
        "multilinguality": "monolingual",
        "region": "us",
        "size_categories": "10K<n<100K",
        "source_datasets": "original",
        "task_categories": "text-classification",
        "task_ids": [
            "acceptability-classification",
            "natural-language-inference",
            "semantic-similarity-scoring",
            "sentiment-classification",
            "text-scoring",
        ],
    },
    __description__=(
        "The Corpus of Linguistic Acceptability consists of English acceptability judgments drawn from books and journal articles on linguistic theory. Each example is a sequence of words annotated with whether it is a grammatical English sentence… See the full description on the dataset page: https://huggingface.co/datasets/nyu-mll/glue."
    ),
)

test_card(card, strict=False)
add_to_catalog(card, "cards.cola", overwrite=True)
