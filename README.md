# Legal-Text-Summarizer
A comparative study on different DL based models for summarization of legal texts.

Overview
Legal Text Summarizer is a Deep Learning and NLP-based project that aims to automatically summarize lengthy and complex legal documents into concise, meaningful summaries. Legal texts are often verbose, repetitive, and full of domain-specific jargon, making manual summarization time-consuming and error-prone. This project leverages modern transformer-based models and deep learning architectures to generate summaries that retain essential information and legal context.

Objective

The goal of this project is to:
•	Reduce the reading time for lengthy legal documents.
•	Generate summaries that capture the core legal meaning and context.
•	Experiment with both extractive and abstractive summarization approaches.
•	Evaluate which deep learning model performs best for legal text summarization.

🧩 Approaches Used
🔹 1. Extractive Summarization

Extractive summarization works by identifying the most significant sentences from the original document and concatenating them to form the summary. No new sentences are generated — the model “extracts” rather than “writes.”

Approaches Implemented:
a. BERT (Bidirectional Encoder Representations from Transformers)

BERT is used to obtain contextual embeddings for each sentence. Each sentence is encoded, and cosine similarity with the document embedding is computed. Sentences most similar to the document are selected for the final summary.

b. LexRank

Graph-based algorithm inspired by PageRank. Constructs a similarity graph between sentences and uses eigenvector centrality to identify important sentences.

c. TextRank

Similar to LexRank but based purely on cosine similarity between TF-IDF vectors. Identifies the most central sentences to represent the main theme.

🔹 2. Abstractive Summarization

Abstractive summarization generates summaries that paraphrase and rephrase the content, rather than directly copying sentences. This requires understanding context and semantics at a deeper level.

Approaches Implemented:
a. BART (Bidirectional and Auto-Regressive Transformers)

Combines bidirectional encoding (like BERT) with autoregressive decoding (like GPT). Excels at abstractive summarization and paraphrasing tasks.

b. T5 (Text-to-Text Transfer Transformer)

Converts every NLP task into a text-to-text format. For summarization, the model learns to map “document → summary”. Pretrained on massive text corpora for generalization across domains.

c. PEGASUS

Specifically designed for abstractive summarization. Pretrained using a novel Gap Sentence Generation objective that mimics summary generation. Produces highly fluent and context-aware summaries.

d. LSTM (Long Short-Term Memory Networks)

A Recurrent Neural Network (RNN) variant capable of capturing long-term dependencies. Used in early neural abstractive summarization models before transformers. Encodes input text and decodes it into a summary sequence.
