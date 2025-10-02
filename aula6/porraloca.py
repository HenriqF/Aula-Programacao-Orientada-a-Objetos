with open("r.command", "w") as f:
    ans = "set n to _\nget n -->"
    for i in range(0, 100000, 2):
        ans += f"\nif n = {i}\n    show par\nif n = {i+1}\n    show impar"
        
    ans += "\nelse\n    show nao sei"

    f.write(ans)