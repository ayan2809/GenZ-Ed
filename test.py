import os
import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key='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'
print(openai.api_key)
print(openai.Engine("davinci").search(
  documents=["Jquery is used to Manipulate DOM", "JavaScript is a high-level programming language that follows the ECMAScript standard. It was originally designed as a scripting language for websites but became widely adopted as a general-purpose programming language, and is currently the most popular programming language in use. JavaScript is usually found running in a web browser as interactive or automated content, ranging from popup messages and live clocks to large web applications. JavaScript is also commonly used in server-side programming through platforms like Node.js, or  in non-JavaScript applications where the base programming language lacks the high-level functionality that JavaScript offers.", "Web 3.0 is the new technology for the web"],
  query="What is Web 3.0?"
))
