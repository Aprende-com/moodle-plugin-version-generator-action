# Moodle Plugin Version Generator - GitHub Action
GitHub Action that increases version number from selected Moodle Plugins.

In order to make this work, include the following snippet in your **.github/workflows** directory as **moodle-plugin-version-generator.yaml**:

```
name: Moodle Plugin Version Generator
on:
  push:
    branches:
      - main
jobs:
  generate:
    name: Moodle Plugin Version Generator
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          ref: ${{ github.event.push.head.ref }}
      - name: Increase plugin version
        uses: Aprende-com/moodle-plugin-version-generator-action@v1
      - name: Add artifact to repo
        run: |
          git config --global user.name "${{ github.actor }}"
          git config --global user.email "${{ github.actor }}@users.noreply.github.com"
          git add --all
          git commit -m "docs: version.php increased the version number."
          git push
```
