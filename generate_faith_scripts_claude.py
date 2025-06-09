import boto3
import json

# Initialize AWS Bedrock client (make sure you've configured AWS CLI with your keys)
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

def generate_script(index):
    # Claude prompt must start and end correctly
    prompt = f"""\n\nHuman: Generate a 60-second Christian video script:
1. Start with an attention-grabbing hook.
2. Include a scripture quote with the reference.
3. Add a faith-based declaration grounded in the verse.
4. End with a call to action like “Repeat after me”.
Theme: Identity in Christ.
Format as a script for video {index}.

\n\nAssistant:"""
    
    # Call Claude via Bedrock
    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",  # Use claude-v3 if it's enabled for your account
        body=json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 600,
            "temperature": 0.7
        }),
        contentType="application/json",
        accept="application/json"
    )

    # Read and return Claude's generated output
    result = json.loads(response['body'].read())
    return result['completion']

# Example usage
if __name__ == "__main__":
    script = generate_script(1)
    print("\n📜 Generated Script:\n")
    print(script)
