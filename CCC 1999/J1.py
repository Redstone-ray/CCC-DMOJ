'''
[three, four, ace, ..... ]
'''
def is_high_card(pos,num,cards):
    if pos+num>51:
        return 0
    c=cards[pos+1:pos+num+1]
    if 'ace' not in c and 'king' not in c and \
            'queen' not in c and 'jack' not in c:
                return num
# 0, ..., 51
l=[]
for i in range(52):
   a=input()
   l.append(a)

a_score=0
b_score=0
for i, card in enumerate(l):

   score=0
   if card=='ace':
       score=is_high_card(i,4,l)
   elif card=='king':
       score=is_high_card(i,3,l)
   elif card=='queen':
       score = is_high_card(i, 2, l)
   elif card=='jack':
       onecard=[l[i+1]]
       score = is_high_card(i, 1, l)

   if score!=0 and score!=None:
       if i%2==0:
           a_score+=score
           print('Player A scores',score,'point(s).')
       else:
           b_score+=score
           print('Player B scores',score,'point(s).')
print('Player A:',a_score,'point(s).')
print('Player B:',b_score,'point(s).')
