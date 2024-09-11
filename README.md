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

4. **Update environment variables: Create a .env file in the root directory and add the following:**
   ```bash
   AZURE_LANGUAGE_ENDPOINT=<your-language-service-endpoint>
   AZURE_LANGUAGE_KEY=<your-language-service-key>
   KNOWLEDGE_BASE_ID=<your-knowledge-base-id>

### Usage
To run the bot locally:
```bash
npm start
```
Visit http://localhost:3978 to interact with the bot. You can also connect the bot to other channels like Microsoft Teams or Slack for a wider audience.

### Deployment
To deploy the Azure bot:
1. In Language Studio, on the custom question answering Deploy project page, select the Create a bot button.
   ![image](https://github.com/user-attachments/assets/ee969801-be60-4197-b9ff-4af4f99bb7ba)

2. A new browser tab opens for the Azure portal, with the Azure AI Bot Service's creation page. Configure the Azure AI Bot Service and hit the Create button.

| Setting         | Value                                                                               | 
|-----------------|-------------------------------------------------------------------------------------|
| Bot handle      | Unique identifier for your bot. This value needs to be distinct from your App name. | 
| Subscription    | Select your subscription.                                                           | 
| Resource group  | Select an existing resource group or create a new one                               |
| Location        | Select your desired location.                                                       | 
| Pricing tier    | Choose pricing tier                                                                 |
| App name        | App service name for your bot                                                       |
| SDK language    | C# or Node.js. Once the bot is created, you can download the code to your local development environment and continue the development process.|
| Language Resource Key | This key is automatically populated deployed custom question answering project |
| App service plan/Location | This value is automatically populated, do not change this value            | 

3. After the bot is created, open the Bot service resource.
   
4. Under Settings, select Test in Web Chat.

![image](https://github.com/user-attachments/assets/92674de5-b221-4a62-94a8-4b6baa96faf8)

5. At the chat prompt of Type your message, enter:
   ```bash
   How do I set up my surface book?
   ```
   The chatbot responds with an answer from your project.

   ![image](https://github.com/user-attachments/assets/078fc533-8411-4ed8-9371-f980ac5885e5)




