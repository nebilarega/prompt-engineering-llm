## Business objective

Large Language Models coupled with multiple AI capabilities are able to generate images and text, and also approach/achieve human level performance on a number of tasks. The world is going through a revolution in art (DALL-E, MidJourney, Imagine, etc.), science (AlphaFold), medicine, and other key areas, and this approach is playing a role in this revolution.
.
In-context learning, popularized by the team behind the GPT-3 LLM, brought a new revolution for using LLMs in many tasks that the LLM was not originally not trained for. This stands in contrast to the usual fine-tuning that used to be required to equip AI models to improve performance in tasks they were not trained for.

With in-context learning, LLMs are able to constantly adjust their performance on a task depending on the prompt - from structured input that can be considered partly a few-shot training and partly a test input. This has opened up many applications.

This week’s challenge is to systematically explore strategies that help generate prompts for LLMs to extract relevant entities from job descriptions and also to classify web pages given only a few examples of human scores. You will be also required to compare responses and accuracies of multiple LLM models for given prompts.

## Project Overview

A client has a system that collects news artifacts from web pages, tweets, facebook posts, etc. The client is interested in scoring a given new artifact against a topic. The client has hired experts to score a few of these news items in the range from 0 to 10; a score of 0 means the news item is totally NOT relevant while a score of 10 means the news item is very relevant. The range of results between 0 and 10 signifies the degree of relevance of the news item to the topic. The client wants to explore how useful existing LLMs such as GPT-3 are for this task. You are hired as a consultant to explore the efficiency of GPT3-like LLMs to this task. If your recommendation is positive, you must demonstrate that your strategies to design prompts are reproducible and produce a consistent result.
