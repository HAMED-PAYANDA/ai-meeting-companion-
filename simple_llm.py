from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# Pre-arranged credentials for Skills Network environment
my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
}

# Generation parameters for the model
params = {
    GenParams.MAX_NEW_TOKENS: 700, # Maximum output length
    GenParams.TEMPERATURE: 0.1,    # Controls creativity vs determinism
}

# Initialize model instance with model_id and credentials
LLAMA2_model = Model(
    model_id='meta-llama/llama-4-maverick-17b-128e-instruct-fp8', 
    credentials=my_credentials,
    params=params,
    project_id="skills-network",  
)

# Wrap with LangChain's WatsonxLLM interface
llm = WatsonxLLM(LLAMA2_model)  

# Prompt the model and print output
print(llm("How to read a book effectively?"))
