Login to github

```
gh api login
```

Get the list of all the files in the git repo

```
curl https://api.github.com/repos/code4lib/2024.code4lib.org/git/trees/main\?recursive\=1 > file_manifest.json
```

Or use the GH API with a token if you don't want to be rate limited

```
gh api /repos/code4lib/2024.code4lib.org/git/trees/main\?recursive\=1 > file_manifest.json
```

Download all the files in the `_posts/` directory (excluding the `_posts/keynotes`)

```
zsh <(jq -r '.tree[] | select(.path | startswith("_posts/")) | select(.path | startswith("_posts/keynotes") | not) | "curl \("https://raw.githubusercontent.com/code4lib/2024.code4lib.org/main/\(.path)" | @sh) -o \(.path|@sh)"' file_manifest.json)
```

Now extract the title and text from the markdown files and create a CSV file

```
python3 buildcsv.py
```
