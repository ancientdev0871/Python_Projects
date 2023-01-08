text = input(">")
lst = text.split(' ')
emoji = {
  "sunrise" : "🌅",
  ":)": "😃",
  ":(": "😔"
}
output = ""
for word in lst:
  output += emoji.get(word, word) + " "
print(output)