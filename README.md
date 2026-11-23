# Weight-Space Programming: Papers, Code, Models and Guides

An annotated collection of research on representing and constructing programs in neural-network weights: formal compilation, trained weight generators, LLM reasoning over weights, and experimental feedback.

[Read the guide](https://weightspaceprogramming.tech/) · [Search the collection](https://weightspaceprogramming.tech/research/) · [BibTeX](citations.bib) · [JSON](library.json) · [Dated releases](https://github.com/weightspaceprogramming/reading-list/releases)

34 resources. Updated 2026-11-22.

## Start here

- [How neural networks represent programs](https://weightspaceprogramming.tech/learn/how-neural-networks-represent-programs/) — concepts and concrete examples.
- [Compare construction methods](https://weightspaceprogramming.tech/learn/comparing-methods/) — construction inputs, training, saved artifacts and execution.
- [Choose a reading path](https://weightspaceprogramming.tech/learn/reading-paths/) — routes through the literature.
- [Research history](https://weightspaceprogramming.tech/history/) — contributions, dates and original sources.
- [Build a reusable neural function](https://weightspaceprogramming.tech/build/reusable-neural-function/) — a Program-as-Weights example with a [playground](https://programasweights.com/playground).

## Contents

- [Foundations and formal compilation](#foundations-and-formal-compilation)
- [Trained compilers and weight generators](#trained-compilers-and-weight-generators)
- [LLM reasoning over weights and experimental feedback](#llm-reasoning-over-weights-and-experimental-feedback)
- [Replications, criticism and responses](#replications-criticism-and-responses)
- [Tutorials, tools and collections](#tutorials-tools-and-collections)

Dates below are the first public dates recorded for each resource; conference years are shown separately.

## Foundations and formal compilation

### [Learning to Control Fast-Weight Memories: An Alternative to Dynamic Recurrent Networks](https://people.idsia.ch/~juergen/fastweights/)

Jürgen Schmidhuber.

Neural Computation · 1992

An early weight-generating system: one network learns to change another network’s weights, using those changes as temporary memory.

[Paper and abstract](https://people.idsia.ch/~juergen/fastweights/) · [Research profile](https://weightspaceprogramming.tech/research/fast-weight-memories/)

### [A Neural Compiler](https://blob.lisn.upsaclay.fr/publication/tcs.pdf)

Frédéric Gruau, Jean-Yves Ratajszczak, Gilles Wiber.

Theoretical Computer Science · 1995

Translates Pascal programs into neural networks that implement their computations.

[Full paper](https://blob.lisn.upsaclay.fr/publication/tcs.pdf) · [Research profile](https://weightspaceprogramming.tech/research/a-neural-compiler/)

### [Thinking Like Transformers](https://proceedings.mlr.press/v139/weiss21a.html)

Gail Weiss, Yoav Goldberg, Eran Yahav.

ICML 2021 · 2021-06-13

Introduces RASP, a language for expressing sequence computations in terms of transformer operations.

[Published paper](https://proceedings.mlr.press/v139/weiss21a.html) · [Original preprint](https://arxiv.org/abs/2106.06981) · [Research profile](https://weightspaceprogramming.tech/research/thinking-like-transformers/)

### [Tracr: Compiled Transformers as a Laboratory for Interpretability](https://arxiv.org/abs/2301.05062)

David Lindner, János Kramár, Sebastian Farquhar, Matthew Rahtz, Thomas McGrath, Vladimir Mikulik.

NeurIPS 2023 · 2023-01-12

Compiles RASP programs into transformer weights with known computational structure.

[Paper](https://arxiv.org/abs/2301.05062) · [Full text](https://arxiv.org/html/2301.05062) · [Code](https://github.com/google-deepmind/tracr) · [Research profile](https://weightspaceprogramming.tech/research/tracr/)

## Trained compilers and weight generators

### [HyperNetworks](https://arxiv.org/abs/1609.09106)

David Ha, Andrew Dai, Quoc V. Le.

ICLR 2017 · 2016-09-27

Uses one neural network to generate the weights of another.

[Paper](https://arxiv.org/abs/1609.09106) · [Research profile](https://weightspaceprogramming.tech/research/hypernetworks/)

### [Learning to Generate Task-Specific Adapters from Task Description](https://aclanthology.org/2021.acl-short.82/)

Qinyuan Ye, Xiang Ren.

ACL-IJCNLP 2021 · 2021-01-02

Introduces Hypter, which generates adapters from natural-language task descriptions.

[Published paper](https://aclanthology.org/2021.acl-short.82/) · [Paper](https://arxiv.org/abs/2101.00420) · [Code](https://github.com/INK-USC/hypter) · [Research profile](https://weightspaceprogramming.tech/research/hypter/)

### [HyperTuning: Toward Adapting Large Language Models without Back-propagation](https://proceedings.mlr.press/v202/phang23a.html)

Jason Phang, Yi Mao, Pengcheng He, Weizhu Chen.

ICML 2023 · 2022-11-22

Produces task-specific parameters for a frozen language model from a few demonstrations.

[Published paper](https://proceedings.mlr.press/v202/phang23a.html) · [Paper](https://arxiv.org/abs/2211.12485) · [Research profile](https://weightspaceprogramming.tech/research/hypertuning/)

### [HINT: Hypernetwork Instruction Tuning for Efficient Zero- & Few-Shot Generalisation](https://aclanthology.org/2023.acl-long.631/)

Hamish Ivison, Akshita Bhagia, Yizhong Wang, Hannaneh Hajishirzi, Matthew Peters.

ACL 2023 · 2022-12-20

Turns instructions and examples into reusable prefixes, adapters, and encoded instruction representations.

[Published paper](https://aclanthology.org/2023.acl-long.631/) · [Paper](https://arxiv.org/abs/2212.10315) · [Research profile](https://weightspaceprogramming.tech/research/hint/)

### [Text-to-LoRA: Instant Transformer Adaption](https://proceedings.mlr.press/v267/charakorn25a.html)

Rujikorn Charakorn, Edoardo Cetin, Yujin Tang, Robert Tjarko Lange.

ICML 2025 · 2025-06-06

Uses a hypernetwork to generate LoRA adapters from task descriptions.

[Published paper](https://proceedings.mlr.press/v267/charakorn25a.html) · [Paper](https://arxiv.org/abs/2506.06105) · [Code](https://github.com/SakanaAI/text-to-lora) · [Model checkpoints](https://huggingface.co/SakanaAI/text-to-lora) · [Research profile](https://weightspaceprogramming.tech/research/text-to-lora/)

### [Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution](https://arxiv.org/abs/2606.06492)

Liliana Hotsko, Yinxi Li, Yuntian Deng, Pengyu Nie.

arXiv · 2026-06-04

Trains a hypernetwork to generate repository-specific LoRA adapters from source code and update them as commits arrive.

[Paper](https://arxiv.org/abs/2606.06492) · [Full text](https://arxiv.org/html/2606.06492v2) · [Research profile](https://weightspaceprogramming.tech/research/code-to-lora/)

### [Program-as-Weights: A Programming Paradigm for Fuzzy Functions](https://arxiv.org/abs/2607.02512)

Wentao Zhang, Liliana Hotsko, Woojeong Kim, Pengyu Nie, Stuart Shieber, Yuntian Deng.

NeurIPS 2026 · 2026-07-02

Proposes fuzzy-function programming: compile a natural-language function specification into a neural program, then reuse it locally. Establishes a compiler–interpreter interface and releases FuzzyBench.

[Paper](https://arxiv.org/abs/2607.02512) · [Python SDK](https://github.com/programasweights/programasweights-python) · [SDK reference](https://programasweights.readthedocs.io/en/latest/api-reference/python-sdk/) · [Original full text](https://arxiv.org/html/2607.02512v1) · [Project](https://programasweights.com) · [Demo](https://programasweights.com/playground) · [Local compiler](https://github.com/programasweights/compiler) · [Current full text](https://arxiv.org/html/2607.02512v2) · [Standard compiler checkpoint](https://huggingface.co/programasweights/paw-4b-qwen3-0.6b) · [Compact compiler checkpoint](https://huggingface.co/programasweights/paw-4b-gpt2) · [Qwen3-0.6B interpreter](https://huggingface.co/programasweights/Qwen3-0.6B-GGUF-Q6_K) · [GPT-2 interpreter](https://huggingface.co/programasweights/GPT2-GGUF-Q8_0) · [FuzzyBench verified evaluation data](https://huggingface.co/datasets/yuntian-deng/fuzzy_bench_verified) · [FuzzyBench train, validation and test data](https://huggingface.co/datasets/wtzhang-nlp/fuzzy_bench) · [Research profile](https://weightspaceprogramming.tech/research/program-as-weights/)

### [Compile by Training: Turning Natural-Language Specifications into Local Neural Functions](https://aclanthology.org/2026.emnlp-demos.78/)

Yuntian Deng, Pengyu Nie, Stuart Shieber.

EMNLP 2026 System Demonstrations · 2026-09-03

Compiles a function description into a reusable local program by generating training examples and optimizing an adapter.

[Paper](https://aclanthology.org/2026.emnlp-demos.78/) · [Code](https://github.com/programasweights/compile-by-training) · [Original full text](https://arxiv.org/html/2609.04199v1) · [Research profile](https://weightspaceprogramming.tech/research/compile-by-training/)

## LLM reasoning over weights and experimental feedback

### [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/)

Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab.

Research article · 2026-11-02

A general-purpose LLM reads numerical weights, constructs networks, and edits a language model. Tool access varies by experiment, from no tools to Python and limited model executions.

[Original article](https://rikiyat.github.io/blog/weight-space-programming/) · [Experiment logs and code](https://github.com/RikiyaT/lm_understand-logs) · [Edited Qwen model](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming) · [Community model-comparison demo](https://huggingface.co/spaces/akhaliq/weight-space-programming-demo) · [Research profile](https://weightspaceprogramming.tech/research/sparks-weight-space-programming/)

### [Weight-Space Programming from scratch on simple tasks](https://csinva.io/weight-space-programming-autoresearch/analyze/toy_examples/report.html)

Chandan Singh.

Research article · 2026-11-02

An LLM coding agent writes transformer weights for tasks such as addition, sorting, and parity, then revises the programs using evaluation feedback.

[Original article](https://csinva.io/weight-space-programming-autoresearch/analyze/toy_examples/report.html) · [Code](https://github.com/csinva/weight-space-programming-autoresearch) · [Research profile](https://weightspaceprogramming.tech/research/weight-space-programming-simple-tasks/)

### [WeightLoop: Weight-Space Programming with Experimental Feedback](https://arxiv.org/abs/2611.07319)

Mengran Li, Bo Li, Weijing Zhao, Chengyang Zhang, Boyu Zhang, Jinfeng Xu, Zelin Zang, Victor C. M. Leung, Stan Z. Li.

arXiv · 2026-11-05

Builds reusable update programs that turn experimental measurements into persistent corrections to scientific predictors.

[Paper](https://arxiv.org/abs/2611.07319) · [Full text](https://arxiv.org/html/2611.07319v2) · [Code](https://github.com/limengran98/WeightLoop) · [Research profile](https://weightspaceprogramming.tech/research/weightloop/)

### [Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations](https://arxiv.org/abs/2611.09382)

Junru Hu, Cheng Tang, Wei Li, Hongze Zhu, Chun-Mei Feng, Qi Zhang, Yirong Chen, Ming Hu.

arXiv · 2026-11-06

Studies direct weight editing across 16 searches, seven benchmark families, and two model scales, measuring held-out gains and transfer between tasks.

[Paper](https://arxiv.org/abs/2611.09382) · [Full text](https://arxiv.org/html/2611.09382v1) · [Project repository](https://github.com/WSP-Scope/WSP-Scope-Project) · [Research profile](https://weightspaceprogramming.tech/research/exploring-weight-space-programming/)

### [Weight-Space Programming of Policies and Their Verification via Model Checking](https://arxiv.org/abs/2611.11604)

Dennis Gross.

arXiv · 2026-11-08

Combines LLM-written neural policies with probabilistic model checking and feedback-driven repair.

[Paper](https://arxiv.org/abs/2611.11604) · [Full text](https://arxiv.org/html/2611.11604v1) · [Code: WSP branch](https://github.com/LAVA-LAB/COOL-MC/tree/wsp_verified) · [Research profile](https://weightspaceprogramming.tech/research/weight-space-policy-verification/)

### [Interpretable weight-space programming builds transparent transformers and brain encoding models](https://arxiv.org/abs/2611.18114)

Yash Mehta, Chandan Singh, Weijia Xu, Richard J. Antonello, Adeen Flinker, Nima Mesgarani, Michael F. Bonner, Nebojsa Jojic, Jianfeng Gao.

arXiv · 2026-11-13

An LLM agent constructs interpretable transformers and brain-encoding features by writing their computations and weights in code.

[Paper](https://arxiv.org/abs/2611.18114) · [Full text](https://arxiv.org/html/2611.18114v1) · [Code](https://github.com/csinva/weight-space-programming-autoresearch) · [Research profile](https://weightspaceprogramming.tech/research/interpretable-weight-space-programming/)

### [WeightBench: Evaluating Language Models as Weight-Space Programmers](https://arxiv.org/abs/2611.18553)

Aayush Marasini, Barsat Khadka, Nick Rahimi.

arXiv · 2026-11-13

Evaluates language-model agents on 42 tasks covering weight reading, repair, construction, impossible edits, and data-free compression.

[Paper](https://arxiv.org/abs/2611.18553) · [Full text](https://arxiv.org/html/2611.18553v1) · [Code and benchmark](https://github.com/Aayush-Marasini/WeightBench) · [Research profile](https://weightspaceprogramming.tech/research/weightbench/)

### [Zero-Shot Weight-Space Programming for Prediction and Classification of Target Variables in Structured Datasets](https://arxiv.org/abs/2611.19292)

Eduardo C. Garrido-Merchán.

arXiv · 2026-11-14

Tests whether an LLM can infer a predictor from structured examples and write every network parameter as a literal number.

[Paper](https://arxiv.org/abs/2611.19292) · [Full text](https://arxiv.org/html/2611.19292v2) · [Research profile](https://weightspaceprogramming.tech/research/zero-shot-structured-data/)

### [Weight-space programming for tractor guidance controller: large language models natively write neural network weights that steer a real tractor](https://arxiv.org/abs/2611.21958)

Timo Oksanen.

arXiv · 2026-11-16

Uses LLM-written neural-network weights to repair and construct a tractor steering controller, with simulation and real-tractor evaluation.

[Paper](https://arxiv.org/abs/2611.21958) · [Full text](https://arxiv.org/html/2611.21958v1) · [Research profile](https://weightspaceprogramming.tech/research/weight-space-tractor-control/)

### [What Does Weight-Space Programming Add to Diffusion Editing? Program Construction versus Score-Guided Refinement](https://arxiv.org/abs/2611.22228)

Zitian Gao, Jingyi Xu, Ziqi Han, Chengkai Lei, Ye Liu, Liangliang Shi.

arXiv · 2026-11-17

Separates LLM program construction from score-guided refinement in diffusion concept editing.

[Paper](https://arxiv.org/abs/2611.22228) · [Full text](https://arxiv.org/html/2611.22228v1) · [Research profile](https://weightspaceprogramming.tech/research/weight-space-diffusion-editing/)

### [Weight-Space Programming Doesn't Need Transformers](https://arxiv.org/abs/2611.22055)

Hyunjong Ok, Jaeho Lee.

arXiv · 2026-11-17

Compares fixed transformers with architectures designed by LLM weight writers, including sparse tables and associative-memory models.

[Paper](https://arxiv.org/abs/2611.22055) · [Full text](https://arxiv.org/html/2611.22055v1) · [Code](https://github.com/effl-lab/Weight-Space-Programming) · [Research profile](https://weightspaceprogramming.tech/research/weight-space-without-transformers/)

### [WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming](https://arxiv.org/abs/2611.25476)

Bo Li, Taoyong Cui, Bob Zhang, Mengran Li, Chengyang Zhang, Yang Zhang, Pheng Ann Heng, Wanli Ouyang, Zhenfei Yin, Yingcheng Wu, Ling Yang.

arXiv · 2026-11-19

A frozen language model writes reusable programs that construct weight updates for trained networks.

[Paper](https://arxiv.org/abs/2611.25476) · [Full text](https://arxiv.org/html/2611.25476v1) · [Code](https://github.com/Gen-Verse/WeightCode) · [Data and experiment artifacts](https://huggingface.co/datasets/Boom5426/WeightCode) · [Research profile](https://weightspaceprogramming.tech/research/weightcode/)

## Replications, criticism and responses

### [The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading)

Matthew Honnibal.

honnibal.dev · 2026-11-03

Separates the Sparks experiments by raw-weight access, Python tools and forward-pass feedback, and challenges presenting them as one capability.

[Original critique](https://honnibal.dev/blog/astra-read-write-misleading) · [Research profile](https://weightspaceprogramming.tech/research/honnibal-sparks-critique/)

### [LLMs are not superhuman at reading and writing neural network weights](https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/)

Sean Goedecke.

seangoedecke.com · 2026-11-03

Questions the superhuman-research interpretation of Sparks, examining input-layer heatmaps and the relationship between Qwen repair and established steering methods.

[Original critique](https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/) · [Research profile](https://weightspaceprogramming.tech/research/goedecke-superhuman-critique/)

### [Qwen 3.8 27B on my laptop can interpret model weights, too](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/)

Simon Willison.

Simon Willison’s Weblog · 2026-11-03

Re-runs the Sparks game-identification prompts with a local Qwen3.8 27B model, publishing commands and model responses.

[Original article](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/) · [Research profile](https://weightspaceprogramming.tech/research/willison-local-weight-reading/)

### [Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](https://arxiv.org/abs/2611.08070)

Nazmus Sakib Ahmed.

arXiv · 2026-11-05

Audits whether zero-shot neural-weight interpretation reflects computation tracing or local arithmetic and familiar-dataset priors.

[Paper](https://arxiv.org/abs/2611.08070) · [Full text](https://arxiv.org/html/2611.08070v1) · [Research profile](https://weightspaceprogramming.tech/research/weight-reading-audit/)

### [Sparks of Weight-Space Programming: Response to Comments](https://rikiyat.github.io/blog/weight-space-programming/)

Rikiya Takehi, Jayden Teoh, Alex Zhang, Omar Khattab.

Update to Sparks of Weight-Space Programming · 2026-11-12

The authors’ response distinguishes weight-space programming as a capability from any single experimental method.

[Response in the original article](https://rikiyat.github.io/blog/weight-space-programming/) · [Research profile](https://weightspaceprogramming.tech/research/sparks-response-to-comments/)

### [Replicating and Extending Weight-Space Programming: Frontier LLMs Compile Programs into Weights and Read Input Layers](https://borowiecki.dev/pdf/2611.21449)

Roksana Goworek, Alexander Hickey, Federico Nanni, Martin O’Reilly.

arXiv · 2026-11-16

Replicates weight construction and reading, then tests changed games, ordinary-code policies and shuffled-weight controls.

[Full paper](https://borowiecki.dev/pdf/2611.21449) · [Research profile](https://weightspaceprogramming.tech/research/replicating-weight-space-programming/)

## Tutorials, tools and collections

### [Weight-Space Programming — From Neural Programs to Qwen Repair](https://az9713.github.io/weight-space-programming/weight-space-programming-tutorial.html)

AZ9713.

Interactive tutorial

An illustrated walkthrough of network construction, raw-weight interpretation and Qwen repair, with labs based on released experiment artifacts.

[Interactive tutorial](https://az9713.github.io/weight-space-programming/weight-space-programming-tutorial.html) · [Research profile](https://weightspaceprogramming.tech/research/wsp-visual-tutorial/)

### [wsp — weight space programming](https://github.com/mfaseehuddin/wsp)

mfaseehuddin.

GitHub implementation

Community experiment harnesses, agent prompts and results for explaining, constructing and modifying neural-network weights.

[Implementation and experiments](https://github.com/mfaseehuddin/wsp) · [Research profile](https://weightspaceprogramming.tech/research/wsp-agent-harnesses/)

### [Awesome Weight-Space Programming](https://github.com/Boom5426/Awesome-Weight-Space-Programming)

Boom5426.

GitHub collection

A bilingual collection covering direct weight programming and related research in generation, editing, merging and continual learning.

[Curated collection](https://github.com/Boom5426/Awesome-Weight-Space-Programming) · [Research profile](https://weightspaceprogramming.tech/research/awesome-wsp-boom5426/)

### [Awesome Weight-Space Programming](https://github.com/brighterr/awesome-wsp)

brighterr.

GitHub collection

A reading collection connecting direct weight programming, community experiments, compilers, weight generation and model editing.

[Curated collection](https://github.com/brighterr/awesome-wsp) · [Research profile](https://weightspaceprogramming.tech/research/awesome-wsp-brighterr/)

## Use the collection

Download `library.json` for stable record IDs, authors, dates, venues, summaries, method descriptions, source links and BibTeX. The `mechanisms`, `operations` and `artifacts` fields support filtering and analysis. `citations.bib` contains the citations for the collected works.

Cite the original work when discussing its contribution. To identify the collection version used in an analysis, link to a dated release or a commit.

To rebuild the README and citations from a local copy of the research records:

```sh
python3 scripts/sync.py --source /path/to/library.json
python3 scripts/sync.py --check
```

Running `python3 scripts/sync.py` without `--source` downloads the guide's public [JSON export](https://weightspaceprogramming.tech/library.json). Python 3 and its standard library are sufficient.

## Contribute

Suggest a paper, implementation, model, critique or correction through an issue or pull request. Include the primary source and a short explanation of the connection. See [CONTRIBUTING.md](CONTRIBUTING.md) for the record format and checks.

Edited by [Yuntian Deng](https://yuntiandeng.com/), a coauthor of [Program-as-Weights](https://programasweights.com/). Read more about the guide on its [About page](https://weightspaceprogramming.tech/about/).
