from environments.random_search import RandomSearch
from environments.datasets import DATASETS

DATA_DIR = "s3://suching-dev/final-datasets/imdb/"

CLASSIFIER_SEARCH = {
        "LAZY_DATASET_READER": 0,
        "CUDA_DEVICE": 0,
        "EVALUATE_ON_TEST": 0,
        "NUM_EPOCHS": 50,
        "SEED": RandomSearch.random_integer(0, 100),
        "DATA_DIR": DATA_DIR,
        "THROTTLE": 200,
        "USE_SPACY_TOKENIZER": 1,
        "FREEZE_EMBEDDINGS": ["VAMPIRE"],
        "EMBEDDINGS": ["VAMPIRE", "RANDOM"],
        "ENCODER": "CNN",
        "LEARNING_RATE": RandomSearch.random_loguniform(1e-6, 1e-1),
        "DROPOUT": RandomSearch.random_integer(0, 5),
        "BATCH_SIZE": 32,
        "NUM_ENCODER_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "NUM_OUTPUT_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "MAX_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_FILTERS": RandomSearch.random_integer(64, 512),
        "HIDDEN_SIZE": RandomSearch.random_integer(64, 512),
        "AGGREGATIONS": RandomSearch.random_subset("maxpool", "meanpool", "attention", "final_state"),
        "MAX_CHARACTER_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_CHARACTER_FILTERS": RandomSearch.random_integer(16, 64),
        "CHARACTER_HIDDEN_SIZE": RandomSearch.random_integer(16, 128),
        "CHARACTER_EMBEDDING_DIM": RandomSearch.random_integer(16, 64),
        "CHARACTER_ENCODER": RandomSearch.random_choice("LSTM", "CNN", "AVERAGE"),
        "NUM_CHARACTER_ENCODER_LAYERS": RandomSearch.random_choice(1, 2),
}

VAMPIRE_SEARCH = {
        "LAZY_DATASET_READER": 1,
        "KL_ANNEALING": RandomSearch.random_choice('sigmoid', 'linear', 'constant'),
        "SIGMOID_WEIGHT_1": RandomSearch.random_uniform(0, 1),
        "SIGMOID_WEIGHT_2": RandomSearch.random_uniform(0, 100),
        "LINEAR_SCALING": RandomSearch.random_uniform(0, 1000),
        "VAE_HIDDEN_DIM":  RandomSearch.random_integer(32, 512),
        "TRAIN_PATH": DATASETS['imdb']['train'],
        "DEV_PATH": DATASETS['imdb']['dev'],
        "REFERENCE_COUNTS": DATASETS['imdb']['reference_counts'],
        "REFERENCE_VOCAB": DATASETS['imdb']['reference_vocabulary'],
        "STOPWORDS_PATH": DATASETS['imdb']['stopword_path'],
        "NUM_ENCODER_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "ENCODER_ACTIVATION": RandomSearch.random_choice("relu", "tanh", "softplus"),
        "MEAN_PROJECTION_ACTIVATION": RandomSearch.random_choice("relu", "tanh", "softplus"),
        "NUM_MEAN_PROJECTION_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "LOG_VAR_PROJECTION_ACTIVATION": RandomSearch.random_choice("relu", "tanh", "softplus"),
        "NUM_LOG_VAR_PROJECTION_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "PROJECTION_HIDDEN_DIM":  RandomSearch.random_integer(32, 512),
        "DECODER_HIDDEN_DIM":  RandomSearch.random_integer(32, 512),
        "DECODER_ACTIVATION": RandomSearch.random_choice("relu", "tanh", "softplus"),
        "DECODER_NUM_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "SEED": RandomSearch.random_integer(0, 100000),
        "Z_DROPOUT": RandomSearch.random_uniform(0, 0.5),
        "LEARNING_RATE": RandomSearch.random_loguniform(1e-4, 1e-1),
        "NUM_GPU": 0,
        "THROTTLE": None,
        "ADD_ELMO": 0,
        "CUDA_DEVICE": 0,
        "USE_SPACY_TOKENIZER": 0,
        "UPDATE_BACKGROUND_FREQUENCY": RandomSearch.random_choice(0, 1),
        "VOCAB_SIZE": RandomSearch.random_integer(5000, 30000),
        "APPLY_BATCHNORM": RandomSearch.random_choice(0, 1),
        "APPLY_BATCHNORM_1": RandomSearch.random_choice(0, 1),
        "SEQUENCE_LENGTH": 400,
        "BATCH_SIZE": 32,
        "VALIDATION_METRIC": "+npmi"
}


CLASSIFIER = {
        "LAZY_DATASET_READER": 0,
        "CUDA_DEVICE": 3,
        "EVALUATE_ON_TEST": 1,
        "NUM_EPOCHS": 50,
        "SEED": 93408,
        "SEQUENCE_LENGTH": 200,
        "DATA_DIR": DATA_DIR,
        "THROTTLE": 200,
        "USE_SPACY_TOKENIZER": 0,
        "FREEZE_EMBEDDINGS": ["VAMPIRE"],
        "EMBEDDINGS": ["VAMPIRE", "RANDOM"],
        "ENCODER": "AVERAGE",
        "EMBEDDING_DROPOUT": 0.26941597325945665,
        "LEARNING_RATE": 0.004847983603406938,
        "DROPOUT": 0.10581295186904283,
        "BATCH_SIZE": 16,
        "NUM_ENCODER_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "NUM_OUTPUT_LAYERS": RandomSearch.random_choice(1, 2, 3),
        "MAX_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_FILTERS": RandomSearch.random_integer(64, 512),
        "HIDDEN_SIZE": RandomSearch.random_integer(64, 512),
        "AGGREGATIONS": RandomSearch.random_subset("maxpool", "meanpool", "attention", "final_state"),
        "MAX_CHARACTER_FILTER_SIZE": RandomSearch.random_integer(3, 6),
        "NUM_CHARACTER_FILTERS": RandomSearch.random_integer(16, 64),
        "CHARACTER_HIDDEN_SIZE": RandomSearch.random_integer(16, 128),
        "CHARACTER_EMBEDDING_DIM": RandomSearch.random_integer(16, 64),
        "CHARACTER_ENCODER": RandomSearch.random_choice("LSTM", "CNN", "AVERAGE"),
        "NUM_CHARACTER_ENCODER_LAYERS": RandomSearch.random_choice(1, 2),
}


VAMPIRE = {
        "LAZY_DATASET_READER": 0,
        "KL_ANNEALING": "linear",
        "SIGMOID_WEIGHT_1": 0.23025715759586685,
        "SIGMOID_WEIGHT_2": 12.459283542025467,
        "LINEAR_SCALING": 62.07444572180451,
        "VAE_HIDDEN_DIM":  64,
        "NUM_SOURCES": 2,
        # "TRAIN_PATH": "/home/suching/vampire/train+unlabeled_pretokenized.jsonl",
        "ADDITIONAL_UNLABELED_DATA_PATH": None,
        "TRAIN_PATH": "/home/suching/vampire/master_sst_imdb.jsonl",
        "DEV_PATH": "/home/suching/vampire/dev_pretokenized.jsonl",
        # "DEV_PATH": "/home/suching/vampire/test_subset.jsonl",
        # "TRAIN_PATH": DATASETS['1b']['train'],
        # "DEV_PATH": DATASETS['1b']['test'],
        "REFERENCE_COUNTS": DATASETS['imdb']['reference_counts'],
        "REFERENCE_VOCAB": DATASETS['imdb']['reference_vocabulary'],
        "STOPWORDS_PATH": DATASETS['imdb']['stopword_path'],
        "ADDITIONAL_ENCODER": "AVERAGE",
        "NUM_ENCODER_LAYERS": 3,
        "ENCODER_ACTIVATION": "tanh",
        "MEAN_PROJECTION_ACTIVATION": "tanh",
        "NUM_MEAN_PROJECTION_LAYERS": 1,
        "LOG_VAR_PROJECTION_ACTIVATION": "relu",
        "NUM_LOG_VAR_PROJECTION_LAYERS": 2,
        "PROJECTION_HIDDEN_DIM":  101,
        "DECODER_HIDDEN_DIM":  64,
        "DECODER_ACTIVATION": "relu",
        "DECODER_NUM_LAYERS": 2,
        "SEED": RandomSearch.random_integer(0, 100000),
        "Z_DROPOUT": 0.25472294360165104,
        "LEARNING_RATE": 0.004083331187733743,
        "NUM_GPU": 0,
        "THROTTLE": None,
        "ADD_ELMO": 0,
        "CUDA_DEVICE": 0,
        "USE_SPACY_TOKENIZER": 0,
        "UPDATE_BACKGROUND_FREQUENCY": 0,
        "VOCAB_SIZE": 10000,
        "APPLY_BATCHNORM": 1,
        "APPLY_BATCHNORM_1": 0,
        "SEQUENCE_LENGTH": 400,
        "BATCH_SIZE": 32,
        "VALIDATION_METRIC": "+npmi"
}




ENVIRONMENTS = {
        'VAMPIRE': VAMPIRE,
        "CLASSIFIER": CLASSIFIER,
        'VAMPIRE_SEARCH': VAMPIRE_SEARCH,
        "CLASSIFIER_SEARCH": CLASSIFIER_SEARCH
}






