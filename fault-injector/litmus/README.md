# Generating Schema Types

Using [sqlc-codegen Tool](https://sgqlc.readthedocs.io/en/latest/sgqlc.codegen.html)

Download the GraphQL schema from the server:
```bash
python3 -m sgqlc.introspection \
     --exclude-deprecated \
     -H "Authorization: ${TOKEN}" \
     https://localhost:9002/query \
     schema.json
```

Generate the Python module `schema.py` from the GraphQL schema `schema.json`:
```bash
sgqlc-codegen schema --docstrings -s chaos schema.json schema.py
```