# Contributing

Suggest relevant papers, technical posts, implementations, models, tutorials, replications and critiques through an issue or pull request.

For an addition, include:

- The title, authors in their published order, first public date, venue and primary-source URL.
- A short summary of the contribution and its connection to weight-space programming.
- What constructs or edits the weights, what training or feedback it uses, the saved artifact and how it executes.
- Public code, models, datasets and demonstrations when available.

For a correction, identify the entry and link to the source supporting the replacement. For a revised paper, name the version and explain what changed.

## Editing records

Records live in `library.json`. Keep each existing `id` stable. Use an existing record as a template; preserve the distinction between a first public date and the conference publication year. The `en.summary` field supplies the annotation in the README. Method details belong in `en.construction`, `en.training` and `en.execution`.

When adding a record, add its ID to the appropriate section in `GROUPS` in `scripts/sync.py`, then regenerate the derived files:

```sh
python3 scripts/sync.py --source library.json
python3 scripts/sync.py --check
```

Check the actual primary source and open resource links without signing in. Keep paper, code, model and demo links labeled by their purpose. Cite the original work for claims about its method or results.
