## parameter:
section=6

## code:
template="\\section{{ }} %% Ex{}.{} \n\n"
for i in range(1,30):
    print(template.format(section,i), end="")
