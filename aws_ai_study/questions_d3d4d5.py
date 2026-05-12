D3_QUESTIONS = [
    # --- 3.1 Text generation applications (7 questions) ---
    {
        "id": "d3_001",
        "domain": 3,
        "subdomain": "3.1",
        "difficulty": "foundational",
        "text": "A company wants to build a customer-facing chatbot that answers product questions using a foundation model on Amazon Bedrock. Which inference parameter should they lower to make the chatbot's responses more deterministic and factual?",
        "choices": [
            "Top K",
            "Temperature",
            "Max tokens",
            "Stop sequences"
        ],
        "correct_index": 1,
        "explanation": "Temperature controls the randomness of model output. A lower temperature (closer to 0) makes the model select higher-probability tokens, producing more deterministic and factually grounded responses. This is ideal for customer-facing chatbots where consistency and accuracy matter more than creativity."
    },
    {
        "id": "d3_002",
        "domain": 3,
        "subdomain": "3.1",
        "difficulty": "intermediate",
        "text": "A developer is using Amazon Bedrock to generate code and notices the model sometimes produces syntactically incorrect output that gets cut off mid-function. Which parameter adjustment is most likely to resolve this?",
        "choices": [
            "Decrease the temperature to 0",
            "Increase the max tokens parameter",
            "Add a system prompt instructing the model to be concise",
            "Switch from on-demand to provisioned throughput"
        ],
        "correct_index": 1,
        "explanation": "When model output is cut off mid-generation, it typically means the response has hit the maximum token limit. Increasing the max tokens parameter allows the model to generate longer responses, which is especially important for code generation where functions and classes can be lengthy. Temperature and throughput settings would not address truncation."
    },
    {
        "id": "d3_003",
        "domain": 3,
        "subdomain": "3.1",
        "difficulty": "foundational",
        "text": "Which Amazon Bedrock capability allows a company to summarize lengthy legal documents into concise briefs without writing custom ML training code?",
        "choices": [
            "Amazon Bedrock model fine-tuning",
            "Amazon Bedrock foundation model inference with an appropriate prompt",
            "Amazon SageMaker built-in summarization algorithm",
            "Amazon Comprehend key phrase extraction"
        ],
        "correct_index": 1,
        "explanation": "Foundation models available through Amazon Bedrock can perform text summarization out of the box by providing an appropriate prompt, with no custom training required. This is a core capability of large language models and is one of the most straightforward text generation use cases. Fine-tuning would be unnecessary for general summarization tasks."
    },
    {
        "id": "d3_004",
        "domain": 3,
        "subdomain": "3.1",
        "difficulty": "intermediate",
        "text": "A global e-commerce company needs to translate product descriptions from English into 12 languages while maintaining brand voice and terminology. Which approach on AWS is most appropriate?",
        "choices": [
            "Use Amazon Translate with custom terminology files for each language",
            "Use a foundation model on Amazon Bedrock with few-shot prompting that includes brand-specific translation examples",
            "Train a custom neural machine translation model on Amazon SageMaker",
            "Use Amazon Comprehend to detect language and then apply rule-based translation"
        ],
        "correct_index": 1,
        "explanation": "Foundation models excel at translation tasks where context, tone, and brand voice matter. By using few-shot prompting with examples of desired translations that reflect the brand's style and terminology, the model can maintain consistent brand voice across languages without custom training. Amazon Translate handles general translation well but has less flexibility for nuanced brand voice adaptation."
    },
    {
        "id": "d3_005",
        "domain": 3,
        "subdomain": "3.1",
        "difficulty": "foundational",
        "text": "What is the primary purpose of a system prompt when using a foundation model for a Q&A chatbot?",
        "choices": [
            "To encrypt the conversation between the user and the model",
            "To define the model's persona, behavior guidelines, and response constraints",
            "To increase the model's token processing speed",
            "To store the conversation history in a database"
        ],
        "correct_index": 1,
        "explanation": "A system prompt sets the context, persona, and behavioral guardrails for a foundation model. It tells the model how to behave, what role to assume, what topics to avoid, and how to format responses. This is essential for building reliable Q&A chatbots that stay on topic and respond in the desired tone."
    },
    {
        "id": "d3_006",
        "domain": 3,
        "subdomain": "3.1",
        "difficulty": "intermediate",
        "text": "A developer is building a content creation tool that generates marketing copy. They want the model to produce creative and varied outputs for each run. Which combination of inference parameters should they adjust?",
        "choices": [
            "Increase temperature and increase top P",
            "Decrease temperature and decrease top P",
            "Increase max tokens and add stop sequences",
            "Decrease top K and set temperature to 0"
        ],
        "correct_index": 0,
        "explanation": "Higher temperature increases randomness in token selection, and higher top P (nucleus sampling) allows the model to consider a wider range of probable tokens. Together, these settings produce more creative, diverse, and varied outputs. Lowering temperature or top P would make outputs more deterministic and repetitive, which is the opposite of what creative content generation requires."
    },
    {
        "id": "d3_007",
        "domain": 3,
        "subdomain": "3.1",
        "difficulty": "foundational",
        "text": "Which of the following is an example of zero-shot prompting?",
        "choices": [
            "Providing the model with 5 example customer reviews and their sentiment labels before asking it to classify a new review",
            "Asking the model to classify the sentiment of a review without providing any examples",
            "Fine-tuning a model on thousands of labeled sentiment examples before deployment",
            "Using a retrieval-augmented approach to find similar classified reviews first"
        ],
        "correct_index": 1,
        "explanation": "Zero-shot prompting means asking the model to perform a task without providing any examples in the prompt. The model relies entirely on its pre-trained knowledge to understand and execute the instruction. This contrasts with few-shot prompting, which includes examples, and fine-tuning, which involves additional training on task-specific data."
    },
    # --- 3.2 RAG and knowledge bases (7 questions) ---
    {
        "id": "d3_008",
        "domain": 3,
        "subdomain": "3.2",
        "difficulty": "foundational",
        "text": "What is the primary purpose of Retrieval-Augmented Generation (RAG)?",
        "choices": [
            "To train a foundation model from scratch on company-specific data",
            "To reduce the cost of model inference by caching responses",
            "To supplement a foundation model's responses with relevant information retrieved from external knowledge sources",
            "To convert unstructured data into structured database records"
        ],
        "correct_index": 2,
        "explanation": "RAG combines a retrieval mechanism with a generative model so that responses are grounded in relevant, up-to-date information from external knowledge sources. This reduces hallucinations and allows the model to answer questions about data it was never trained on, such as proprietary company documents. RAG does not retrain the model; it augments the prompt with retrieved context."
    },
    {
        "id": "d3_009",
        "domain": 3,
        "subdomain": "3.2",
        "difficulty": "intermediate",
        "text": "In a RAG architecture, what role do vector embeddings play?",
        "choices": [
            "They encrypt document contents for secure storage in the knowledge base",
            "They convert text into numerical representations that capture semantic meaning, enabling similarity-based retrieval",
            "They compress documents to reduce storage costs in Amazon S3",
            "They translate documents into multiple languages before indexing"
        ],
        "correct_index": 1,
        "explanation": "Vector embeddings are dense numerical representations of text that capture semantic meaning in a high-dimensional space. When a user query is also converted to an embedding, the system can find documents with similar meaning by calculating vector distance, even if the exact words differ. This semantic search capability is what makes RAG effective at retrieving relevant context."
    },
    {
        "id": "d3_010",
        "domain": 3,
        "subdomain": "3.2",
        "difficulty": "foundational",
        "text": "A company wants to build a RAG-based application that answers employee questions using internal HR policy documents stored in Amazon S3. Which AWS service provides a managed solution for this?",
        "choices": [
            "Amazon Comprehend",
            "Amazon Bedrock Knowledge Bases",
            "Amazon Textract",
            "Amazon Kendra"
        ],
        "correct_index": 1,
        "explanation": "Amazon Bedrock Knowledge Bases is a fully managed RAG service that can ingest documents from Amazon S3, automatically generate embeddings, store them in a vector database, and retrieve relevant chunks at query time to augment foundation model responses. It handles the entire RAG pipeline without requiring custom infrastructure. While Amazon Kendra also provides search, Bedrock Knowledge Bases integrates directly with foundation models for generative responses."
    },
    {
        "id": "d3_011",
        "domain": 3,
        "subdomain": "3.2",
        "difficulty": "intermediate",
        "text": "When configuring a knowledge base in Amazon Bedrock, a developer needs to choose a chunking strategy for large PDF documents. Which chunking approach would best preserve the context of information within individual sections of a technical manual?",
        "choices": [
            "Fixed-size chunking with 100-token chunks and no overlap",
            "Hierarchical chunking that respects document structure such as headings and sections",
            "Single-chunk strategy that keeps each entire document as one chunk",
            "Character-level chunking with 50-character segments"
        ],
        "correct_index": 1,
        "explanation": "Hierarchical chunking respects the natural structure of documents by splitting along headings, sections, and paragraphs. For technical manuals where information is organized by topic under section headers, this approach preserves the semantic coherence within each chunk. Fixed-size chunking can split mid-sentence or mid-concept, and single-chunk strategies may exceed token limits or dilute retrieval precision."
    },
    {
        "id": "d3_012",
        "domain": 3,
        "subdomain": "3.2",
        "difficulty": "intermediate",
        "text": "Which vector database option is natively supported as a vector store for Amazon Bedrock Knowledge Bases?",
        "choices": [
            "Amazon ElastiCache for Redis",
            "Amazon OpenSearch Serverless with vector engine",
            "Amazon DynamoDB with GSI",
            "Amazon Neptune"
        ],
        "correct_index": 1,
        "explanation": "Amazon OpenSearch Serverless with the vector engine is one of the natively supported vector stores for Amazon Bedrock Knowledge Bases. It provides serverless vector search capabilities that integrate directly with the Knowledge Bases service for storing and querying embeddings. Other supported options include Amazon Aurora PostgreSQL with pgvector and Pinecone, but ElastiCache, DynamoDB, and Neptune are not supported as vector stores for this service."
    },
    {
        "id": "d3_013",
        "domain": 3,
        "subdomain": "3.2",
        "difficulty": "foundational",
        "text": "What is a key advantage of using RAG over fine-tuning a foundation model for answering questions about frequently updated company data?",
        "choices": [
            "RAG produces faster inference responses than a fine-tuned model",
            "RAG allows the model to access current information without retraining, since the knowledge base can be updated independently",
            "RAG eliminates the need for a foundation model entirely",
            "RAG automatically improves model accuracy over time through reinforcement learning"
        ],
        "correct_index": 1,
        "explanation": "RAG decouples the knowledge source from the model itself, so when company data changes, only the knowledge base needs to be updated rather than retraining or fine-tuning the model. This makes RAG ideal for data that changes frequently, such as product catalogs, policies, or documentation. Fine-tuning bakes knowledge into model weights, which becomes stale as source data evolves."
    },
    {
        "id": "d3_014",
        "domain": 3,
        "subdomain": "3.2",
        "difficulty": "intermediate",
        "text": "A RAG application is returning irrelevant documents that share keywords with the query but differ in meaning. What is the most likely cause and fix?",
        "choices": [
            "The foundation model needs fine-tuning; switch to a custom-trained model",
            "The embedding model produces poor semantic representations; switch to a higher-quality embedding model or adjust the similarity threshold",
            "The documents are too large; increase the chunk size to include more context",
            "The vector database is running out of storage; migrate to a larger instance"
        ],
        "correct_index": 1,
        "explanation": "When retrieval returns keyword-matching but semantically irrelevant results, the embedding model may not be capturing meaning well enough to distinguish between different uses of the same words. Upgrading to a higher-quality embedding model that better captures semantic nuance, or adjusting the similarity score threshold to be more strict, can improve retrieval relevance. This is a retrieval quality issue, not a generation or storage issue."
    },
    # --- 3.3 AI agents and reasoning (7 questions) ---
    {
        "id": "d3_015",
        "domain": 3,
        "subdomain": "3.3",
        "difficulty": "foundational",
        "text": "What distinguishes an AI agent from a standard foundation model inference call?",
        "choices": [
            "An AI agent uses a smaller, more efficient model than standard inference",
            "An AI agent can plan multi-step tasks, use tools, and take actions to accomplish a goal autonomously",
            "An AI agent can only process structured data, while standard inference handles unstructured text",
            "An AI agent requires GPUs for inference while standard calls use CPUs"
        ],
        "correct_index": 1,
        "explanation": "AI agents extend foundation model capabilities by adding the ability to reason about tasks, break them into steps, select and use external tools or APIs, and iterate until a goal is achieved. Unlike a single inference call that produces one response, an agent orchestrates multiple steps and tool invocations. This makes agents suitable for complex tasks that require planning and interaction with external systems."
    },
    {
        "id": "d3_016",
        "domain": 3,
        "subdomain": "3.3",
        "difficulty": "intermediate",
        "text": "In Amazon Bedrock Agents, what is the purpose of an action group?",
        "choices": [
            "To define IAM permissions that control which users can invoke the agent",
            "To specify a set of actions the agent can perform, defined by API schemas that map to Lambda functions or other endpoints",
            "To group multiple foundation models together for ensemble inference",
            "To batch multiple user requests for cost-efficient processing"
        ],
        "correct_index": 1,
        "explanation": "Action groups in Amazon Bedrock Agents define the tools and capabilities available to the agent. Each action group contains an API schema (such as an OpenAPI schema) that describes available operations, and maps them to backend implementations like AWS Lambda functions. When the agent determines it needs to take an action, it selects the appropriate action group and invokes the corresponding API."
    },
    {
        "id": "d3_017",
        "domain": 3,
        "subdomain": "3.3",
        "difficulty": "foundational",
        "text": "A company wants an AI agent that can look up order status, process returns, and update shipping addresses by calling existing backend APIs. Which AWS service should they use?",
        "choices": [
            "Amazon Lex",
            "Amazon Bedrock Agents",
            "Amazon SageMaker Endpoints",
            "AWS Step Functions"
        ],
        "correct_index": 1,
        "explanation": "Amazon Bedrock Agents is designed for building AI agents that can reason about user requests and take actions by calling backend APIs through action groups. The agent uses a foundation model to understand the user's intent, plan the necessary steps, and invoke the appropriate APIs for tasks like order lookup, returns processing, and address updates. Amazon Lex is a chatbot service but lacks the autonomous reasoning and multi-step planning capabilities of Bedrock Agents."
    },
    {
        "id": "d3_018",
        "domain": 3,
        "subdomain": "3.3",
        "difficulty": "intermediate",
        "text": "How does Amazon Bedrock Agents handle the orchestration of multi-step tasks?",
        "choices": [
            "It requires the developer to explicitly code every possible step sequence in a workflow definition",
            "It uses a foundation model to reason about the task, decompose it into steps, and dynamically decide which actions to invoke at each step",
            "It sends the entire task to a single Lambda function that handles all steps sequentially",
            "It uses a pre-defined decision tree that maps user inputs to fixed response paths"
        ],
        "correct_index": 1,
        "explanation": "Amazon Bedrock Agents uses the underlying foundation model's reasoning capabilities to dynamically orchestrate task execution. The agent interprets the user request, determines what information it needs, selects appropriate action groups, invokes them in the right order, and uses the results to inform subsequent steps. This dynamic orchestration means developers do not need to pre-define every possible sequence of actions."
    },
    {
        "id": "d3_019",
        "domain": 3,
        "subdomain": "3.3",
        "difficulty": "intermediate",
        "text": "A Bedrock Agent needs access to both a company knowledge base for policy information and an action group for submitting IT tickets. How should this be configured?",
        "choices": [
            "Create two separate agents, one for knowledge base queries and one for ticket submission, and route requests between them",
            "Associate both the knowledge base and the action group with the same Bedrock Agent so it can use either capability as needed during orchestration",
            "Fine-tune the foundation model to include the policy information so the knowledge base is not needed",
            "Use Amazon Lex to handle the routing between the knowledge base and the action group"
        ],
        "correct_index": 1,
        "explanation": "Amazon Bedrock Agents supports associating multiple knowledge bases and action groups with a single agent. During orchestration, the agent dynamically decides whether to query the knowledge base for information, invoke an action group to perform an action, or do both in sequence. This unified architecture simplifies the design and allows the agent to seamlessly combine knowledge retrieval with action execution."
    },
    {
        "id": "d3_020",
        "domain": 3,
        "subdomain": "3.3",
        "difficulty": "foundational",
        "text": "What is the concept of 'tool use' in the context of foundation models and AI agents?",
        "choices": [
            "The ability of a model to use GPU hardware tools for faster computation",
            "The ability of a model to recognize when it needs external information or actions and invoke APIs, databases, or functions to fulfill the request",
            "The process of using development tools like IDEs to build AI applications",
            "The technique of using multiple models simultaneously for the same task"
        ],
        "correct_index": 1,
        "explanation": "Tool use refers to a foundation model's ability to identify when it cannot answer a question or complete a task with its built-in knowledge alone and instead invoke external tools such as APIs, databases, calculators, or code interpreters. This extends the model's capabilities beyond text generation to include real-world actions and up-to-date information retrieval."
    },
    {
        "id": "d3_021",
        "domain": 3,
        "subdomain": "3.3",
        "difficulty": "intermediate",
        "text": "An Amazon Bedrock Agent occasionally takes an incorrect action because it misinterprets the user's request. Which feature helps a developer inspect and debug the agent's reasoning process?",
        "choices": [
            "Amazon CloudWatch model inference logs",
            "The agent's trace output, which shows the reasoning steps, thought process, and action selections at each orchestration step",
            "Amazon Bedrock model evaluation reports",
            "AWS X-Ray distributed tracing"
        ],
        "correct_index": 1,
        "explanation": "Amazon Bedrock Agents provides a trace feature that exposes the agent's internal reasoning at each step of orchestration, including its thought process, the rationale for selecting specific actions, the inputs and outputs of each action group invocation, and its final response formulation. This visibility is critical for debugging incorrect agent behavior and refining prompts or action group definitions."
    },
    # --- 3.4 Multimodal and image applications (7 questions) ---
    {
        "id": "d3_022",
        "domain": 3,
        "subdomain": "3.4",
        "difficulty": "foundational",
        "text": "What does 'multimodal' mean in the context of foundation models?",
        "choices": [
            "A model that can run on multiple types of hardware simultaneously",
            "A model that can process and generate content across multiple data types such as text, images, and audio",
            "A model that has been trained by multiple organizations collaboratively",
            "A model that supports multiple programming languages for API calls"
        ],
        "correct_index": 1,
        "explanation": "A multimodal model can understand and work with multiple types of data (modalities) such as text, images, audio, and video. For example, a multimodal model can take an image as input and produce a text description, or accept both text and images together to answer visual questions. This is in contrast to unimodal models that work with only one data type."
    },
    {
        "id": "d3_023",
        "domain": 3,
        "subdomain": "3.4",
        "difficulty": "intermediate",
        "text": "A marketing team wants to generate product images from text descriptions using AWS. Which Amazon Bedrock model is purpose-built for text-to-image generation?",
        "choices": [
            "Amazon Titan Text",
            "Anthropic Claude",
            "Amazon Titan Image Generator",
            "AI21 Labs Jurassic"
        ],
        "correct_index": 2,
        "explanation": "Amazon Titan Image Generator is specifically designed for text-to-image generation, allowing users to create realistic images from natural language descriptions. It is available through Amazon Bedrock and supports features like image generation from text prompts, image editing, and image variation. The other models listed are text-focused foundation models that do not generate images."
    },
    {
        "id": "d3_024",
        "domain": 3,
        "subdomain": "3.4",
        "difficulty": "foundational",
        "text": "Which model provider available on Amazon Bedrock is known for its Stable Diffusion family of image generation models?",
        "choices": [
            "Anthropic",
            "Cohere",
            "Stability AI",
            "Meta"
        ],
        "correct_index": 2,
        "explanation": "Stability AI is the creator of the Stable Diffusion family of models, which are widely used for image generation and are available through Amazon Bedrock. These models can generate, modify, and upscale images based on text prompts. Anthropic, Cohere, and Meta primarily offer text-based foundation models through Bedrock."
    },
    {
        "id": "d3_025",
        "domain": 3,
        "subdomain": "3.4",
        "difficulty": "intermediate",
        "text": "A company wants to use a foundation model to analyze photographs of damaged vehicles and generate text descriptions of the damage for insurance claims. Which type of model capability is required?",
        "choices": [
            "Text-to-image generation",
            "Image-to-text (visual understanding and description)",
            "Text summarization",
            "Named entity recognition"
        ],
        "correct_index": 1,
        "explanation": "This use case requires a multimodal model that can accept images as input and produce text descriptions as output, known as image-to-text or visual understanding capability. Models like Anthropic Claude on Amazon Bedrock can analyze images and generate detailed textual descriptions. Text-to-image generation does the reverse (creates images from text) and would not help here."
    },
    {
        "id": "d3_026",
        "domain": 3,
        "subdomain": "3.4",
        "difficulty": "intermediate",
        "text": "Amazon Titan Image Generator includes a built-in watermarking capability. What is the purpose of this feature?",
        "choices": [
            "To add a visible company logo to all generated images",
            "To embed an invisible watermark that helps identify images as AI-generated, supporting responsible AI practices",
            "To compress images for faster delivery over networks",
            "To encrypt image content so only authorized users can view them"
        ],
        "correct_index": 1,
        "explanation": "Amazon Titan Image Generator includes invisible watermarking that embeds a signal in generated images to identify them as AI-created. This supports responsible AI practices by enabling detection of AI-generated content, which helps address concerns about misinformation and deepfakes. The watermark is imperceptible to the human eye but can be detected programmatically."
    },
    {
        "id": "d3_027",
        "domain": 3,
        "subdomain": "3.4",
        "difficulty": "foundational",
        "text": "A developer wants to build an application where users upload a photo of a dish and receive the recipe in text form. Which AI approach best describes this application?",
        "choices": [
            "Text generation using a large language model",
            "Image classification using a convolutional neural network",
            "Multimodal AI that combines image understanding with text generation",
            "Object detection using a computer vision model"
        ],
        "correct_index": 2,
        "explanation": "This application requires a multimodal approach that can understand the visual content of a food photograph and then generate a detailed text recipe based on that understanding. A purely text-based model cannot process images, and a pure image classifier would only label the dish without generating a recipe. Multimodal models bridge both modalities to deliver the complete user experience."
    },
    {
        "id": "d3_028",
        "domain": 3,
        "subdomain": "3.4",
        "difficulty": "intermediate",
        "text": "When using Amazon Titan Image Generator, a user provides both a text prompt and a reference image to guide generation. What is this technique called?",
        "choices": [
            "Zero-shot generation",
            "Image-to-image generation (image conditioning)",
            "Transfer learning",
            "Model distillation"
        ],
        "correct_index": 1,
        "explanation": "Image-to-image generation, also called image conditioning, uses an existing image as a reference along with a text prompt to guide the generation of a new image. The reference image provides structural or stylistic guidance while the text prompt specifies desired changes or characteristics. This is different from pure text-to-image generation, which creates images solely from text descriptions."
    },
]

D4_QUESTIONS = [
    # --- 4.1 Fairness and bias (5 questions) ---
    {
        "id": "d4_001",
        "domain": 4,
        "subdomain": "4.1",
        "difficulty": "foundational",
        "text": "A hiring AI system consistently rates male candidates higher than equally qualified female candidates. What type of bias does this represent?",
        "choices": [
            "Selection bias",
            "Confirmation bias",
            "Gender bias in training data leading to algorithmic discrimination",
            "Survivorship bias"
        ],
        "correct_index": 2,
        "explanation": "When an AI system systematically favors one gender over another for equivalent qualifications, it reflects gender bias that was likely present in the historical training data. If the training data contained patterns where men were historically hired or rated more favorably, the model learns and perpetuates this discriminatory pattern. This is a well-known risk of training models on historical data that reflects societal biases."
    },
    {
        "id": "d4_002",
        "domain": 4,
        "subdomain": "4.1",
        "difficulty": "intermediate",
        "text": "Which AWS service provides pre-training and post-training bias detection capabilities for machine learning models?",
        "choices": [
            "Amazon Rekognition",
            "Amazon SageMaker Clarify",
            "Amazon Macie",
            "AWS Trusted Advisor"
        ],
        "correct_index": 1,
        "explanation": "Amazon SageMaker Clarify is specifically designed to detect bias in both training data (pre-training bias metrics) and model predictions (post-training bias metrics). It computes metrics such as Class Imbalance, Difference in Proportions of Labels, and Disparate Impact to quantify bias across protected groups. It also provides feature attribution explanations to help understand model decisions."
    },
    {
        "id": "d4_003",
        "domain": 4,
        "subdomain": "4.1",
        "difficulty": "foundational",
        "text": "What is 'sampling bias' in the context of training an AI model?",
        "choices": [
            "When the model is trained on too much data, causing overfitting",
            "When the training dataset does not accurately represent the population the model will serve, leading to skewed predictions",
            "When the model randomly samples different answers each time it runs",
            "When data is collected at regular intervals rather than continuously"
        ],
        "correct_index": 1,
        "explanation": "Sampling bias occurs when the training data is not representative of the real-world population. For example, a facial recognition model trained predominantly on lighter-skinned faces will perform poorly on darker-skinned faces. Addressing sampling bias requires ensuring the training dataset includes diverse and proportional representation of all groups the model will encounter in production."
    },
    {
        "id": "d4_004",
        "domain": 4,
        "subdomain": "4.1",
        "difficulty": "intermediate",
        "text": "A data scientist discovers that their loan approval model has a significantly higher false rejection rate for applicants from a specific ethnic group. Which SageMaker Clarify metric would help quantify this disparity?",
        "choices": [
            "Class Imbalance (CI)",
            "Difference in Conditional Acceptance (DCA)",
            "Difference in Proportions of Labels (DPL)",
            "Disparate Impact (DI)"
        ],
        "correct_index": 3,
        "explanation": "Disparate Impact (DI) measures the ratio of favorable outcomes for a disadvantaged group compared to an advantaged group. A DI value significantly below 1.0 indicates that the disadvantaged group receives fewer favorable outcomes proportionally, which is exactly what a higher false rejection rate would show. This metric is widely used in fairness assessments and aligns with the four-fifths rule used in employment discrimination analysis."
    },
    {
        "id": "d4_005",
        "domain": 4,
        "subdomain": "4.1",
        "difficulty": "intermediate",
        "text": "Which of the following is a bias mitigation strategy that can be applied DURING model training?",
        "choices": [
            "Collecting more representative training data",
            "Applying adversarial debiasing where a secondary model penalizes the primary model for biased predictions",
            "Using Amazon Bedrock Guardrails to filter biased outputs",
            "Publishing a model card that documents known biases"
        ],
        "correct_index": 1,
        "explanation": "Adversarial debiasing is an in-training (in-processing) bias mitigation technique where a secondary adversarial model tries to predict protected attributes from the primary model's predictions. The primary model is then penalized for any predictions that allow such inference, encouraging it to make decisions independent of protected attributes. Data collection is a pre-training strategy, and output filtering and model cards are post-training approaches."
    },
    # --- 4.2 Explainability and transparency (5 questions) ---
    {
        "id": "d4_006",
        "domain": 4,
        "subdomain": "4.2",
        "difficulty": "foundational",
        "text": "Why is model explainability important in AI systems used for critical decisions like healthcare diagnoses or loan approvals?",
        "choices": [
            "It makes the model run faster by simplifying its architecture",
            "It allows stakeholders to understand why a model made a particular prediction, building trust and enabling accountability",
            "It automatically improves the model's accuracy over time",
            "It eliminates the need for human oversight of AI decisions"
        ],
        "correct_index": 1,
        "explanation": "Model explainability provides transparency into how and why an AI system reaches its decisions. In high-stakes domains like healthcare and finance, understanding the reasoning behind predictions is essential for building trust with users, meeting regulatory requirements, identifying potential errors or biases, and ensuring appropriate human oversight. Explainability is about understanding, not performance optimization."
    },
    {
        "id": "d4_007",
        "domain": 4,
        "subdomain": "4.2",
        "difficulty": "intermediate",
        "text": "What are SHAP (SHapley Additive exPlanations) values used for in machine learning?",
        "choices": [
            "To measure the training speed of a model across different hardware configurations",
            "To quantify the contribution of each input feature to a specific prediction, providing local feature importance explanations",
            "To compress model weights for faster deployment",
            "To evaluate the statistical significance of A/B test results"
        ],
        "correct_index": 1,
        "explanation": "SHAP values, based on game theory's Shapley values, assign each input feature a value representing its contribution to a specific prediction. A positive SHAP value means the feature pushed the prediction higher, while a negative value means it pushed it lower. Amazon SageMaker Clarify uses SHAP values to provide feature attribution explanations that help data scientists and stakeholders understand which factors drove individual model decisions."
    },
    {
        "id": "d4_008",
        "domain": 4,
        "subdomain": "4.2",
        "difficulty": "foundational",
        "text": "What is a model card?",
        "choices": [
            "A physical ID badge that identifies which team owns an ML model",
            "A documentation artifact that describes a model's purpose, performance, limitations, intended use cases, and ethical considerations",
            "A credit card-sized device that stores model weights for edge deployment",
            "A configuration file that defines model hyperparameters"
        ],
        "correct_index": 1,
        "explanation": "A model card is a standardized documentation practice that provides essential information about an ML model including its intended purpose, training data, performance metrics across different populations, known limitations, and ethical considerations. Model cards promote transparency and help users make informed decisions about whether a model is appropriate for their use case. Amazon SageMaker supports creating and managing model cards."
    },
    {
        "id": "d4_009",
        "domain": 4,
        "subdomain": "4.2",
        "difficulty": "intermediate",
        "text": "A company deploys a complex deep learning model that achieves 98% accuracy but cannot explain its decisions to regulators. What is this tension known as?",
        "choices": [
            "The bias-variance tradeoff",
            "The interpretability-accuracy tradeoff",
            "The precision-recall tradeoff",
            "The latency-throughput tradeoff"
        ],
        "correct_index": 1,
        "explanation": "The interpretability-accuracy tradeoff reflects the common observation that more complex models (like deep neural networks) often achieve higher accuracy but are harder to explain, while simpler models (like linear regression or decision trees) are more interpretable but may sacrifice some predictive power. In regulated industries, this tradeoff must be carefully considered, and techniques like SHAP values or LIME can help add explainability to complex models."
    },
    {
        "id": "d4_010",
        "domain": 4,
        "subdomain": "4.2",
        "difficulty": "intermediate",
        "text": "Which approach helps make a foundation model's text responses more transparent to end users?",
        "choices": [
            "Increasing the model's temperature to produce more varied responses",
            "Including citations or references to source documents when the model uses retrieved information to generate answers",
            "Using a larger model with more parameters",
            "Deploying the model on dedicated hardware for consistent performance"
        ],
        "correct_index": 1,
        "explanation": "Providing citations and source references in generated responses allows users to verify the information and understand where the answer came from. This is particularly valuable in RAG-based applications where the model draws from specific documents. Transparency about sources builds user trust and allows fact-checking, which is a core principle of responsible AI deployment."
    },
    # --- 4.3 AI governance (4 questions) ---
    {
        "id": "d4_011",
        "domain": 4,
        "subdomain": "4.3",
        "difficulty": "foundational",
        "text": "What is the 'human-in-the-loop' approach in AI governance?",
        "choices": [
            "Requiring a human to manually label all training data before model training",
            "Keeping human oversight and review in AI decision-making processes, especially for high-stakes or ambiguous cases",
            "Having a human physically present next to the server running the AI model",
            "Replacing AI models with human workers for all customer interactions"
        ],
        "correct_index": 1,
        "explanation": "Human-in-the-loop is a governance practice where humans maintain oversight over AI decisions, particularly for high-risk, edge-case, or ambiguous situations. This can mean a human reviews AI recommendations before they are acted upon, handles cases where the model's confidence is low, or audits a sample of automated decisions. It balances the efficiency of AI with the judgment and accountability that human oversight provides."
    },
    {
        "id": "d4_012",
        "domain": 4,
        "subdomain": "4.3",
        "difficulty": "intermediate",
        "text": "Amazon Bedrock Guardrails can be configured to filter model inputs and outputs. Which of the following is a capability of Guardrails?",
        "choices": [
            "Automatically fine-tuning the model to avoid generating harmful content",
            "Defining denied topics, content filters for harmful categories, word filters, and sensitive information filters (like PII redaction) that block or mask inappropriate content",
            "Replacing the foundation model with a rules-based system when harmful input is detected",
            "Permanently modifying the model's weights to prevent it from ever producing harmful content"
        ],
        "correct_index": 1,
        "explanation": "Amazon Bedrock Guardrails provides configurable safeguards that evaluate both user inputs and model outputs against policies you define. These include denied topics that the model should refuse to engage with, content filters for categories like violence or hate speech, word-level filters, and sensitive information filters that can detect and redact PII. Guardrails operate at the application layer and do not modify the underlying model."
    },
    {
        "id": "d4_013",
        "domain": 4,
        "subdomain": "4.3",
        "difficulty": "foundational",
        "text": "Which of the following is a core principle of responsible AI that focuses on ensuring AI systems work correctly and reliably?",
        "choices": [
            "Robustness and safety",
            "Cost efficiency",
            "Processing speed",
            "Model size optimization"
        ],
        "correct_index": 0,
        "explanation": "Robustness and safety is a core responsible AI principle that ensures AI systems behave as intended, handle unexpected inputs gracefully, and do not cause harm. This includes testing for edge cases, adversarial inputs, and failure modes. Along with fairness, explainability, privacy, and governance, robustness is one of the pillars of responsible AI frameworks adopted by AWS and the broader industry."
    },
    {
        "id": "d4_014",
        "domain": 4,
        "subdomain": "4.3",
        "difficulty": "intermediate",
        "text": "A company is establishing an AI governance framework. Which practice ensures ongoing accountability for AI systems after deployment?",
        "choices": [
            "Conducting a one-time bias assessment before launch and archiving the results",
            "Implementing continuous monitoring of model performance, fairness metrics, and user feedback with regular human reviews",
            "Restricting model access to a single team to minimize coordination complexity",
            "Using only open-source models to ensure transparency"
        ],
        "correct_index": 1,
        "explanation": "Effective AI governance requires ongoing monitoring and review, not just pre-deployment checks. Continuous monitoring of model performance, fairness metrics, data drift, and user feedback ensures that issues are detected and addressed promptly after deployment. Regular human reviews and audits provide accountability, and feedback loops enable iterative improvement of the AI system over time."
    },
]

D5_QUESTIONS = [
    # --- 5.1 Security for AI (5 questions) ---
    {
        "id": "d5_001",
        "domain": 5,
        "subdomain": "5.1",
        "difficulty": "foundational",
        "text": "A company uses Amazon Bedrock to process sensitive customer data. Which encryption approach ensures data is protected both during transmission and when stored?",
        "choices": [
            "Encrypt data at rest using AWS KMS and enforce TLS 1.2 or higher for data in transit",
            "Use server-side encryption only, since data in transit through AWS services is always unencrypted",
            "Rely on the foundation model to encrypt the data as part of its processing",
            "Use client-side encryption only and disable server-side encryption to avoid double encryption"
        ],
        "correct_index": 0,
        "explanation": "A defense-in-depth approach requires encrypting data at rest using AWS Key Management Service (KMS) and encrypting data in transit using TLS (Transport Layer Security). Amazon Bedrock encrypts data at rest by default with AWS-managed keys and supports customer-managed KMS keys for additional control. All API calls to Bedrock use TLS encryption for data in transit."
    },
    {
        "id": "d5_002",
        "domain": 5,
        "subdomain": "5.1",
        "difficulty": "intermediate",
        "text": "A security team needs to ensure that calls to Amazon Bedrock foundation models from their VPC do not traverse the public internet. Which AWS feature should they implement?",
        "choices": [
            "Amazon CloudFront distribution with origin access control",
            "VPC endpoint (AWS PrivateLink) for Amazon Bedrock",
            "AWS Direct Connect with a public virtual interface",
            "NAT gateway with an Elastic IP address"
        ],
        "correct_index": 1,
        "explanation": "VPC endpoints powered by AWS PrivateLink allow traffic between a VPC and Amazon Bedrock to stay entirely within the AWS network, never traversing the public internet. This is critical for organizations with strict security requirements that mandate private connectivity. A VPC endpoint creates a private entry point in the VPC for the Bedrock service, and combined with VPC endpoint policies, it provides fine-grained access control."
    },
    {
        "id": "d5_003",
        "domain": 5,
        "subdomain": "5.1",
        "difficulty": "foundational",
        "text": "Which AWS service is used to control which users and roles can invoke specific foundation models on Amazon Bedrock?",
        "choices": [
            "Amazon Cognito",
            "AWS Identity and Access Management (IAM)",
            "AWS Shield",
            "Amazon GuardDuty"
        ],
        "correct_index": 1,
        "explanation": "AWS IAM policies control access to Amazon Bedrock APIs, including which users, roles, or services can invoke specific foundation models. IAM policies can specify allowed actions (like bedrock:InvokeModel), restrict access to specific model IDs, and enforce conditions such as source IP or MFA requirements. This is the primary mechanism for managing who can use AI services within an AWS account."
    },
    {
        "id": "d5_004",
        "domain": 5,
        "subdomain": "5.1",
        "difficulty": "intermediate",
        "text": "A company wants to ensure that their custom model trained on Amazon SageMaker cannot be accessed by unauthorized AWS accounts. Which security control is most relevant?",
        "choices": [
            "Enable Amazon Macie to scan the model artifacts for sensitive data",
            "Configure the SageMaker model endpoint's resource-based policy to deny cross-account access and ensure the S3 bucket hosting model artifacts has restricted bucket policies",
            "Use AWS WAF to block unauthorized API calls to the model endpoint",
            "Deploy the model on a dedicated host to physically isolate it from other customers"
        ],
        "correct_index": 1,
        "explanation": "Protecting a custom model requires controlling access to both the model endpoint and the underlying model artifacts stored in S3. Resource-based policies on the SageMaker endpoint and S3 bucket policies can restrict access to only authorized principals and accounts. IAM policies on the roles used to access these resources provide an additional layer of control. WAF is for web application protection, not direct API access control for SageMaker."
    },
    {
        "id": "d5_005",
        "domain": 5,
        "subdomain": "5.1",
        "difficulty": "intermediate",
        "text": "Which security practice helps prevent prompt injection attacks when building applications with foundation models?",
        "choices": [
            "Increasing the model's temperature to randomize responses",
            "Validating and sanitizing user inputs, using system prompts to define boundaries, and implementing guardrails to filter harmful content",
            "Deploying the model on larger instances for better performance",
            "Disabling all logging to prevent attackers from seeing model behavior"
        ],
        "correct_index": 1,
        "explanation": "Prompt injection attacks attempt to manipulate a model into ignoring its instructions or performing unintended actions by crafting malicious inputs. Defense requires a multi-layered approach: validating and sanitizing user inputs before they reach the model, using system prompts to establish firm behavioral boundaries, and applying guardrails (like Amazon Bedrock Guardrails) to filter both inputs and outputs for harmful or policy-violating content."
    },
    # --- 5.2 Compliance (5 questions) ---
    {
        "id": "d5_006",
        "domain": 5,
        "subdomain": "5.2",
        "difficulty": "foundational",
        "text": "Under the AWS Shared Responsibility Model, who is responsible for ensuring that the data used to train a custom ML model on SageMaker complies with privacy regulations?",
        "choices": [
            "AWS is responsible because it provides the training infrastructure",
            "The customer is responsible because they own and control the training data",
            "The foundation model provider is responsible because they created the base model",
            "The responsibility is shared equally between AWS and the customer for all data"
        ],
        "correct_index": 1,
        "explanation": "Under the AWS Shared Responsibility Model, AWS is responsible for security 'of' the cloud (infrastructure, hardware, managed services), while the customer is responsible for security 'in' the cloud. Training data is customer-owned content, so the customer is fully responsible for ensuring their data complies with applicable privacy regulations like GDPR or HIPAA, including proper consent, data handling, and retention policies."
    },
    {
        "id": "d5_007",
        "domain": 5,
        "subdomain": "5.2",
        "difficulty": "intermediate",
        "text": "A healthcare company wants to use Amazon Bedrock to process patient records. Which compliance requirement must they address, and how does AWS support it?",
        "choices": [
            "PCI DSS compliance; they should use Amazon Bedrock's built-in payment processing features",
            "HIPAA compliance; they must sign a Business Associate Agreement (BAA) with AWS and ensure Amazon Bedrock is a HIPAA-eligible service",
            "SOX compliance; they need to use AWS Artifact to generate financial audit reports",
            "FedRAMP compliance; they should deploy to AWS GovCloud regardless of the data type"
        ],
        "correct_index": 1,
        "explanation": "Healthcare organizations processing Protected Health Information (PHI) must comply with HIPAA. To use AWS services for PHI, customers must sign a Business Associate Agreement (BAA) with AWS and only use HIPAA-eligible services. Amazon Bedrock is a HIPAA-eligible service, meaning AWS has implemented the controls necessary to support HIPAA compliance, but the customer remains responsible for configuring and using the service in a HIPAA-compliant manner."
    },
    {
        "id": "d5_008",
        "domain": 5,
        "subdomain": "5.2",
        "difficulty": "foundational",
        "text": "Where can an AWS customer download compliance reports such as SOC 2 and ISO 27001 audit reports for AWS services?",
        "choices": [
            "AWS Management Console under the Billing dashboard",
            "AWS Artifact",
            "Amazon Inspector",
            "AWS Config"
        ],
        "correct_index": 1,
        "explanation": "AWS Artifact is a self-service portal that provides on-demand access to AWS compliance reports and select online agreements. Customers can download audit reports including SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, and PCI DSS reports. These documents help customers demonstrate to their auditors and regulators that the underlying AWS infrastructure meets specific compliance standards."
    },
    {
        "id": "d5_009",
        "domain": 5,
        "subdomain": "5.2",
        "difficulty": "intermediate",
        "text": "A European company must comply with GDPR when using AI services. Which of the following is a key GDPR requirement related to AI-processed personal data?",
        "choices": [
            "All AI models must be open source to comply with GDPR",
            "Personal data must be stored in the EU, and individuals have the right to explanation of automated decisions that significantly affect them",
            "GDPR only applies to data stored on-premises, not in the cloud",
            "Companies must use only EU-built AI models for processing EU citizens' data"
        ],
        "correct_index": 1,
        "explanation": "GDPR includes provisions for data residency (data can be processed in approved regions with adequate protections), the right to explanation for significant automated decisions (Article 22), and other rights like data access, rectification, and erasure. AWS supports GDPR compliance by offering EU-based regions for data residency and providing tools for data management. Customers must configure their AI workloads to respect these rights."
    },
    {
        "id": "d5_010",
        "domain": 5,
        "subdomain": "5.2",
        "difficulty": "foundational",
        "text": "A company wants to ensure that data sent to Amazon Bedrock for inference is not used to train AWS foundation models. What assurance does AWS provide?",
        "choices": [
            "AWS uses all customer data to improve its models unless the customer pays for a premium opt-out tier",
            "AWS does not use customer inputs or outputs from Amazon Bedrock to train Amazon Titan or any other foundation models",
            "Customer data is used for model improvement by default but can be opted out via a support ticket",
            "AWS only uses anonymized data, so customers do not need to worry about data usage"
        ],
        "correct_index": 1,
        "explanation": "AWS explicitly states that customer inputs and outputs processed by Amazon Bedrock are not used to train Amazon Titan or any third-party foundation models available through the service. This is a default behavior, not an opt-out. This assurance is critical for customers with sensitive data who need confidence that their content remains private and is not incorporated into model training."
    },
    # --- 5.3 Monitoring and governance (4 questions) ---
    {
        "id": "d5_011",
        "domain": 5,
        "subdomain": "5.3",
        "difficulty": "foundational",
        "text": "Which AWS service records API calls made to Amazon Bedrock, including who made the call, when it was made, and what parameters were used?",
        "choices": [
            "Amazon CloudWatch",
            "AWS CloudTrail",
            "Amazon Inspector",
            "AWS Config"
        ],
        "correct_index": 1,
        "explanation": "AWS CloudTrail logs API calls made to AWS services, including Amazon Bedrock. Each log entry records the identity of the caller, the time of the call, the source IP address, the API action, and the request parameters. This audit trail is essential for security monitoring, compliance auditing, and troubleshooting. CloudWatch handles metrics and alarms, while CloudTrail specifically focuses on API activity logging."
    },
    {
        "id": "d5_012",
        "domain": 5,
        "subdomain": "5.3",
        "difficulty": "intermediate",
        "text": "A deployed ML model's prediction accuracy has degraded over time because the statistical properties of the input data have changed. What is this phenomenon called?",
        "choices": [
            "Overfitting",
            "Data drift (also known as feature drift or covariate shift)",
            "Model compression",
            "Gradient vanishing"
        ],
        "correct_index": 1,
        "explanation": "Data drift occurs when the statistical distribution of the input data in production diverges from the data the model was trained on. For example, a model trained on pre-pandemic consumer behavior may perform poorly on post-pandemic data because spending patterns shifted. Monitoring for data drift is critical for maintaining model reliability, and Amazon SageMaker Model Monitor can automatically detect drift and alert teams."
    },
    {
        "id": "d5_013",
        "domain": 5,
        "subdomain": "5.3",
        "difficulty": "intermediate",
        "text": "A company wants to track Amazon Bedrock usage and set up alerts when inference costs exceed a monthly threshold. Which combination of AWS services should they use?",
        "choices": [
            "AWS Artifact for cost reports and Amazon SNS for notifications",
            "Amazon CloudWatch for usage metrics and AWS Budgets for cost alerts",
            "AWS CloudTrail for cost logging and Amazon SQS for alert queuing",
            "Amazon SageMaker Model Monitor for cost tracking and AWS Lambda for notifications"
        ],
        "correct_index": 1,
        "explanation": "Amazon CloudWatch captures usage metrics for Amazon Bedrock, including invocation counts and token consumption, which can be used to create dashboards and alarms. AWS Budgets allows customers to set custom cost thresholds and receive alerts via email or SNS when actual or forecasted spending exceeds the defined budget. Together, these services provide comprehensive cost monitoring and governance for AI workloads."
    },
    {
        "id": "d5_014",
        "domain": 5,
        "subdomain": "5.3",
        "difficulty": "foundational",
        "text": "Why is model versioning important in AI governance?",
        "choices": [
            "It allows running multiple model versions simultaneously to increase throughput",
            "It enables tracking which model version produced specific predictions, supporting reproducibility, auditability, and the ability to roll back to a previous version if issues arise",
            "It reduces the storage cost of model artifacts by compressing older versions",
            "It automatically improves model accuracy by combining predictions from all versions"
        ],
        "correct_index": 1,
        "explanation": "Model versioning maintains a record of each model iteration, including its artifacts, configuration, and metadata. This is essential for governance because it enables teams to trace predictions back to a specific model version for auditing, reproduce results for regulatory inquiries, and quickly roll back to a known-good version if a new deployment introduces problems. Amazon SageMaker Model Registry supports model versioning and approval workflows."
    },
]
