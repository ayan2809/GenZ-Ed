import os
import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key='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'
# print(openai.api_key)
# print(openai.Engine("davinci").search(
#   documents=["The German invasion in 1939, the massacre of the Jewish population and deportations to concentration camps led to the uprising in the Warsaw ghetto in 1943 and to the major and devastating Warsaw Uprising between August and October 1944. Warsaw gained the title of the 'Phoenix City' because it has survived many wars, conflicts and invasions throughout its long history. Most notably, the city required painstaking rebuilding after the extensive damage it suffered in World War II, which destroyed 85% of its buildings. On 9 November 1940, the city was awarded Poland's highest military decoration for heroism, the Virtuti Militari, during the Siege of Warsaw (1939). ", "JavaScript is a high-level programming language that follows the ECMAScript standard. It was originally designed as a scripting language for websites but became widely adopted as a general-purpose programming language, and is currently the most popular programming language in use. JavaScript is usually found running in a web browser as interactive or automated content, ranging from popup messages and live clocks to large web applications. JavaScript is also commonly used in server-side programming through platforms like Node.js, or  in non-JavaScript applications where the base programming language lacks the high-level functionality that JavaScript offers.", "Web 3.0 is the new technology for the web"],
#   query="When did the german invasion happen?"
# ))


# import os
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Answer.create(
  search_model="ada",
  model="curie",
  question="When did the warsaw ghetto uprising start?",
  documents=["The German invasion in 1939, the massacre of the Jewish population and deportations to concentration camps led to the uprising in the Warsaw ghetto in 1943 and to the major and devastating Warsaw Uprising between August and October 1944. Warsaw gained the title of the 'Phoenix City' because it has survived many wars, conflicts and invasions throughout its long history. Most notably, the city required painstaking rebuilding after the extensive damage it suffered in World War II, which destroyed 85% of its buildings. On 9 November 1940, the city was awarded Poland's highest military decoration for heroism, the Virtuti Militari, during the Siege of Warsaw (1939).", "Puppy B is sad."],
  examples_context="World War 2",
  examples=[["When did the german invasion happen?","It happened in 1939"]],
  max_tokens=5,
  stop=["\n", "<|endoftext|>"],
))
