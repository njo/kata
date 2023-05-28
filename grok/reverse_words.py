def reverse_chars(chars):
   l, r = 0, len(chars) - 1
   while l < r:
      chars[l], chars[r] = chars[r], chars[l]
      l += 1
      r -= 1
   return chars

def reverse_words(sentence):
   sentence = reverse_chars(list(sentence))
   l = r = 0
   while l < len(sentence):
      while r < len(sentence):
         if sentence[r] == " ":
            r -= 1   # Move back to last letter
            break
         r += 1

      # Stop on last letter of the word
      sentence = sentence[:l] + reverse_chars(sentence[l:r+1]) + sentence[r+1:]
      
      r += 2
      l = r

      # Should be first letter of next word, if not move until that's true
      if r < len(sentence) and sentence[r] == " ":
         #asd  asd
         while r < len(sentence):
            if sentence[r] != " ":
               break

            r += 1

         # Remove spaces
         sentence = sentence[:l] + sentence[r:]
         r = l

   return "".join(sentence).strip()

for s in ["World  Hello", "1 2 3 foo"]:
   print(reverse_words(s))