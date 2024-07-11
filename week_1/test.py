

def longest_common_prefix(strs):
    prefix= strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break
    return prefix


str = ["flow","flower","float"]

# Input strings
# str = input("Enter the strings: ").split()

result = longest_common_prefix(str)

print("Longest Common Prefix:", result)
