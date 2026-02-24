import json 

api_response = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''
parsed = json.loads(api_response)

print("Request ID:", parsed["id"])
print("Status:", parsed["status"])
print("Text:", parsed["result"]["text"])
print("Confidence:", parsed["result"]["confidence"])

if parsed["result"]["confidence"] < 0.9:
    print("Warning: Confidence is low")


result = {
  "id": "req_123",
  "reviewed" : True,
  "remarks" : "Response Processed"
}

response = json.dumps(result)
with open("response.json", "w") as f:
    json.dump(result, f)

# I have moved the response.json file from main folder to this assignment folder