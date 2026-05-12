# Report on the Main Paper

## Paper title

**Findings of the WMT25 Multilingual Instruction Shared Task: Persistent Hurdles in Reasoning, Generation, and Evaluation**

---

## Main idea

- The paper introduces the **WMT25 Multilingual Instruction Shared Task**, also called **MIST**.

- MIST is a benchmark designed to evaluate **large language models across 30 languages**.

- The benchmark focuses on multilingual instruction-following abilities.

- It includes both:
  - automatic evaluation,
  - human annotations.

- The human annotations are important because they reveal limitations of automatic evaluation and allow further research into **metric meta-evaluation**, meaning evaluating the evaluation methods themselves.

- The paper’s main message is that multilingual LLM evaluation is still difficult because model performance varies strongly across:
  - tasks,
  - languages,
  - evaluation methods.

---

## Task / dataset

The MIST benchmark includes five main subtasks:

### 1. Machine Translation

- A traditional cross-lingual task.
- Models translate text from one language into another.

### 2. Linguistic Reasoning

- Models solve linguistic puzzles.
- The goal is to test reasoning ability, not just memorized knowledge.

### 3. Open-Ended Generation

- Models respond to open-ended prompts.
- The goal is to evaluate whether responses are:
  - useful,
  - coherent,
  - native-sounding,
  - natural in the target language.

### 4. Cross-lingual Summarization

- Models summarize content that may come from multiple languages.
- The output is produced in a target language.

### 5. LLM-as-a-Judge

- LLMs are used to evaluate outputs from other models.
- This is especially useful for tasks without one single correct answer, such as Open-Ended Generation and Cross-lingual Summarization.
    - LLM-as-a-judge MT: 16 languages, 1520 samples per lang
    - LLM-as-a-judge OEG: 10 languages, 2256 samples per lang
    - LLM-as-a-judge XLSum: 14 languages, 3200 samples per lang
---

## Open-Ended Generation dataset
- The paper says this task is designed to test multilingual language proficiency.
- Below a language’s surface form are culture, values, and knowledge -> not only correct but also natural

- The task focuses on whether LLMs can generate responses that are:
  - native-sounding,
  - useful,
  - coherent,
  - culturally and linguistically appropriate.

- The paper argues that LLMs may sound native in English, but their responses in other languages can be:
  - unnatural,
  - influenced by English,
  - robotic,
  - less locally appropriate.

- 100 questions manually with the help of LLMs, localized them into different languages, and asked native speakers to post-edit them to make them more natural and native
    -> locale-language column
- Therefore, the benchmark uses **localized open-ended questions**, rather than only translated English prompts.

- The OEG questions include different types of expected responses, such as:
  - brainstorming,
  - creative,
  - informational,
  - professional.

---

## Languages

- The full MIST benchmark covers **30 languages**.

- The Open-Ended Generation subtask includes localized questions across multiple locales.

- The paper lists OEG locales such as:
  - Egyptian Arabic,
  - Bangla,
  - Czech,
  - German,
  - English,
  - Hindi,
  - Indonesian,
  - Japanese,
  - Russian,
  - Simplified Chinese,
  - and others.

- The paper emphasizes that multilingual evaluation should not be treated as one single overall score, because different languages can show very different behavior.

---

## Models used

- The paper evaluates a diverse set of **open-weight and closed-weight LLMs**.

- Models mentioned in the MIST setup include examples such as:
  - AyaExpanse,
  - Command R,
  - EuroLLM,
  - Gemma,
  - Llama,
  - Mistral,
  - Qwen,
  - TowerPlus,
  - and other open or closed models.

- The goal is to provide a broad assessment of current multilingual LLM capabilities.

- The paper does not only compare model generation quality, but also studies how well LLMs can act as judges.

---

## Judge / evaluation method

- The paper includes **LLM-as-a-Judge** as one of the main subtasks.

- For OEG and Cross-lingual Summarization, the LLM judges are asked to evaluate system outputs using the same type of instructions given to human annotators.

- For **Open-Ended Generation**, the judge evaluates outputs according to three criteria:
  - **instruction following**
  - **naturalness**
  - **coherence**

- The outputs are scored on a **Likert scale from 1 to 7**.

- The judge models are then evaluated by comparing their judgments to human judgments.

- This means the paper treats LLM-as-a-Judge as a **meta-evaluation problem**:
  - first, humans evaluate model outputs;
  - then, LLM judges also evaluate the same outputs;
  - finally, the judge scores are compared with human ratings.
- For **LLM-as-a-Judge for MT**, Even though each replacement increased the correlation with human judgment of translation quality, new concerns have emerged regarding language bias, robustness and self-bias for evaluation

---

## Metrics

- The paper uses human annotations as the reference signal for evaluating judge quality.

- For LLM-as-a-Judge, the key idea is to measure how well judge outputs agree with human judgments.

- In the paper, different subtasks may use different metrics, depending on the task type.

- For judge evaluation, the general goal is to compare:

```text
LLM judge judgment vs human judgment
```

- The paper emphasizes that human annotations are necessary because automatic metrics can be limited, especially for open-ended generation tasks.

---

## Main results / correlations

- The paper finds substantial variation across:
  - subtasks,
  - languages,
  - models,
  - evaluation settings.

- The results show that current LLMs still face persistent challenges in:
  - reasoning,
  - cross-lingual generation,
  - evaluation reliability.

- For OEG, 16 systems, 10 languages and the same 46 questions for all system-language combinations.
    - proprietary models generally perform better, except for DeepSeekV3, which is a large open-source mix-of-expert model
    - performance differences among the leading systems are narrow
    - naturalness scores show a wider spread than instruction following or coherence. 
    -> highlighting the limitations of systems to produce
native sounding text

 

- For LLM-as-a-Judge, the paper highlights that judge reliability is still a challenge, especially in multilingual settings.
    The paper reports two main types of evaluation for LLM-as-a-Judge:

    #### 1. Pairwise Accuracy

    - Used at the system-ranking level.
    - It measures how well the judge’s ranking of systems agrees with the human ranking.
    - Ties are ignored.

    #### 2. acceq

    - Used at the instance/segment level.
    - It is a group-by-item pairwise accuracy with ties.
    - The paper reports acceq separately for each evaluation criterion and also as an average.

- The results show that judge models are roughly split into two groups:
  - large models with more than 100B parameters, including both closed-source and open-source models, achieve high accuracy;
  - small open-source models perform worse, with the lowest performance close to random guessing.

- The best-performing systems at the system level include:
  - Claude 4: Pairwise Accuracy 0.95
  - GPT 4.1: Pairwise Accuracy 0.95
  - CommandA: Pairwise Accuracy 0.93
  - Qwen3 235B: Pairwise Accuracy 0.91

- Smaller models perform lower:
  - Qwen2.5 7B: Pairwise Accuracy 0.70
  - Llama 3.1 8B: Pairwise Accuracy 0.63
  - Mistral 7B: Pairwise Accuracy 0.55

- At the instance level, the differences between top models are smaller.
- The best judge also depends on the criterion:
  - Claude 4 performs best for judging naturalness.
  - GPT 4.1, CommandA, and Qwen3 235B perform best for instruction following and coherence.

- The paper’s results suggest that LLM judges should not be trusted only based on an overall score.

- Their performance needs to be analyzed more carefully by:
  - language,
  - aspect,
  - system-level versus instance-level behavior

---

## Important findings

- Multilingual LLM evaluation is still not fully solved.

- Performance differs strongly across languages and subtasks.

- Human evaluation is important because automatic metrics have limitations.

- Open-ended multilingual generation is difficult because it requires more than just correct content:
  - the answer must also sound natural,
  - be coherent,
  - follow the instruction,
  - and fit the language/culture.

- LLM-as-a-Judge is useful, but its reliability must be tested against human ratings.

- The paper shows that evaluating the evaluator is an important research direction.

- Localized prompts are important because simply translating English prompts may not fully test natural multilingual ability.

---

## Relevance to our project

- This paper is the **main paper** for our project.

- It defines the benchmark and task setup we are working with.

- It explains why Open-Ended Generation is important for multilingual LLM evaluation.

- It defines the key human rating aspects for OEG:
  - coherence,
  - naturalness,
  - instruction following.

- It explains why LLM-as-a-Judge should be evaluated against human judgments.

- The paper also motivates why we should not only report one overall result.

- We should also look at:
  - language-level differences,
  - aspect-level differences,
  - judge reliability,
  - possible evaluation bias.
