import re

def transform_text(text):
    transformed_lines = []

    # Iterate over each line in the input text
    for line in text.strip().split("\n"):
        # Search for the patterns using regular expressions
        usecase_match = re.search(r'Use case: (\S+),', line)
        openssh_version_match = re.search(r'OpenSSH version: (\S+),', line)
        key_size_match = re.search(r'Key size: (\d+)', line)

        # If matches are found, format and append to the transformed_lines list
        if usecase_match and openssh_version_match and key_size_match:
            usecase = usecase_match.group(1)
            openssh_version = openssh_version_match.group(1)
            key_size = key_size_match.group(1)
            transformed_lines.append(f'{usecase} & {openssh_version} & {key_size} \\\\')

    return "\n".join(transformed_lines)

# Sample input text
text = """
\item Use case: port-forwarding, OpenSSH version: V\_8\_0\_P1, Key size: 64
            \item Use case: port-forwarding, OpenSSH version: V\_8\_0\_P1, Key size: 32
            \item Use case: port-forwarding, OpenSSH version: V\_7\_8\_P1, Key size: 16
            \item Use case: port-forwarding, OpenSSH version: V\_7\_8\_P1, Key size: 64
            \item Use case: port-forwarding, OpenSSH version: V\_7\_8\_P1, Key size: 32
            \item Use case: scp, OpenSSH version: V\_8\_0\_P1, Key size: 64
            \item Use case: scp, OpenSSH version: V\_8\_0\_P1, Key size: 32
            \item Use case: scp, OpenSSH version: V\_7\_8\_P1, Key size: 64
            \item Use case: scp, OpenSSH version: V\_7\_8\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_8\_7\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_8\_7\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_8\_7\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_8\_8\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_8\_8\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_8\_8\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_7\_0\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_7\_0\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_7\_0\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_6\_8\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_6\_8\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_6\_8\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_6\_2\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_6\_2\_P1, Key size: 24
            \item Use case: basic, OpenSSH version: V\_6\_2\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_6\_0\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_6\_0\_P1, Key size: 24
            \item Use case: basic, OpenSSH version: V\_6\_0\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_8\_1\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_8\_1\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_8\_1\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_6\_1\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_6\_1\_P1, Key size: 24
            \item Use case: basic, OpenSSH version: V\_6\_1\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_7\_2\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_7\_2\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_7\_2\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_8\_0\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_8\_0\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_8\_0\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_6\_3\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_6\_3\_P1, Key size: 24
            \item Use case: basic, OpenSSH version: V\_6\_3\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_6\_9\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_6\_9\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_6\_9\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_7\_1\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_7\_1\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_7\_1\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_7\_9\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_7\_9\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_7\_9\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_6\_7\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_6\_7\_P1, Key size: 24
            \item Use case: basic, OpenSSH version: V\_6\_7\_P1, Key size: 32
            \item Use case: basic, OpenSSH version: V\_7\_8\_P1, Key size: 16
            \item Use case: basic, OpenSSH version: V\_7\_8\_P1, Key size: 64
            \item Use case: basic, OpenSSH version: V\_7\_8\_P1, Key size: 32
            \item Use case: client, OpenSSH version: V\_8\_0\_P1, Key size: 16
            \item Use case: client, OpenSSH version: V\_8\_0\_P1, Key size: 64
            \item Use case: client, OpenSSH version: V\_8\_0\_P1, Key size: 32
            \item Use case: client, OpenSSH version: V\_7\_8\_P1, Key size: 16
            \item Use case: client, OpenSSH version: V\_7\_8\_P1, Key size: 32
"""

# Transform and print the text
print(transform_text(text))
