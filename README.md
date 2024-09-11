# Custom QnA Bot using Azure Language Service

This repository contains the code and resources for building a custom Question & Answering (Q&A) bot using Azure Language Service's Custom Question Answering feature. The bot is capable of understanding natural language queries and providing relevant answers from a custom knowledge base.

## Features

- **Custom Knowledge Base**: Build and manage your own Q&A knowledge base using Azure Language Service.
- **Natural Language Understanding**: Leverage Azure's powerful language models to understand and respond to user queries.
- **Flexible Deployment**: Deploy the bot to various platforms including Microsoft Teams, Slack, Web, and more.
- **Azure Integration**: Fully integrates with Azure resources such as Azure Bot Service, Azure Functions, and more.
- **Scalable and Secure**: Built on Azure infrastructure, ensuring scalability, security, and compliance.

## Getting Started

### Prerequisites

- An Azure subscription. If you don't have one, [create a free Azure account](https://azure.microsoft.com/free/).
- Azure Language Service enabled in your Azure subscription.
- Node.js and npm installed on your machine.
- Azure CLI installed on your machine.
- Knowledge of JavaScript or Python, depending on the codebase provided.

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/custom-qna-bot.git
   cd custom-qna-bot

2. **Install Dependencies:**
   ```bash
   npm install

3. **Configure Azure Language Service:**
- Create a Language Service resource in the Azure portal.
- Enable Custom Question Answering and create a knowledge base.
- Retrieve the Language Service Endpoint, Key, and Knowledge Base ID.
