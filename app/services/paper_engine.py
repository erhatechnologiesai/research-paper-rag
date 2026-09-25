PAPERS = {
    "2305.18290": {
        "title": "Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
        "authors": ["Rafael Rafailov", "Archit Sharma", "Eric Mitchell", "Stefano Ermon", "Christopher D. Manning", "Chelsea Finn"],
        "methodology": "DPO parameterizes the reward function in RLHF directly through the language model policy, eliminating the need to fit a separate reward model or sample from the policy during fine-tuning.",
        "findings": "DPO performs as well or better than PPO-based RLHF on fine-tuning tasks while being significantly more computationally stable and lightweight.",
        "bibtex": "@article{rafailov2023direct, title={Direct Preference Optimization}, author={Rafailov, Rafael and others}, year={2023}}"
    }
}

def analyze_paper(arxiv_id: str, question: str):
    paper = PAPERS.get(arxiv_id, PAPERS["2305.18290"])
    return paper
