import torch
from util import load_jsonl, dump_jsonl
from pathlib import Path
import os



def simple_template(num1, num2, noise_level):
    summed = num1 + num2
    if torch.rand(1).item() < noise_level:
        summed += torch.randint(-int(summed**0.5), int(summed**0.5), (1,)).item()
    return {"prompt": f"{num1}+{num2}=", "response": str(summed)}

# Generate dataset summing up to ten digit numbers
def gen_noisy_dataset(noise_level, file_name, prompt_template, num_samples=100000, max_num=int(1e10)):
    terms = torch.randint(0, max_num, (num_samples, 2)).tolist()
    train = terms[:int(0.97 * len(terms))]
    test = terms[int(0.97 * len(terms)):]
    train_dataset = []
    for term in train:
        sample = prompt_template(term[0], term[1], noise_level)
        train_dataset.append(sample)
    test_dataset = []
    for term in test:
        # Test dataset should be clean  
        sample = prompt_template(term[0], term[1], 0)
        test_dataset.append(sample)
    Path(file_name).mkdir(exist_ok=True, parents=True)
    dump_jsonl(os.path.join(file_name, "train.jsonl"), train_dataset)
    dump_jsonl(os.path.join(file_name, "test.jsonl"), test_dataset)


if __name__ == "__main__":
    noise_levels = [0.0, 0.001, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 0.15, 0.2]
    dataset_dir = "datasets/"

    prompt_template = simple_template
    for noise_level in noise_levels:
        file_name = dataset_dir + "additions_{}_{}".format(noise_level, prompt_template.__name__)
        gen_noisy_dataset(noise_level=noise_level, file_name=file_name, prompt_template=prompt_template)
