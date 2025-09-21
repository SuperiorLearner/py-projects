import random
import string
import time

def crack_password(target):
    charset = string.ascii_letters + string.digits
    attempts = 0
    start_time = time.time()
    
    while attempts < 100_000_000:
        guess = ''.join(random.choices(charset, k=len(target)))
        attempts += 1
        
        if attempts % 100_000 == 0:
            elapsed = time.time() - start_time
            speed = attempts / elapsed if elapsed > 0 else 0
            print(f"{attempts:,} attempts | {speed:,.0f}/sec")
        
        if guess == target:
            elapsed = time.time() - start_time
            print(f"\nPASSWORD CRACKED: {guess}")
            print(f"Attempts: {attempts:,}")
            print(f"Time: {elapsed:.1f}s")
            return
    
    print(f"\nPassword not found after {attempts:,} attempts")
    print("Password is secure!")

password = input("Enter Password: ").strip()
if password:
    crack_password(password)
else:
    print("Empty password!")