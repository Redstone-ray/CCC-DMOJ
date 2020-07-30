from fractions import Fraction

def dec_to_proper_frac(num, deno):
   frac = Fraction(num % deno, deno)
   if num>=deno:
       if frac.numerator==0:
           print(num // deno)
       else:
           print(num // deno,
                 f"{frac.numerator}/{frac.denominator}")
   else:
       print(f"{frac.numerator}/{frac.denominator}")

dec_to_proper_frac(int(input()), int(input()))