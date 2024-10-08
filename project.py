temperature=int(input("Please enter temperature: "))
rain=str(input("Is it raining?  (true/false)"))

if temperature>=30:
    print("You can wear a t-shirt and jeans.")

if temperature>=15:
    print("Wearing a pullover would be nice.")
    
if temperature>=5:
    print("You should wear a jacket.")
    
if rain== True:
    print("Don't forget your umbrella!")
else:
    print("There is no need for an umbrella.")