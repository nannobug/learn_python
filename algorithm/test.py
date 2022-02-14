def lineUp(commands):
    commands_ls = list(commands)
    n = 0
    total = 0
    ans = 0
    for i in range(len(commands_ls)):
        if commands_ls[i] == "R" or commands_ls[i] == "L":
            n += 1
            total = total + (-1)^n
        if total == 0:
            ans += 1
    return ans

lineUp("LL")