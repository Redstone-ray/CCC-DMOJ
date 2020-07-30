text = {
   "CU": "see you",
   ":-)": "I’m happy",
   ":-(": "I’m unhappy",
   ";-)": "wink",
   "(˜.˜)": "sleepy",
   "TA": "totally awesome",
   "CCC": "Canadian Computing Competition",
   "CUZ": "because",
   "TY": "thank-you",
   "YW": "you’re welcome",
   "TTYL": "talk to you later"
}

a = ""

while a != "TTYL":

   a = input()
   try:
       print(text[a])
   except:
       print(a)