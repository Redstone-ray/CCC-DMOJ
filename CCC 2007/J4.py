import sys

print("Is an anagram."if sorted([x for x in sys.stdin.readline() if x.isalpha()])==sorted([x for x in sys.stdin.readline() if x.isalpha()]) else "Is not an anagram.")