def execute(code):
    env, i, m, code = {}, 0, 0, ' '.join(code.split("\n")).split(" ") #env, codepointer, mempointer tokens
    while i < len(code):
        print(env)
        env[m] = env[m] if m in env else 0
        env[m] = env[m] + 1 if code[i] == "s" else env[m]-1 if code[i] == "k" else env[m]+int(input()) if code[i] == "!" else env[m]
        m = m+1 if code[i] == "skrr" else m-1 if code[i] == "rrks" else m
        print([env[m] if code[i] == ":" else chr(env[m]) if code[i] == "::" else ""][-1], end="", sep="")
        i = env[m] if code[i] == "tinha" else i+2 if (((code[i] == "ornintorrinco") and (env[m] != 0)) or (code[i] == "ornin" and (env[m] == 0))) else i+1