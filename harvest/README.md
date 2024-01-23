Login to github
```
gh api login
```

Get the list of all the files in the git repo
```
curl https://api.github.com/repos/code4lib/2023.code4lib.org/git/trees/main\?recursive\=1 > output.json
gh api /repos/code4lib/2023.code4lib.org/git/trees/main\?recursive\=1 > output.json
```

Download all the files in the `_posts/` directory (excluding the `_posts/keynotes`)
```
zsh <(jq -r '.tree[] | select(.path | startswith("_posts/")) | select(.path | startswith("_posts/keynotes") | not) | "curl \("https://raw.githubusercontent.com/code4lib/2023.code4lib.org/main/\(.path)" | @sh) -o \(.path|@sh)"' output.json)
```


```
```