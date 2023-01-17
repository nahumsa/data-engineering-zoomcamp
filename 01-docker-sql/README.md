# Docker and SQL

## Data pipeline
```mermaid
flowchart LR
    id1[csv] --> id2(python script)
    id2 -->  id3[(Postgres)]
```