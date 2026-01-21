parol = input("Parol kiriting: ")

uzunlik = len(parol) >= 8
katta_harf = any(c.isupper() for c in parol)
kichik_harf = any(c.islower() for c in parol)
raqam = any(c.isdigit() for c in parol)
maxsus = any(c in "!@#$%^&*()_+" for c in parol)

ball = uzunlik + katta_harf + kichik_harf + raqam + maxsus

print("\nParol tahlili:")
print(f"Uzunligi 8+         : {'✅' if uzunlik else '❌'}")
print(f"Katta harf bor      : {'✅' if katta_harf else '❌'}")
print(f"Kichik harf bor     : {'✅' if kichik_harf else '❌'}")
print(f"Raqam bor           : {'✅' if raqam else '❌'}")
print(f"Maxsus belgi bor    : {'✅' if maxsus else '❌'}")

if ball == 5:
    print("→ Bu juda kuchli parol! 🔥")
elif ball >= 4:
    print("→ Yaxshi parol, lekin yanada kuchaytirsa bo‘ladi.")
elif ball >= 3:
    print("→ O‘rtacha parol — yaxshiroq qilish mumkin.")
else:
    print("→ Zaif parol! Iltimos, kuchliroq tanlang.")
